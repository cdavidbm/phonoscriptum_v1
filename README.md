# Phonoscriptum v1.0: Generador de Frecuencias para Frases

Este proyecto convierte palabras y frases en frecuencias de audio y las envía a SuperCollider para su reproducción. También permite configurar efectos de audio como delay, distorsión y ruido.

## Requisitos

- Python 3.x
- SuperCollider

## Instalación

### Instalación de SuperCollider

1. Descarga e instala SuperCollider desde su [sitio oficial](https://supercollider.github.io/download).
2. Una vez instalado, abre SuperCollider y ejecuta el siguiente código para iniciar el servidor:
3. Carga el archivo `FullSynth.scd` en SuperCollider y ejecuta el código presionando:

(Windows y Linux)
```
CTRL Enter
```

## Instalación del Proyecto

Clona este repositorio:
```bash
git clone https://github.com/cdavidbm/phonoscriptum_v1.git
cd phonoscriptum_v1
```

## Instala las dependencias de Python:
```bash
pip install python-osc
```

## Uso

Asegúrate de que SuperCollider esté ejecutándose y que hayas cargado y ejecutado el archivo `FullSynth.scd`.

Ejecuta el programa principal en Python:
```bash
python main.py
```

Sigue las instrucciones en pantalla para convertir palabras o frases a frecuencias, encontrar combinaciones de letras para un número objetivo, configurar parámetros de audio y efectos.

## Configuración

El archivo `config.json` contiene la configuración predeterminada del programa, incluyendo la frecuencia base, el incremento, el ataque, el decaimiento y los efectos de audio. Puedes editar este archivo directamente o usar las opciones del menú en el programa para actualizar la configuración.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request con tus mejoras.

## Demo

Puedes ver una versión online, un poco mas sencilla en esta ruta:

https://phonoscriptum.netlify.app
