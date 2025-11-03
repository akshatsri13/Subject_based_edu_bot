from llm_setup import llm, maths_prompt

def handle_maths(query: str):
    prompt = maths_prompt.format(query=query)
    response = llm.invoke(prompt)
    return response.content.strip()