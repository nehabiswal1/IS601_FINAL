from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    mailtrap_host: str
    mailtrap_port: int
    mailtrap_username: str
    mailtrap_password: str
    
    minio_endpoint: str
    minio_access_key: str
    minio_secret_key: str
    minio_bucket_name: str
    minio_public_endpoint: str

    class Config:
        # env_file = ".env"  # Specifies the location of the .env file
        # Point to the .env file
        Path(__file__).resolve().parent / ".env"
        env_file_encoding = 'utf-8'
# Instantiate the settings
settings = Settings()

print(settings.dict())