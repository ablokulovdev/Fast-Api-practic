from decouple import config

class Config():
    DB_NAME = config("DB_NAME")
    DB_USER = config("DB_USER")
    DB_PASS = config("DB_PASS")
    DB_HOST = config("DB_HOST")
    DB_PORT = config("DB_PORT")
    
core = Config()

