from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mailtrap_host: str
    mailtrap_port: int
    mailtrap_username: str
    mailtrap_password: str

    class Config:
        env_file = ".env"  # Specifies the location of the .env file

# Instantiate the settings
settings = Settings()

