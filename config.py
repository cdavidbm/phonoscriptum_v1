# configurar el cliente OSC
from pythonosc import udp_client
import json
import os

# Configuración del cliente OSC
client = udp_client.SimpleUDPClient("127.0.0.1", 57120)

# Path del archivo de configuración
CONFIG_FILE_PATH = "config.json"

# Valores predeterminados para la configuración
default_config = {
    "frecuencia_base": 100,
    "incremento": 1,
    "ataque": 2,
    "decaimiento": 1,
    "efectos": {
        "delay": {"active": False, "amount": 0},
        "distortion": {"active": False, "amount": 0},
        "noise": {"active": False, "amount": 0}
    }
}

# Cargar la configuración desde el archivo o usar valores predeterminados
def cargar_configuracion():
    """Carga la configuración desde un archivo JSON"""
    try:
        with open(CONFIG_FILE_PATH, 'r') as file:
            config = json.load(file)
    except FileNotFoundError:
        config = default_config
        guardar_configuracion(config)
    return config

# Guardar la configuración en el archivo
def guardar_configuracion(config):
    """Guarda la configuración en un archivo JSON"""
    with open(CONFIG_FILE_PATH, 'w') as file:
        json.dump(config, file, indent=4)
