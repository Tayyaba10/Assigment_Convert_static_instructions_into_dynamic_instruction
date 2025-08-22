from agents import RunContextWrapper,GuardrailFunctionOutput,input_guardrail,Runner
from my_agent.guardrail_agent import guardrail_agent

@input_guardrail
async def input_guardrail(ctx: RunContextWrapper,agent,input:str) -> GuardrailFunctionOutput:
    
    result = await Runner.run(guardrail_agent,input=input,context=ctx.context)
    
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_hotel_sannata_query and not result.final_output.is_hotel_virana_query,
    )