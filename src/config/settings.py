"""
Configuration settings for CrewAI Medical Research Assistant
"""

import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # OpenAI Configuration
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")

    # Model Configuration (using cheap model with token limits)
    model_name: str = os.getenv("MODEL_NAME", "gpt-4o-mini")
    llm_temperature: float = float(os.getenv("LLM_TEMPERATURE", "0.7"))
    max_tokens: int = int(os.getenv("MAX_TOKENS", "1000"))

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
