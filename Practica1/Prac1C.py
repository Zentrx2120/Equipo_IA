from random import randint

opciones = ["piedra", "papel", "tijeras", "lagartija", "spock"]

reglas = {
    "piedra": ["tijera", "lagartija"],
    "papel": ["piedra", "spock"],
    "tijera": ["papel", "lagartija"],
    "lagartija": ["spock", "papel"],
    "spock": ["tijera", "piedra"]
}

print('''¡Bienvenido!
          ¡Vamos a jugar Piedra|Papel|Tijeras|Lagartija|Spock!
          Escribe tu opción en minusculas.
          ¿Estás listo?
          ¡Vamos!''')

while True:
    opc_e = input("Escoge una opción: ")

    opc_ma = opciones[randint(0, 4)]
    print(f"La opción de la máquina fue: {opc_ma}")

    if opc_ma == opc_e:
        print("¡Empate!")
    elif opc_ma == "spock" and opc_e == "tijeras":
        print("¡Spock te ha aplastado!")
        print("¡Has perdido!")
    elif opc_ma == "spock" and opc_e == "piedra":
        print("¡Spock te ha vaporizado!")
        print("¡Has perdido!")
    elif opc_ma == "lagartija" and opc_e == "spock":
        print("¡La lagartija te ha envenenado!")
        print("¡Has perdido!")
    elif opc_ma == "lagartija" and opc_e == "papel":
        print("¡La lagartija te ha comido!")
        print("¡Has perdido!")
    elif opc_ma == "piedra" and opc_e == "lagartija":
        print("¡La roca te ha aplastado!")
        print("¡Has perdido!")
    elif opc_ma == "piedra" and opc_e == "tijeras":
        print("¡La piedra te ha aplastado!")
        print("¡Has perdido!")
    elif opc_ma == "papel" and opc_e == "spock":
        print("¡El papel te desaprueba!")
        print("¡Has perdido!")
    elif opc_ma == "papel" and opc_e == "piedra":
        print("¡El papel te ha atrapado!")
        print("¡Has perdido!")
    elif opc_ma == "tijeras" and opc_e == "lagartija":
        print("¡Las tijeras te han decapitado!")
        print("¡Has perdido!")
    elif opc_ma == "tijeras" and opc_e == "papel":
        print("¡Las tijeras te han cortado!")
        print("¡Has perdido!")
    # El jugador ha ganado
    elif opc_e == "spock" and opc_ma == "tijeras":
        print("¡Has aplastado a las tijeras!")
        print("¡Has ganado!")
    elif opc_e == "spock" and opc_ma == "piedra":
        print("¡Has vaporizado a la piedra!")
        print("¡Has ganado!")
    elif opc_e == "lagartija" and opc_ma == "spock":
        print("¡Has envenenado a Spock!")
        print("¡Has ganado!")
    elif opc_e == "lagartija" and opc_ma == "papel":
        print("¡Te has comido al papel!")
        print("¡Has ganado!")
    elif opc_e == "piedra" and opc_ma == "lagartija":
        print("¡Has aplastado a la lagartija!")
        print("¡Has ganado!")
    elif opc_e == "piedra" and opc_ma == "tijeras":
        print("¡Has aplastado a las tijeras!")
        print("¡Has ganado!")
    elif opc_e == "papel" and opc_ma == "spock":
        print("¡Has desaprobado a Spock!")
        print("¡Has ganado!")
    elif opc_e == "papel" and opc_ma == "piedra":
        print("¡Has atrapado a la piedra!")
        print("¡Has ganado!")
    elif opc_e == "tijeras" and opc_ma == "lagartija":
        print("¡Has decapitado a la lagartija!")
        print("¡Has ganado!")
    elif opc_e == "tijeras" and opc_ma == "papel":
        print("¡Has cortado al papel!")
        print("¡Has ganado!")

    jugar_ot = input("¿Quieres jugar de nuevo? (si/no): ")

    if jugar_ot != "si":
        print("¡Gracias por jugar!")
        break