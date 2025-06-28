from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")


# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


agent = Agent(
    name = "Translator",
    instructions = "You are a helpful translator. Always translate urdu sentences into clear and simple english."
)

response = Runner.run_sync(
    agent,
    input = " ئی سی کا طالب علم ہوں۔ میرا نام میر عاطف ایس ڈیتھو ہے۔ میں جی آئی اے ",
    run_config = config
)

print(response)




# def main():
#     print("Hello uv!")


# if __name__ == "__main__":
#     main()




# .venv\scripts\activate