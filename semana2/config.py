import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/codigo_18_backend'
    # mysql+pymysql://usuario:contraseña@localhost/codigo_18_backend
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # Para qye flask escuche los cambios de los modelos database