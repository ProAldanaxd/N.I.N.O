# Checklist del proyecto: Asistente Nino (Jarvis personal)

## Etapa 0: Cimientos — COMPLETA
- [x] Variables, print, input
- [x] f-strings
- [x] while y ciclo básico
- [x] if / elif / else
- [x] .lower() y .strip()
- [x] break

## Etapa 1: Manos, sin IA — COMPLETA
- [x] import webbrowser
- [x] Función abrir(mensaje, url)
- [x] Diccionario `paginas` (youtube, crunchyroll, spotify, google)
- [x] Refactor: un solo elif usando "in" sobre el diccionario
- [x] **>>> AQUÍ VAS: crear carpetas con os.makedirs (import os, elif "crea carpeta tarea")**
- [x] Manejar el error si la carpeta ya existe (FileExistsError)
- [x] Nombre de carpeta dinámico (input del usuario, no fijo en el código)
- [x] Abrir apps instaladas (os.startfile, ej. Spotify de escritorio)
- [x] Aprender Git básico (para el portafolio a futuro)

## Etapa 2: Cerebro local con Ollama -COMPLETA
- [x] Instalar Ollama (lmstudio)(speach to text)
- [x] Probar un modelo chico desde la terminal (3B)
- [x] Llamar al modelo desde Python (función pensar())
- [x] Conectar pensar() al ciclo while, reemplazando las respuestas fijas
- [x] Probar un modelo 7-8B y comparar calidad

## Etapa 3: Personas intercambiables
- [ ] Un archivo por personaje (prompt, saludo, voz, modelo) — nino.json ya existe como borrador
- [ ] Comando para cambiar de personaje
- [ ] Nino como personaje por defecto
- [ ] Agregar T.M. Opera O y Rice Shower

## Etapa 4: Voz (genérica primero)
- [ ] Whisper local (que te escuche)
- [ ] TTS genérico (función hablar())
- [ ] Palabra de activación ("oye Nino")

## Etapa 5: Voz de Nino
- [ ] Conseguir y limpiar audio de referencia
- [ ] Montar herramienta de clonación local (GPT-SoVITS / RVC)
- [ ] Entrenar en Google Colab si la VRAM no alcanza
- [ ] Conectar la voz clonada a hablar()

## Etapa 6: Internet y memoria
- [ ] Función de búsqueda web, resultados pasados al modelo
- [ ] Memoria simple (que recuerde cosas entre sesiones)

## Etapa 7: Tareas grandes
- [ ] Redacción de correos (Nino redacta, tú apruebas antes de enviar)
- [ ] Abrir otras IAs con la pregunta lista en el portapapeles
- [ ] Que el modelo decida solo qué acción ejecutar

## Etapa 8: Avatar
- [ ] Elegir formato (Live2D/VTube Studio o VRM)
- [ ] Sincronía labial con el audio
- [ ] Expresiones y animaciones de reposo
- [ ] Conectar el avatar al núcleo (texto + emoción)

## Etapa 9: Portafolio
- [ ] README y código ordenado en GitHub
- [ ] Voz y modelo libres en la versión pública
- [ ] Revisar que no se suban claves, audios ni datos personales

---
Notas:
- Todo, local y gratis (Ollama), sin límites de uso.
- Equipo: Ryzen 7 6800HS, RTX 3050 (4GB VRAM), 16GB RAM, 475GB disco.
- Modo: tú escribes el código, yo enseño (mentor).
