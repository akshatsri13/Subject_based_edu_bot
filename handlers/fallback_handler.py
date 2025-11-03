from llm_setup import llm, fallback_prompt

def handle_fallback(query: str):
    prompt = fallback_prompt.format(query=query)
    response = llm.invoke(prompt)
    return response.content.strip() 