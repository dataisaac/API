from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Declarar as variáveis que o Pydantic deve procurar no .env ou ambiente
    DATABASE_URL: str = ""
    STORAGE_TYPE: str = "MYSQL" # Valor padrão para o tipo de armazenamento
    # AWS_REGION: str = "us-east-1" # Valor padrão caso não encontre no .env

    # Configuração para carregar o arquivo .env
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding='utf-8'
    )

settings = Settings()