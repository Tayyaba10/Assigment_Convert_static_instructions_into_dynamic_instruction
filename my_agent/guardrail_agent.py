from agents import Agent
from my_config.config import MODEL
from dataclass.data_type import MyDataType

guardrail_agent = Agent(
    name="Guardrail Agent",
    instructions="""
    - This agent is responsible for ensuring that queries related to hotel sannata and hotel virana are handled correctly.
    - It checks if the query is about hotel sannata and virana, whether it pertains to account or tax issues
      and provides a reason for its classification.
    - The output will include whether the query is a hotel sannata and virana query, if it is related to account or tax issues,
      and a reason for the classification.
    """,
    model=MODEL,
    output_type=MyDataType
)
