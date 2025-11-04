from llm_setup import llm, PromptTemplate

maths_prompt = PromptTemplate(
    template="You are a Science expert. Answer questions brief and clearly: \n {query}",
    input_variables=['query']
)

def handle_maths(query: str):
    response = llm.invoke(maths_prompt.format(query=query))
    return response.content.strip()