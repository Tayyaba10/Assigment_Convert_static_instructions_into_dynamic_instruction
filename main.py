from agents import Agent,Runner,set_tracing_disabled,InputGuardrailTripwireTriggered,OutputGuardrailTripwireTriggered
from my_agent.hotel_assistant import hotel_assistant
from dataclass.data_type import data

set_tracing_disabled(True)

while True:
    user_input = input("Enter your query or type 'exit' to quite : ")
    
    if user_input == "exit":
        print("Exiting the program.")
        break
    
    try: 
        result = Runner.run_sync(starting_agent=hotel_assistant, input=user_input,context=data)
        print(result.final_output)
        
    except InputGuardrailTripwireTriggered as e:
        print(f"Tripwire triggered input: {e}")
    
    except OutputGuardrailTripwireTriggered as e:
        print(f"output tripwire triggered: {e}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")