from agents import RunContextWrapper,GuardrailFunctionOutput,Runner,output_guardrail
from my_agent.guardrail_agent import guardrail_agent


@output_guardrail
async def output_guardrail(ctx:RunContextWrapper,agent,output:str) -> GuardrailFunctionOutput:
    
    result = await Runner.run(guardrail_agent, input=output, context=ctx.context)
    
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_hotel_sannata_political_query,
    )