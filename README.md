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

## Ejecución

```powershell
.\.venv\Scripts\python.exe main.py
```

Escribir, por ejemplo: `¿Qué es una cadena de procesamiento? Explicalo en dos oraciones.`

El programa imprime el texto generado; no imprime el objeto `AIMessage` completo. Sin una API key configurada, finaliza con un mensaje que explica qué variable falta. Una pregunta vacía también se rechaza antes de realizar la consulta.

