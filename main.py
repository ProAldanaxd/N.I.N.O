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
    print(mensaje)
    webbrowser.open(url)

def abrir_app(mensaje, exe): 
    print(mensaje)
    os.startfile(exe)

paginas = { #Diccionario de opciones, donde cada una te lleva a una lista
    "abre youtube": ["Tch, ¿ahora quieres ver videos? Ahí tienes.", "https://www.youtube.com/?app=desktop&hl=es"],
    "abre crunchyroll": ["Solamente no te vayas a enviciar!", "https://www.crunchyroll.com/es/discover"],
    "abre spotify": ["Pero ni se te ocurra poner canciones malas!","https://open.spotify.com/intl-es/" ],
    "abre google": ["Abrelo tu...","https://www.google.com/?hl=es&zx=1790036817302"],
}

apps = {
    "abre word": ["Toma, ahora trabaja!","C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"],
    "abre outlook": ["Aqui tienes, tonto","C:/Program Files/WindowsApps/Microsoft.OutlookForWindows_1.2026.908.200_x64__8wekyb3d8bbwe"],
}

print(f"Nino: {nino['saludo']}")
while True: #Este while hace que nuestro jarvis (Nino) siempre esté esperando que le digan algo
    texto = input("Tu: ").strip().lower() #"Barra de accion" lo que tiene al lado ayuda un poco a que reconozca mas escrituras
    if texto == "salir": #Final
        print("N-No es como si queria hablar contigo o algo!")
        break
    elif texto in paginas: #Abrir paginas web
        datos = paginas[texto]
        abrir_url(datos[0], datos[1])
    elif texto == "crea una carpeta": #Crear carpetas
        nombre_carpeta = input("Hmph, ¿C-Como quieres que se llame tu carpeta?: ")
        if not os.path.exists(nombre_carpeta):
            print("Aqui tienes, tonto")
            os.makedirs(nombre_carpeta)
        else:
            print("Ya tienes una carpeta con ese nombre! no me hagas perder mi tiempo...")
    elif texto in apps:
        datos = apps[texto]
        abrir_app(datos[0], datos[1])
    else:
        resultado = pensar(texto)
        print("Nino: ",resultado)