from os import getenv
from dotenv import load_dotenv

load_dotenv()
DATABASE_NAME: str = 'foodAwesome'
MYSQL_URI: str = f"mysql://{getenv('DATABASE_USERNAME')}:{getenv('DATABASE_PASSWORD')}@localhost/{DATABASE_NAME}"
MYSQL_TEST_URI: str = f"mysql://{getenv('DATABASE_USERNAME')}:{getenv('DATABASE_PASSWORD')}@localhost/{DATABASE_NAME}_test"

# Base config
class Config:
    SECRET_KEY: str = getenv('SECRET_KEY') or 'abcdefghijklm'
    APP_ADMIN: str | None = getenv('APP_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    @staticmethod
    def init_app(app) -> None:
        pass


# Development config
class DevelopmentConfig(Config):
    DEBUG: bool = True
    SQLALCHEMY_DATABASE_URI: str = MYSQL_URI


# Development config
class TestingConfig(Config):
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI: str = MYSQL_TEST_URI



config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
