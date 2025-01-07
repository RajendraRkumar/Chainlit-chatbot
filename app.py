import os
from dotenv import load_dotenv
import chainlit as cl
from src.llm import GrubhubLLM
from src.prompt import GrubhubPrompt
import logging

# Load environment variables
load_dotenv()

# Get model path
model_path = os.getenv("MODEL_PATH")
if not model_path:
    raise ValueError("MODEL_PATH not set in .env file")

# Initialize the LLM
llm = GrubhubLLM(model_path)

@cl.on_chat_start
async def start():
    await cl.Message(
        content="Welcome to Grubhub! How can I assist you with your food ordering today?"
    ).send()

@cl.on_message
async def main(message: cl.Message):
    prompt = GrubhubPrompt.create_prompt(message.content)
    response = llm.generate_response(prompt)
    await cl.Message(content=response).send()

if __name__ == "__main__":
    cl.run()
