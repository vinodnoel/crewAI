"""
Medical Research Crew
"""

from crewai import Crew, Process
from src.agents import researcher, analyst, writer
from src.tasks import create_research_task, create_analysis_task, create_writing_task


class MedicalResearchCrew:
    """Medical Research Crew that orchestrates agents for clinical research"""

    def __init__(self, condition: str):
        self.condition = condition
        self.crew = self._create_crew()

    def _create_crew(self) -> Crew:
        """Create and configure the crew"""
        research_task = create_research_task(self.condition)
        analysis_task = create_analysis_task(self.condition)
        writing_task = create_writing_task(self.condition)

        return Crew(
            agents=[researcher, analyst, writer],
            tasks=[research_task, analysis_task, writing_task],
            process=Process.sequential,
            verbose=True
        )

    def run(self) -> str:
        """Execute the crew and return results"""
        print(f"\n{'='*60}")
        print(f"Starting research on: {self.condition}")
        print(f"{'='*60}\n")

        result = self.crew.kickoff()
        return result
