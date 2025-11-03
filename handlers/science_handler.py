from llm_setup import llm, science_prompt

def handle_science(query: str):
    prompt = science_prompt.format(query=query)
    response = llm.invoke(prompt)
    return response.content.strip()
   