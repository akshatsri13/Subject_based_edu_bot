from llm_setup import llm, PromptTemplate

science_prompt = PromptTemplate(
    template="You are a Science expert. Answer questions brief and clearly: \n {query}",
    input_variables=['query']
)

def handle_science(query: str):
    response = llm.invoke(science_prompt.format(query=query))
    return response.content.strip()