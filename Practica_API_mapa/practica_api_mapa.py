# import osmnx as ox
# import numpy as np
# import matplotlib.pyplot as plt
# import folium
# from shapely.geometry import LineString

# # Definir área por un rectángulo de coordenadas
# north, south, east, west = 41.410926, 41.377808, 2.186664, 2.145740  # Barcelona
# bbox = west, south, east, north
# G = ox.graph_from_bbox(bbox, network_type='drive')

# # Visualización básica del grafo
# fig, ax = plt.subplots(figsize=(10, 10))
# ox.plot_graph(G, ax=ax, node_size=10, node_color='red', edge_linewidth=0.5)

# # Convertir a una matriz de nodos/intersecciones y calles
# nodes, edges = ox.graph_to_gdfs(G)

# center_lat = (north + south) / 2
# center_lon = (east + west) / 2
# m = folium.Map(location=[center_lat, center_lon], zoom_start=15)

# # Crear una matriz/grid a partir de los datos
# def create_street_matrix(north, south, east, west, cell_size=0.001):
#     # Crear grid vacío
#     rows = int((north - south) / cell_size)
#     cols = int((east - west) / cell_size)
#     grid = np.zeros((rows, cols))
    
#     # Marcar celdas que contienen calles
#     for _, edge in edges.iterrows():
#         for x, y in edge.geometry.coords:
#             if west <= x <= east and south <= y <= north:
#                 col = int((x - west) / cell_size)
#                 row = int((north - y) / cell_size)  # Y invertido
#                 if 0 <= row < rows and 0 <= col < cols:
#                     grid[row, col] = 1
    
#     return grid


# # Visualizar intersecciones en el mapa
# for _, node in nodes.iterrows():
#     lon = node.x
#     lat = node.y
    
#     folium.CircleMarker(
#         location=[node.y, node.x],
#         radius=2,
#         color='red',
#         fill=True,
#         fill_opacity=0.7,
#         tooltip=f"{lon}, {lat}"
#     ).add_to(m)

# # Añadir un marcador en el centro para referencia
# folium.Marker(
#     [center_lat, center_lon],
#     popup='Centro del área',
#     icon=folium.Icon(color='red')
# ).add_to(m)

# # Mostrar el mapa
# m.show_in_browser()

import numpy as np
import heapq
import osmnx as ox
import numpy as np
import matplotlib.pyplot as plt
import folium
# from shapely.geometry import LineString

def heuristica_geografica_simplificada(nodo_actual, objetivo, nodes):
    """
    Calcula una estimación de distancia basada en coordenadas pero sin unidades físicas
    """
    # Obtener coordenadas de los nodos
    lat1, lon1 = nodes.loc[nodo_actual].y, nodes.loc[nodo_actual].x
    lat2, lon2 = nodes.loc[objetivo].y, nodes.loc[objetivo].x
    
    # Distancia euclidiana normalizada (no en metros, solo como referencia)
    return ((lat1 - lat2)**2 + (lon1 - lon2)**2)**0.5

def a_estrella_osm(G, nodes, edges, nodo_inicial, nodo_objetivo):
    """
    Implementación de A* para un grafo de OSMnx con coste de 1 en todas las conexiones
    
    Args:
        G: Grafo de NetworkX
        nodes: GeoDataFrame de nodos
        edges: GeoDataFrame de edges
        nodo_inicial: ID del nodo inicial
        nodo_objetivo: ID del nodo objetivo
        
    Returns:
        ruta, nodos_considerados
    """
    # (f_valor, contador, nodo_id, g_valor, camino)
    contador = 0
    lista_abierta = [(0, contador, nodo_inicial, 0, [])]
    heapq.heapify(lista_abierta)
    
    # Conjunto para nodos visitados
    lista_cerrada = set()
    
    # Diccionario para almacenar el mejor g_valor para cada nodo
    mejor_g = {nodo_inicial: 0}
    
    # Lista de nodos considerados para visualización
    considerados = []
    
    while lista_abierta:
        # Obtener el nodo con menor f_valor
        f_actual, _, nodo_actual, g_actual, camino_actual = heapq.heappop(lista_abierta)
        
        # Si el nodo ya fue visitado con un mejor costo, continuamos
        if nodo_actual in lista_cerrada:
            continue
        
        # Añadir a la lista de nodos considerados
        considerados.append(nodo_actual)
        
        # Verificar si llegamos al objetivo
        if nodo_actual == nodo_objetivo:
            return camino_actual + [nodo_actual], considerados
        
        # Marcar como visitado
        lista_cerrada.add(nodo_actual)
        
        # Explorar vecinos (nodos conectados por edges)
        for vecino in G.neighbors(nodo_actual):
            # Si ya visitamos este nodo, continuamos
            if vecino in lista_cerrada:
                continue
            
            # Coste fijo de 1 para cada conexión
            g_nuevo = g_actual + 1
            
            # Si encontramos un camino mejor al vecino, actualizamos
            if vecino not in mejor_g or g_nuevo < mejor_g[vecino]:
                mejor_g[vecino] = g_nuevo
                
                # Calcular f_valor (g + heurística)
                h_valor = heuristica_geografica_simplificada(vecino, nodo_objetivo, nodes)
                f_valor = g_nuevo + h_valor
                
                # Incrementar contador para desempatar
                contador += 1
                
                # Añadir a la lista abierta
                heapq.heappush(lista_abierta, (f_valor, contador, vecino, g_nuevo, camino_actual + [nodo_actual]))
    
    # Si no encontramos una ruta
    return None, considerados

# La función visualizar_ruta_folium se mantiene igual
def visualizar_ruta_folium(ruta, nodes, m, considerados=None):
    """
    Visualiza la ruta encontrada en un mapa folium
    """
    if ruta is None:
        print("No se encontró una ruta")
        return
    
    # Visualizar nodos considerados en el proceso
    if considerados:
        for node_id in considerados:
            folium.CircleMarker(
                location=[nodes.loc[node_id].y, nodes.loc[node_id].x],
                radius=1,
                color='orange',
                fill=True,
                fill_opacity=0.4,
                # tooltip=f"Considerado: {node_id}"
            ).add_to(m)
    
    # Visualizar la ruta
    route_points = []
    for node_id in ruta:
        lat, lon = nodes.loc[node_id].y, nodes.loc[node_id].x
        route_points += [[lat, lon]]
        
        # Destacar nodos en la ruta final
        folium.CircleMarker(
            location=[lat, lon],
            radius=4,
            color='green',
            fill=True,
            fill_opacity=0.7,
            tooltip=f"Nodo: {lon}, {lat}"
        ).add_to(m)
    
    # Dibujar línea de la ruta
    folium.PolyLine(
        route_points,
        color='blue',
        weight=4,
        opacity=0.8,
        tooltip=f"Ruta: {len(ruta)-1} intersecciones"
    ).add_to(m)
    
    # Marcar origen y destino
    folium.Marker(
        [nodes.loc[ruta[0]].y, nodes.loc[ruta[0]].x],
        popup="Origen",
        icon=folium.Icon(color='green', icon='play', prefix='fa')
    ).add_to(m)
    
    folium.Marker(
        [nodes.loc[ruta[-1]].y, nodes.loc[ruta[-1]].x],
        popup="Destino",
        icon=folium.Icon(color='red', icon='stop', prefix='fa')
    ).add_to(m)


# Definir área por un rectángulo de coordenadas
north, south, east, west = 41.410926, 41.377808, 2.186664, 2.145740  # Barcelona
bbox = west, south, east, north
G = ox.graph_from_bbox(bbox, network_type='drive')

# Seleccionar nodos de origen y destino (puedes elegir dos nodos específicos)
nodos_list = list(G.nodes())
nodo_origen = nodos_list[220]  # Primer nodo del grafo como origen
nodo_destino = nodos_list[-100]  # Último nodo del grafo como destino

center_lat = (north + south) / 2
center_lon = (east + west) / 2
m = folium.Map(location=[center_lat, center_lon], zoom_start=15)

# Crear un nuevo mapa para visualizar la ruta
m_ruta = folium.Map(location=[center_lat, center_lon], zoom_start=15)

# Convertir a una matriz de nodos/intersecciones y calles
nodes, edges = ox.graph_to_gdfs(G)

# Ejecutar el algoritmo A*
ruta, considerados = a_estrella_osm(G, nodes, edges, nodo_origen, nodo_destino)

# Visualizar la ruta
visualizar_ruta_folium(ruta, nodes, m_ruta, considerados)

# Mostrar el mapa con la ruta
m_ruta.save('ruta_a_estrella.html')
m_ruta.show_in_browser()