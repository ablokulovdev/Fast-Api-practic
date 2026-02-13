from decouple import config


class Config():
    DB_NAME = config("DB_DATABASE"),
    DB_USER = config("DB_USERNAME"),
    DB_PASS = config("DB_PASSWORD"),
    DB_HOST = config("DB_HOST"),
    DB_PORT = config("DB_PORT")
    
    
core = Config()

