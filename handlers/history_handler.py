from llm_setup import llm, history_prompt

def handle_history(query: str):
    prompt = history_prompt.format(query=query)
    response = llm.invoke(prompt)
    return response.content.strip()
