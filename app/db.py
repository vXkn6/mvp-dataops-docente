from dotenv import load_dotenv
import os
import psycopg

load_dotenv()

def get_connection_params():
    return {
        "host": os.getenv("SUPABASE_DB_HOST"),
        "port": os.getenv("SUPABASE_DB_PORT", "5432"),
        "dbname": os.getenv("SUPABASE_DB_NAME", "postgres"),
        "user": os.getenv("SUPABASE_DB_USER"),
        "password": os.getenv("SUPABASE_DB_PASSWORD"),
        "sslmode": "require",
    }

def test_connection():
    params = get_connection_params()
    missing = [k for k, v in params.items() if k != "sslmode" and not v]
    if missing:
        return {"status": "error", "detail": "Faltan variables: " + ", ".join(missing)}

    try:
        with psycopg.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute("select version^(^);")
                version = cur.fetchone()[0]
        return {"status": "ok", "detail": "Conexion exitosa", "db_version": version}
    except Exception as e:
        return {"status": "error", "detail": str(e)}
