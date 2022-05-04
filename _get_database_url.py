from data.config import DIR, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME


DATABASE_URI = f'sqlite:///data/database.sqlite3'

if DB_USER and DB_PASSWORD and DB_HOST and DB_PORT and DB_NAME:
    DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

print(DATABASE_URI)
