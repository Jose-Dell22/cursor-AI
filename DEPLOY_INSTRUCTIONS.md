# Instrucciones de Deploy en Vercel

## Estructura del Proyecto
Este proyecto tiene dos partes principales:
- **Frontend**: Next.js 15 con TypeScript
- **Backend**: FastAPI con Python

## Pasos para el Deploy

### 1. Deploy del Backend

1. **Crear cuenta en Vercel** (si no tienes una)
   - Ve a [vercel.com](https://vercel.com)
   - Regístrate con tu cuenta de GitHub

2. **Deploy del Backend**
   - Ve al dashboard de Vercel
   - Haz clic en "New Project"
   - Importa tu repositorio de GitHub
   - Selecciona la carpeta `Backend` como directorio raíz
   - Vercel detectará automáticamente que es un proyecto Python
   - Haz clic en "Deploy"

3. **Configurar variables de entorno del Backend**
   - En el dashboard de Vercel, ve a tu proyecto del backend
   - Ve a "Settings" > "Environment Variables"
   - Agrega las variables necesarias (si las tienes)

4. **Obtener la URL del backend**
   - Una vez desplegado, copia la URL que te da Vercel
   - Ejemplo: `https://tu-backend.vercel.app`

### 2. Deploy del Frontend

1. **Configurar variables de entorno**
   - En el dashboard de Vercel, crea un nuevo proyecto
   - Importa el mismo repositorio pero selecciona la carpeta `Frontend`
   - Ve a "Settings" > "Environment Variables"
   - Agrega la variable:
     ```
     NEXT_PUBLIC_API_URL=https://tu-backend.vercel.app
     ```
   - Reemplaza `https://tu-backend.vercel.app` con la URL real de tu backend

2. **Deploy del Frontend**
   - Haz clic en "Deploy"
   - Vercel detectará automáticamente que es un proyecto Next.js

### 3. Configuración de CORS (si es necesario)

Si tienes problemas de CORS, modifica el archivo `Backend/app/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://tu-frontend.vercel.app"  # Agrega tu dominio de frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 4. Verificar el Deploy

1. **Backend**: Visita `https://tu-backend.vercel.app/health`
2. **Frontend**: Visita `https://tu-frontend.vercel.app`

## URLs de Ejemplo

- **Backend**: `https://platziflix-backend.vercel.app`
- **Frontend**: `https://platziflix-frontend.vercel.app`

## Troubleshooting

### Error: "Module not found"
- Asegúrate de que el archivo `lib/api.ts` existe en el frontend
- Verifica que las importaciones sean correctas

### Error: "CORS policy"
- Verifica que la URL del backend en las variables de entorno sea correcta
- Asegúrate de que el backend tenga configurado CORS correctamente

### Error: "Build failed"
- Revisa los logs de build en Vercel
- Verifica que todas las dependencias estén en `package.json` y `requirements.txt`

## Comandos Útiles

```bash
# Probar el backend localmente
cd Backend
uvicorn app.main:app --reload

# Probar el frontend localmente
cd Frontend
npm run dev

# Build del frontend
cd Frontend
npm run build
``` 