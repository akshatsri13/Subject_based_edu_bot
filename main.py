from fastapi import FastAPI
from pydantic import BaseModel
from handlers.fallback_handler import handle_fallback
from handlers.history_handler import handle_history
from handlers.maths_handler import handle_maths
from handlers.science_handler import handle_science
from intent_clasifier import classify_intent_llm     #classify_intent 
from db import save_chat, get_history
import json


app = FastAPI(title="Subject Based Educational Bot")

class QueryRequest(BaseModel):
    query: str


@app.get("/")
def welcome():
    return {"message" : "Welcome to the EduBuddy"}


@app.post("/chat")
def chat(request: QueryRequest):
    query = request.query
    intent_json = classify_intent_llm(query)
    intent = intent_json['intent']
    # print(intent)
    if intent == "history":

        response = handle_history(query)

    elif intent == "maths":
        response = handle_maths(query)

    elif intent == "science":
        response = handle_science(query)

    else :
        response = handle_fallback(query)

    save_chat(query, json.dumps(intent), response)     
    return {"intent" : intent, "response" : response}


@app.get("/history")
def fetch_history():
    chats = get_history()
    return [{"query": q, "intent": i, "response": r} for q,i,r in chats]
