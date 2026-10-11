# Unidad 2 — Refactorización a LCEL Asíncrono

Ejercicio de Coderhouse AI Engineering: recibir una pregunta del usuario, preparar mensajes con roles system/human, consultar un modelo OpenAI mediante LangChain y mostrar la respuesta como texto.

El flujo principal es `ChatPromptTemplate | ChatOpenAI | StrOutputParser`. Se ejecuta con `await cadena.ainvoke({"pregunta": pregunta})` dentro de `main()`, iniciada por `asyncio.run(main())`.

## Archivos

| Archivo | Función |
| --- | --- |
| `main.py` | Configuración y ejecución de la cadena asíncrona. |
| `requirements.txt` | Dependencias Python. |
| `.env.example` | Plantilla pública de configuración, sin credenciales. |
| `.gitignore` | Excluye `.env`, entornos virtuales y cachés. |
| `.env` | Configuración local. No se incorpora al repositorio. |

## Preparación en Windows

Requiere Python 3.12 y una API key de OpenAI con acceso al modelo configurado. Las consultas utilizan la API de OpenAI.

Desde la carpeta del proyecto, en PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Crear el archivo local de configuración si todavía no existe:

```powershell
Copy-Item .env.example .env
```

Editar `.env` y completar `OPENAI_API_KEY` con una clave real. El modelo predeterminado es `gpt-4o-mini`; puede cambiarse mediante `OPENAI_MODEL`.

```dotenv
OPENAI_API_KEY=
OPENAI_MODEL=gpt-4o-mini
```

No publicar la clave ni incorporar `.env` al repositorio. El ZIP inicial incluye un `.env` sin clave para facilitar la preparación local. Quien clone el repositorio deberá copiar `.env.example` a `.env`.

## Ejecución

```powershell
.\.venv\Scripts\python.exe main.py
```

Escribir, por ejemplo: `¿Qué es una cadena de procesamiento? Explicalo en dos oraciones.`

El programa imprime el texto generado; no imprime el objeto `AIMessage` completo. Sin una API key configurada, finaliza con un mensaje que explica qué variable falta. Una pregunta vacía también se rechaza antes de realizar la consulta.

## Validación y límites

- El flujo equivalente se ejecutó previamente con Ollama local.
- La sintaxis de esta adaptación a OpenAI fue comprobada.
- La llamada real a OpenAI está pendiente de prueba con una API key válida. La prueba con Ollama no valida la integración ni las credenciales de OpenAI.
- Las respuestas pueden variar; extraer texto con el parser no verifica su exactitud factual.

## Subir a GitHub

Crear un repositorio vacío en GitHub, sin agregar README ni `.gitignore` desde la web. Dentro de esta carpeta:

```powershell
git init
git add main.py requirements.txt README.md .gitignore .env.example
git status
```

Verificar que `.env` y `.venv` no estén preparados para el commit. Luego:

```powershell
git commit -m "Agregar ejercicio de LCEL asincrono con OpenAI"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
git push -u origin main
```

Reemplazar la URL por la del repositorio real. Entregar el enlace del repositorio y asegurar que el docente tenga acceso.

## Referencias

- [Consumo de OpenAI con LangChain](https://docs.langchain.com/oss/python/integrations/chat/openai)
- [OpenAI API: inicio rápido](https://developers.openai.com/api/docs/quickstart)
- [Modelo GPT-4o mini](https://developers.openai.com/api/docs/models/gpt-4o-mini)
