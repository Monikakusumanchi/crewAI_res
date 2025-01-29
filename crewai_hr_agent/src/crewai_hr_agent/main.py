#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crewai_hr_agent.crew import CrewaiHrAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'job_url': 'https://www.mckinsey.com/careers/search-jobs/jobs/associate-15178',
        'company_name': 'Mckinsey & Co.'
    }
    
    try:
        CrewaiHrAgent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


