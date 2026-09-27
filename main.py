import ollama #Libreria en la cual vamos a usar la API
import webbrowser #Libreria para abrir paginas web
import os #Libreria para crear carpetas/abrir aplicaciones
import json #Archivos json que son de texto, para darle instrucciones a la IA
with open("nino.json", "r", encoding="utf-8") as archivo:
    nino = json.load(archivo)

prompt_final = nino["prompt"].replace("{USUARIO}", "JC")

historial = [
    {"role": "system", "content": prompt_final}
]

def pensar(mensaje):
    historial.append({"role": "user", "content": mensaje})
    respuesta = ollama.chat(model="llama3.1:8b", messages=historial)
    texto_respuesta = respuesta["message"]["content"]
    historial.append({"role": "assistant", "content": texto_respuesta})
    return texto_respuesta

def abrir_url(mensaje, url): #2 variables en este ejemplo, cuando llamas a la funcion lo primero sera el mensaje y lo segunda la url que se va a abrir
    print("Nino:",mensaje)
    webbrowser.open(url)

def abrir_app(mensaje, exe): 
    print("Nino:",mensaje)
    os.startfile(exe)

paginas = { #Diccionario de opciones, donde cada una te lleva a una lista
    "abre youtube": ["https://www.youtube.com/?app=desktop&hl=es"],
    "abre crunchyroll": ["https://www.crunchyroll.com/es/discover"],
    "abre spotify": ["https://open.spotify.com/intl-es/" ],
    "abre google": ["https://www.google.com/?hl=es&zx=1790036817302"],
}

apps = {
    "abre word": ["C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"],
    "abre outlook": ["shell:AppsFolder/Microsoft.OutlookForWindows_8wekyb3d8bbwe!Microsoft.OutlookforWindows"],
}

saludo = pensar("El usuario te esta saludando, devuelvele el saludo")
print("Nino:",saludo)
while True: #Este while hace que nuestro jarvis (Nino) siempre esté esperando que le digan algo
    texto = input("Tu: ").strip().lower() #"Barra de accion" lo que tiene al lado ayuda un poco a que reconozca mas escrituras
    if texto == "salir": #Final
        print("Nino:",pensar(texto))
        break
    elif texto in paginas: #Abrir paginas web
        datos = paginas[texto]
        abrir_url(pensar(texto), datos[0])
    elif texto == "crea una carpeta": #Crear carpetas
        pregunta = pensar("El usuario quiere crear una carpeta. Pregúntale cómo se debe llamar, en una sola frase corta.")
        print("Nino:",pregunta)
        nombre_carpeta = input("Tu: ").strip().lower()
        if not os.path.exists(nombre_carpeta):
            print("Nino:",pensar(f"El usuario quiere crear una carpeta con el nombre {nombre_carpeta}"))
            os.makedirs(nombre_carpeta)
            print("Nino:",pensar(f"Acabo de crear la carpeta '{nombre_carpeta}'"))
        else:
            print("Nino:",pensar(f"La carpeta con el nombre '{nombre_carpeta}' ya existe"))
    elif texto in apps:
        datos = apps[texto]
        abrir_app(pensar(texto), datos[0])
    else:
        resultado = pensar(texto)
        print("Nino:",resultado)