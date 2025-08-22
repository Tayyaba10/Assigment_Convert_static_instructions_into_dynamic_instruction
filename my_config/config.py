import os
from dotenv import load_dotenv
from agents import AsyncOpenAI,OpenAIChatCompletionsModel

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
base_url = os.getenv("BASE_URL")

client = AsyncOpenAI(api_key=api_key,base_url=base_url)

MODEL = OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client)
