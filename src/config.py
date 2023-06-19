from distutils.command.config import config
from distutils.debug import DEBUG

class Config:
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*S^'


class DevelopmentConfig(Config):
    MYSQL_HOST = 'softmatter.mysql.pythonanywhere-services.com'
    MYSQL_USER = 'softmatter'
    MYSQL_PASSWORD  = 'Flask123'
    MYSQL_DB  = 'softmatter$flask'

config ={
    'development': DevelopmentConfig
}