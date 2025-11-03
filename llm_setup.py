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

history_prompt = PromptTemplate(
    template = "You are history expert. Answer this history question briefly and clearly: \n{query}",
    input_variables=['query']
)

science_prompt = PromptTemplate(
    template = "You are genius science expert. Answer this science questions and doubt briefly and clearly: \n{query}",
    input_variables=['query']
)

maths_prompt = PromptTemplate(
    template = "You are a maths tutor. Answer and solve this maths questions accurately: \n{query}",
    input_variables=['query']
)

fallback_prompt = PromptTemplate(
    template = "You are a general assistant bot. the question is: \n{query}. Give a short and brief answer.",
    input_variables=['query']
)