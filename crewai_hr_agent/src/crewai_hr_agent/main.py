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
        'job_url': 'https://www.google.com/about/careers/applications/jobs/results/116221099686929094-account-executive-midmarket-sales-google-customer-solutions',
        'company_name': 'Google'
    }
    
    try:
        CrewaiHrAgent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


