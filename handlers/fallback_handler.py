from llm_setup import llm, PromptTemplate

# def handle_fallback(query: str):
#     prompt = fallback_prompt.format(query=query)
#     response = llm.invoke(prompt)
#     return response.content.strip() 



fallback_prompt = PromptTemplate(
    template=(
       """ **Description:**  
Handles any question that is **not related to Maths, Science, or History**.  
If the user asks something outside these subjects — such as personal questions, general knowledge, technology, entertainment, or any unrelated topic — this intent should trigger.  

When this intent is detected, the assistant should politely decline and guide the user back to supported topics.  
It should **not attempt to answer** non-educational questions.  

**Response Style:**  
Be polite, brief, and educational in tone.  
Clearly inform the user that you can only answer questions from Maths, Science, or History."""
        "User Query: {query}"
    ),
    input_variables=["query"]
)

def handle_fallback(query: str):
    response = llm.invoke(fallback_prompt.format(query=query))
    return response.content.strip()