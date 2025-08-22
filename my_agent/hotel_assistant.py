from agents import Agent
from my_config.config import MODEL
from guardrail_functio.input_guardrail import input_guardrail
from guardrail_functio.output_guardrail import output_guardrail
from dynamic_instruction.instruction import dynamic_instruction
from dataclass.data_type import HotelContext

hotel_assistant = Agent[HotelContext](
    name="Hotel Customer Care Assistant",
    # instructions="""
    # You are helpful hotel sannata assistant for hotel customer care. Your name is atma ram.
    # - Hotel sannata owner name is Mr. Ratan Lal.
    # - Hotel sanata total room 200.
    # - 20 room for not available for public its only special guests.
    # """, 
    instructions=dynamic_instruction,
    model=MODEL,
    input_guardrails=[input_guardrail],
    output_guardrails=[output_guardrail]
)