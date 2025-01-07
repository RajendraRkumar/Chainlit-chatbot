from setuptools import setup, find_packages

setup(
    name="grubhub-chainlit-bot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "chainlit",
        "torch",
        "transformers",
        "python-dotenv",
    ],
    author="Rajendra Kumar",
    author_email="kumrajenn@gmail.com",
    description="A Grubhub chatbot using Chainlit and GPT-Neo",
    keywords="chatbot, grubhub, chainlit, gpt-neo",
)
