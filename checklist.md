# Checklist del proyecto: Asistente Nino (Jarvis personal)

## Etapa 0: Cimientos — COMPLETA
- [x] Variables, print, input
- [x] f-strings
- [x] while y ciclo básico
- [x] if / elif / else
- [x] .lower() y .strip()
- [x] break

## Etapa 1: Manos, sin IA — EN PROGRESO
- [x] import webbrowser
- [x] Función abrir(mensaje, url)
- [x] Diccionario `paginas` (youtube, crunchyroll, spotify, google)
- [x] Refactor: un solo elif usando "in" sobre el diccionario
- [x] Crear carpetas con os.makedirs
- [x] Manejar el error si la carpeta ya existe (if not os.path.exists / else)
- [x] Nombre de carpeta dinámico (input del usuario, no fijo en el código)
- [x] Abrir apps instaladas (os.startfile, ej. Word) — con función y diccionario separados de las páginas web (abrir_app / apps)
- [x] Aprender Git básico (init, add/commit, push a GitHub) — ETAPA 1 COMPLETA

## Etapa 2: Cerebro local con Ollama
- [x] Instalar Ollama
- [x] pip install ollama en un venv propio del proyecto, con .gitignore para no subir .venv a GitHub
- [x] Probar un modelo chico desde la terminal (llama3.2:3b, responde bien en español)
- [x] Llamar al modelo desde Python (función pensar())
- [x] Conectar pensar() al ciclo while, reemplazando las respuestas fijas — Nino ya responde de verdad en el else
- [x] Probar un modelo 7-8B (llama3.1:8b) y comparar calidad — ETAPA 2 COMPLETA

## Etapa 3: Personas intercambiables
- [x] nino.json completo (prompt largo, personalidad post-declaración), conectado a pensar() vía "role": "system"
- [x] Historial de conversación (lista que crece con .append) para memoria de corto plazo y menos relectura del prompt
- [x] Fix de ambigüedad de identidad usuario/personaje (regla explícita: "tú eres Nino, quien te escribe es {USUARIO}")
- [x] Nino como personaje por defecto (es el único que existe por ahora, y responde bien)
- [x] Fix del historial en acciones: abrir_url/abrir_app ahora reciben pensar(texto) como mensaje, así que registran la acción en el historial y Nino reacciona con personalidad en vez de frase fija (solución propia, más elegante que el plan original)
- [x] "Crea una carpeta" integrado con pensar(): primero pregunta el nombre generando la pregunta con pensar() (mensaje explícito, evitando que el modelo alucine que ya se creó), pide el nombre con input() simple, ejecuta la lógica real, y reacciona con un mensaje descriptivo del resultado real (creada / ya existía) — confirmado que usa el historial para notar repeticiones
- **PAUSADO por decisión propia:** comando para cambiar de personaje y agregar T.M. Opera O / Rice Shower — se retoman más adelante, después de dejar a Nino sólida
- [ ] Comando para cambiar de personaje (pausado)
- [ ] Agregar T.M. Opera O y Rice Shower (pausado)

**>>> AQUÍ VAS AHORA: seguir puliendo/probando a Nino sola antes de avanzar a otras etapas o personajes**

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
