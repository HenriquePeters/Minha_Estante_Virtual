import os

class Config:
    SECRET_KEY = "chave_secreta_123"  # troque se quiser
    SQLALCHEMY_DATABASE_URI = "sqlite:///estante.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
