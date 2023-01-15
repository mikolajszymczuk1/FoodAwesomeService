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

    @staticmethod
    def init_app(app) -> None:
        pass


# Development config
class DevelopmentConfig(Config):
    DEBUG: bool = True


# Development config
class TestingConfig(Config):
    TESTING: bool = True
    WTF_CSRF_ENABLED: bool = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
