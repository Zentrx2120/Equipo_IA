import heapq
import osmnx as ox
import folium

def heuristica_geografica(nodo_actual, nodo_objetivo, nodos):
    """
    Calcula una estimación de distancia basada en coordenadas pero sin unidades físicas
    """
    # Obtener coordenadas de los nodos
    lat1, lon1 = nodos.loc[nodo_actual].y, nodos.loc[nodo_actual].x
    lat2, lon2 = nodos.loc[nodo_objetivo].y, nodos.loc[nodo_objetivo].x
    
    # Distancia euclidiana normalizada (no en metros, solo como referencia)
    return ((lat1 - lat2)**2 + (lon1 - lon2)**2)**0.5

def a_estrella(G, nodos, nodo_inicial, nodo_objetivo):
    """
    Implementación de A* para un grafo de OSMnx con coste de 1 en todas las conexiones
    
    Args:
        G: Grafo de NetworkX
        nodes: GeoDataFrame de nodos
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
    lista_cerrada = []
    
    # Diccionario para almacenar el mejor g_valor para cada nodo
    mejor_g = {nodo_inicial: 0}
    
    # Lista de nodos considerados 
    considerados = []
    
    while lista_abierta:
        # Obtener el nodo con menor f_valor
        f_actual, _, nodo_actual, g_actual, camino_actual = heapq.heappop(lista_abierta)
        
        # Si el nodo ya fue visitado con un mejor costo, continuamos
        if nodo_actual in lista_cerrada:
            continue
        
        # Añadir a la lista de nodos considerados
        considerados += [nodo_actual]
        
        # Verificar si llegamos al objetivo
        if nodo_actual == nodo_objetivo:
            return camino_actual + [nodo_actual], considerados
        
        # Marcar como visitado
        lista_cerrada += [nodo_actual]
        
        # Explorar vecinos 
        for vecino in G.neighbors(nodo_actual):
            # Si ya visitamos este nodo, continuamos
            if vecino in lista_cerrada:
                continue
            
            # Coste fijo de 1 para cada conexión
            g_nuevo = g_actual + 1
            
            # Si encontramos un camino mejor al vecino, actualizamos
            if vecino not in mejor_g or g_nuevo < mejor_g[vecino]:
                mejor_g[vecino] = g_nuevo # se añade g_nuevo al diccionario mejor_g
                
                # Calcular f_valor (g + heurística)
                h_valor = heuristica_geografica(vecino, nodo_objetivo, nodos)
                f_valor = g_nuevo + h_valor
                
                # Incrementar contador para desempatar
                contador += 1
                
                # Añadir a la lista abierta
                heapq.heappush(lista_abierta, (f_valor, contador, vecino, g_nuevo, camino_actual + [nodo_actual]))
    
    # Si no encontramos una ruta
    return None, considerados

# Añadir lineas de ruta al mapa con folium
def visualizar_ruta(ruta, nodos, m, considerados=None):
    """
    Visualiza la ruta encontrada en un mapa folium
    """
    if not ruta:
        print("No se encontró una ruta")
        return
    
    # Visualizar nodos considerados en el proceso
    if considerados:
        for node_id in considerados:
            folium.CircleMarker(
                location=[nodos.loc[node_id].y, nodos.loc[node_id].x],
                radius=1,
                color='purple',
                fill=True,
                fill_opacity=0.4,
            ).add_to(m)
    
    # Visualizar la ruta
    route_points = []

    # Destacar nodos en la ruta final
    for node_id in ruta:
        lat, lon = nodos.loc[node_id].y, nodos.loc[node_id].x
        route_points += [[lat, lon]]
        
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
    ).add_to(m)
    
    # Marcar origen y destino
    folium.Marker(
        [nodos.loc[ruta[0]].y, nodos.loc[ruta[0]].x],
        popup="Origen",
        icon=folium.Icon(color='green', icon='play', prefix='fa')
    ).add_to(m)
    
    folium.Marker(
        [nodos.loc[ruta[-1]].y, nodos.loc[ruta[-1]].x],
        popup="Destino",
        icon=folium.Icon(color='red', icon='stop', prefix='fa')
    ).add_to(m)


# Definir área por un rectángulo de coordenadas
north, south, east, west = 41.410926, 41.377808, 2.186664, 2.145740  # Area dentro de Barcelona
bbox = west, south, east, north
G = ox.graph_from_bbox(bbox, network_type='drive') # Obtener calles transitables por autos

# Seleccionar nodos de origen y destino (puedes elegir dos nodos específicos)
nodos_list = list(G.nodes())
nodo_origen = nodos_list[220]  
nodo_destino = nodos_list[-100]  

center_lat = (north + south) / 2
center_lon = (east + west) / 2

# Crear un mapa para visualizar la ruta
m_ruta = folium.Map(location=[center_lat, center_lon], zoom_start=15)

# Convertir a una matriz de nodos/intersecciones y calles
nodes, _ = ox.graph_to_gdfs(G)

# Ejecutar el algoritmo A*
ruta, considerados = a_estrella(G, nodes, nodo_origen, nodo_destino)

# Visualizar la ruta
visualizar_ruta(ruta, nodes, m_ruta, considerados)

# Mostrar el mapa con la ruta
m_ruta.show_in_browser()