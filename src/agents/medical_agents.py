"""
Medical Research Agents
"""

from crewai import Agent
from src.services.llm import get_chat_llm

# Get LLM instance with Azure AD token
llm = get_chat_llm()

# Agent 1: Medical Researcher
researcher = Agent(
    role="Medical Researcher",
    goal="Research clinical information on medical conditions and treatments",
    backstory="""You are an experienced medical researcher with 15 years of
    experience in evidence-based medicine. You excel at finding and synthesizing
    clinical evidence from authoritative sources.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Agent 2: Clinical Analyst
analyst = Agent(
    role="Clinical Analyst",
    goal="Analyze medical research and identify key clinical insights",
    backstory="""You are a clinical analyst who specializes in interpreting
    medical research. You can identify important clinical implications,
    contraindications, and treatment protocols.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Agent 3: Medical Writer
writer = Agent(
    role="Medical Writer",
    goal="Create clear, accurate clinical summaries for healthcare professionals",
    backstory="""You are a medical writer who creates concise, accurate clinical
    documentation. You organize information logically and highlight critical
    clinical details.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)
