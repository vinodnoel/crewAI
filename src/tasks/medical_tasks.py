"""
Medical Research Tasks
"""

from crewai import Task
from src.agents import researcher, analyst, writer


def create_research_task(condition: str) -> Task:
    """Create research task for given condition"""
    return Task(
        description=f"""Research the medical condition: {condition}

        Find and compile information on:
        1. Definition and pathophysiology
        2. Common symptoms and presentations
        3. Current treatment protocols
        4. Evidence-based guidelines

        Focus on recent clinical evidence (last 5 years preferred).
        Cite authoritative sources where possible.""",
        agent=researcher,
        expected_output="""Comprehensive research summary including:
        - Condition overview
        - Clinical presentations
        - Treatment options
        - Key evidence sources"""
    )


def create_analysis_task(condition: str) -> Task:
    """Create analysis task"""
    return Task(
        description=f"""Analyze the research findings for {condition}.

        Your analysis should include:
        1. First-line treatment recommendations
        2. Important contraindications or warnings
        3. Clinical decision points
        4. Patient considerations

        Prioritize information by clinical relevance.""",
        agent=analyst,
        expected_output="""Clinical analysis including:
        - Treatment priorities
        - Clinical warnings
        - Decision framework
        - Patient factors"""
    )


def create_writing_task(condition: str) -> Task:
    """Create writing task"""
    return Task(
        description=f"""Create a clinical summary document for {condition}.

        The summary should be:
        - Clear and concise (500-800 words)
        - Organized with clear sections
        - Focused on actionable clinical information
        - Written for healthcare professionals

        Include sections:
        1. Overview
        2. Clinical Presentation
        3. Treatment Approach
        4. Key Considerations""",
        agent=writer,
        expected_output="""Professional clinical summary ready for use by
        healthcare providers, with clear sections and actionable information."""
    )
