import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


async def main():
  # Buscar .env junto a este archivo, independientemente de la carpeta actual.
  load_dotenv(Path(__file__).resolve().parent / ".env")

  if not os.getenv("OPENAI_API_KEY", "").strip():
        raise SystemExit(
            "Falta OPENAI_API_KEY. Configurá tu clave en el archivo .env "
            "o en las variables de entorno."
        )

  # 1. Definir los roles y la variable que recibirá la pregunta.
  prompt = ChatPromptTemplate.from_messages([
        ("system", "Sos un asistente educativo. Respondé en español de forma breve y clara."),
        ("human", "{pregunta}"),
  ])

  # 2. Definir el modelo y tomar la clave de OPENAI_API_KEY. 
  modelo = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL") or "gpt-4o-mini",
        temperature=0,
  )

  # 3. Extraer el texto de la respuesta.
  parser = StrOutputParser()

  # 4. Construir el flujo principal.
  cadena = prompt | modelo | parser

  pregunta = input("Escribí tu pregunta: ").strip()
  if not pregunta:
        raise SystemExit("Se debe ingresar una pregunta.")

  # 5. Ejecutar el flujo y mostrar la respuesta.
  respuesta = await cadena.ainvoke({"pregunta": pregunta})

  print("\nRespuesta:")
  print(respuesta)

if __name__ == "__main__":
  asyncio.run(main())
