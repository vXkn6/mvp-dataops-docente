# MVP DataOps Docente

Repositorio piloto para preparar, probar y documentar un entorno tecnico reproducible para soluciones de datos e IA.

## Objetivo
Contar con una base tecnica simple y replicable para que los grupos de estudiantes puedan trabajar con:
- Python 3
- FastAPI
- Docker
- Git y GitHub
- GitHub Actions
- Render
- Supabase (PostgreSQL)

## Arquitectura del MVP
La solucion implementa una arquitectura IA hibrida simple:
- Aplicacion Python dockerizada
- API con FastAPI
- CI/CD con GitHub Actions
- Despliegue en Render
- Base de datos PostgreSQL en Supabase

## Estructura del proyecto
```text
mvp-dataops-docente/
├─ app/
│  ├─ __init__.py
│  ├─ main.py
│  └─ db.py
├─ tests/
│  └─ test_health.py
├─ data/
├─ .github/
│  └─ workflows/
│     └─ ci.yml
├─ .env.example
├─ .gitignore
├─ .dockerignore
├─ Dockerfile
├─ README.md
├─ render.yaml
└─ requirements.txt
```

## Endpoints actuales
- `GET /` : verifica que la API este activa
- `GET /health` : verifica salud general
- `GET /db-health` : verifica conexion a Supabase

## Ejecucion local
1. Clonar el repositorio
2. Crear archivo `.env` a partir de `.env.example`
3. Activar entorno virtual
4. Instalar dependencias
5. Ejecutar:

```bash
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

## Pruebas
Ejecutar:

```bash
python -m pytest -v
```

## Docker
Construir imagen:

```bash
docker build -t mvp-dataops-docente .
```

Ejecutar contenedor:

```bash
docker run --name mvp-dataops-docente-container -p 8000:8000 mvp-dataops-docente
```

## CI/CD
El workflow `.github/workflows/ci.yml`:
- instala dependencias
- ejecuta pruebas automaticas
- valida el proyecto en cada push a `main`

## Render
El servicio web se despliega en Render usando Docker y `render.yaml`.
URL publica actual:

```text
https://mvp-dataops-docente.onrender.com
```

## Supabase
La conexion a PostgreSQL se realiza mediante variables de entorno:
- `SUPABASE_DB_HOST`
- `SUPABASE_DB_PORT`
- `SUPABASE_DB_NAME`
- `SUPABASE_DB_USER`
- `SUPABASE_DB_PASSWORD`

## Estado actual del piloto docente
- [x] Repositorio creado y conectado a GitHub
- [x] App minima en FastAPI
- [x] Docker operativo
- [x] Tests locales funcionando
- [x] GitHub Actions en verde
- [x] Servicio desplegado en Render
- [x] Conexion publica a Supabase verificada
- [ ] Carga de datos desde .xlsx
- [ ] Insercion de datos en tablas
- [ ] Endpoint de lectura de datos
- [ ] Primer flujo de prediccion

## Uso docente sugerido
1. Probar este repositorio piloto de punta a punta
2. Replicar la misma estructura en los repositorios de los grupos
3. Pedir que cada grupo configure sus variables y despliegue su propia version
4. Evaluar sobre una base tecnica comparable

## Siguiente etapa sugerida
Implementar la primera funcionalidad de datos:
- cargar un archivo `.xlsx`
- procesarlo con Python
- insertar registros en Supabase
- exponer un endpoint para consultar los datos
