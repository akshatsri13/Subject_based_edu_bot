from llm_setup import llm, PromptTemplate

# def handle_history(query: str):
#     prompt = history_prompt.format(query=query)
#     response = llm.invoke(prompt)
#     return response.content.strip()
  

history_prompt = PromptTemplate(
    template="You are a history expert. Answer questions brief and clearly: \n {query}",
    input_variables=['query']
)

def handle_history(query: str):
    response = llm.invoke(history_prompt.format(query=query))
    return response.content.strip()