# syntax=docker/dockerfile:1
FROM python:3.11-slim

# Instala curl y wget para soporte Dev Containers
RUN apt-get update && apt-get install -y curl wget && rm -rf /var/lib/apt/lists/*

# Instala uv (gestor de dependencias ultrarrápido)
RUN pip install --no-cache-dir uv

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de dependencias primero para aprovechar el cache
COPY pyproject.toml .
COPY poetry.lock .

# Instala las dependencias
RUN uv pip compile pyproject.toml -o requirements.txt
RUN uv pip install --system --no-deps --upgrade -r requirements.txt

# Copia el resto del código de la aplicación
COPY ./app ./app
COPY ./specs ./specs
# Expone el puerto 8000
EXPOSE 8000

# Comando por defecto para desarrollo (hot reload)
CMD ["uv", "run", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"] 