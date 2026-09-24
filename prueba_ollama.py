import ollama

def pensar(mensaje):
    respuesta = ollama.chat(model="llama3.2:3b", messages=[
        {"role": "user", "content": mensaje}
    ])
    return respuesta["message"]["content"]

resultado = pensar("Hola, ¿quién eres?")
print(resultado)