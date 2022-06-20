from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:toor@localhost:5432/faculdade'
    DBBaseModel = declarative_base()

    JWT_SECRET: str = '3ELOAL6bH2uqaKRegvsUBaj7PFcPIen2lMr7vFSb_wg'
    '''
    import secrets

    token: str = secrets.token_urlsafe(32)
    '''
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # uma semana em minutos

    class Config:
        case_sensitive = True


settings: Settings = Settings()
