"""
CrewAI Medical Research Assistant
Entry point for running the medical research crew
"""

from src.crews import MedicalResearchCrew


def run_medical_research(condition: str) -> str:
    """Run the medical research crew for a given condition"""
    crew = MedicalResearchCrew(condition)
    return crew.run()


if __name__ == "__main__":
    # Test with a medical condition
    condition = "Type 2 Diabetes"

    result = run_medical_research(condition)

    print("\n" + "="*60)
    print("FINAL OUTPUT:")
    print("="*60)
    print(result)
