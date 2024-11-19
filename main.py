# Archivo principal que importa y organiza las funciones de los demás módulos

from config import cargar_configuracion, guardar_configuracion, client
from frecuencias import crear_diccionario_frecuencias, frase_a_frecuencias
from color import generar_color_hexadecimal
from combinaciones import encontrar_combinaciones_optimizada
from input_usuario import obtener_numero_objetivo

def enviar_frecuencias(frecuencias, modo='simultaneo'):
    """Envía frecuencias a SuperCollider con los efectos especificados"""
    config = cargar_configuracion()
    efectos = config.get("efectos", {})
    print(f"\n-> Enviando frecuencias: {frecuencias} Hz a SuperCollider")
    print(f"   Modo: {modo}")
    print(f"   Ataque: {config['ataque']}s, Decaimiento: {config['decaimiento']}s\n")
    
    # Procesar efectos
    delay_amount = efectos["delay"]["amount"] if efectos["delay"]["active"] else 0
    dist_amount = efectos["distortion"]["amount"] if efectos["distortion"]["active"] else 0
    noise_amount = efectos["noise"]["amount"] if efectos["noise"]["active"] else 0

    # Asegurar que frecuencias sea una lista
    if not isinstance(frecuencias, list):
        frecuencias = [frecuencias]

    # Enviar mensaje OSC
    client.send_message("/frecuencia_palabra", 
                       [modo, *frecuencias, config['ataque'], config['decaimiento'],
                        delay_amount, dist_amount, noise_amount])

def actualizar_configuracion():
    """Actualiza los parámetros de configuración"""
    config = cargar_configuracion()
    print("\n=== Configuración Actual ===")
    print(f"1) Frecuencia base: {config['frecuencia_base']}")
    print(f"2) Incremento: {config['incremento']}")
    print(f"3) Ataque (segundos): {config['ataque']}")
    print(f"4) Decaimiento (segundos): {config['decaimiento']}")
    print("\nIntroduce el número de la opción que deseas modificar o '0' para regresar.")

    opciones = {
        "1": ("frecuencia_base", "Introduce el nuevo valor para frecuencia base: ", float),
        "2": ("incremento", "Introduce el nuevo valor para incremento: ", float),
        "3": ("ataque", "Introduce el nuevo valor para ataque (segundos): ", float),
        "4": ("decaimiento", "Introduce el nuevo valor para decaimiento (segundos): ", float)
    }

    opcion = input("Opción: ")
    if opcion in opciones:
        param, mensaje, tipo = opciones[opcion]
        try:
            valor = tipo(input(mensaje))
            if valor >= 0:
                config[param] = valor
                guardar_configuracion(config)
                print("Configuración actualizada con éxito.\n")
            else:
                print("El valor debe ser un número positivo.")
        except ValueError:
            print(f"Entrada inválida. Se requiere un número {tipo.__name__}.")

def configurar_efectos():
    """Configura los efectos de audio"""
    config = cargar_configuracion()
    efectos = config.get("efectos", {
        "delay": {"active": False, "amount": 0},
        "distortion": {"active": False, "amount": 0},
        "noise": {"active": False, "amount": 0}
    })

    print("\n=== Configuración de Efectos ===")
    print("1) Delay")
    print("2) Distortion")
    print("3) Noise")
    print("Introduce el número del efecto que deseas modificar o '0' para regresar.")

    opciones = {
        "1": "delay",
        "2": "distortion",
        "3": "noise"
    }

    opcion = input("Opción: ")
    if opcion in opciones:
        efecto = opciones[opcion]
        active = input(f"¿Activar {efecto}? (s/n): ").lower() == 's'
        amount = float(input(f"Introduce el valor para {efecto} (valor entre 0 y 1): ")) if active else 0
        efectos[efecto] = {"active": active, "amount": amount}
        config["efectos"] = efectos
        guardar_configuracion(config)
        print(f"Efecto {efecto} configurado con éxito.\n")
    else:
        print("Opción no válida, por favor elige una opción del menú.\n")

def main():
    """Función principal del programa"""
    frecuencias = crear_diccionario_frecuencias()

    print("=== Generador de Frecuencias para Frases ===")
    print("Escribe '0' y presiona 'Enter' en cualquier momento para detener el sonido.\n")

    while True:
        print("---------------------------------------------------")
        print("Selecciona una opción:")
        print(" 1) Convertir una palabra o frase a frecuencia")
        print(" 2) Encontrar combinaciones de letras para un número objetivo")
        print(" 3) Configuración")
        print(" 4) Configurar efectos de audio")
        print("---------------------------------------------------")
        
        opcion = input("Introduce una opción (o '0' para terminar el sonido): ")

        if opcion == "0":
            pass
           # break
        elif opcion == "1":
            texto = input("\nIntroduce una palabra o frase: ")
            frecuencias_palabras = frase_a_frecuencias(texto, frecuencias)
            colores = generar_color_hexadecimal(texto)
            print(f"\nFrecuencias para: '{texto}'\n{frecuencias_palabras}")
            print(f"Colores hexadecimales: {colores}\n")
            enviar_frecuencias(frecuencias_palabras)
        elif opcion == "2":
            objetivo = obtener_numero_objetivo()
            combinaciones = encontrar_combinaciones_optimizada(frecuencias, objetivo)
            print(f"\nCombinaciones encontradas para {objetivo}: {combinaciones}\n")
        elif opcion == "3":
            actualizar_configuracion()
        elif opcion == "4":
            efectos = configurar_efectos()
            print(f"Efectos configurados: {efectos}\n")
        else:
            print("Opción no válida, por favor elige una opción del menú.\n")

if __name__ == "__main__":
    main()
