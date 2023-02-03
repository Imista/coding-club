import random

# Desarrolla un programa en Python que simule el juego: Piedra, papel o tijera.

if __name__ == "__main__":
    # Declarar variables
    opciones = ['piedra', 'papel', 'tijera']

    while (True):
        opc_maquina = opciones[random.randint(0, 2)].lower()
        opc_user = input(
            "Elije una opcion entre 'piedra' 'papel' 'tijera': ").lower()

        # Validar
        if not opc_user in opciones:
            print('Opcion invalida')
        else:
            print("*"*5, "Elecciones", "*"*5)
            print("Maquina: ", opc_maquina)
            print("Usuario: ", opc_user)
            # Empate
            if opc_maquina == opc_user:
                print('Hubo un empate')
            elif opc_user == 'piedra':
                if opc_maquina == 'tijera':
                    print('Gana el usuario con ', opc_user)
                else:
                    print('Gana la maquina con ', opc_maquina)
            elif opc_user == 'papel':
                if opc_maquina == 'piedra':
                    print('Gana el usuario con ', opc_user)
                else:
                    print('Gana la maquina con ', opc_maquina)
            elif opc_user == 'tijera':
                if opc_maquina == 'papel':
                    print('Gana el usuario con ', opc_user)
                else:
                    print('Gana la maquina con ', opc_maquina)
            # Cerrar bucle
            if input("\n¿Quieres seguir jugador? S/N: ").lower() == 'n':
                break
