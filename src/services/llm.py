"""
=============================================================================
LLM.PY - LLM Service (OpenAI Direct)
=============================================================================
Simple OpenAI configuration for CrewAI.
=============================================================================
"""

import os
from crewai import LLM
from src.config.settings import settings

# Set OpenAI API key in environment
os.environ["OPENAI_API_KEY"] = settings.openai_api_key


def get_chat_llm() -> LLM:
    """
    Create a CrewAI LLM instance with OpenAI.

    Uses gpt-4o-mini by default (cheap model).

    Returns:
        LLM: Configured CrewAI LLM for OpenAI
    """
    return LLM(
        model=settings.model_name,
        temperature=settings.llm_temperature,
        max_tokens=settings.max_tokens,
    )
