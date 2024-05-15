import os

def mysql_uri() -> str:
    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "password")
    server = os.getenv("DB_HOST", "db")
    port = os.getenv("DB_PORT", "3306")
    db = os.getenv("DB_NAME", "app")
    return f"mysql://{user}:{password}@{server}:{port}/{db}"
