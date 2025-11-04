from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite",
    temperature=0.7,
    api_key=os.environ["GEMINI_API_KEY"]
)

intent_prompt = PromptTemplate(
    template = """
    You are an intent classifier for a chatbot.
    You are given a list of intents in JSON format:
    {context}

    User query: {query}

    Your task:
    - compare the user query with intent descriptions and examples.
    Return the **name** of the most relevant intent(e.g. history, science, maths or fallback).
    - Reply with the name only, no explaination 
"""
)