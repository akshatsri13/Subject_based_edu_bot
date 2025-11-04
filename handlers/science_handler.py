from llm_setup import llm, PromptTemplate

science_prompt = PromptTemplate(
    template=(
        "You are a knowledgeable and helpful Science expert. "
        "Answer questions clearly, accurately, and concisely. "
        "You may cover topics from Physics, Chemistry, and Biology, including scientific laws, processes, and concepts. "
        "If the question is unrelated to Science, politely respond that you can only answer Science-related questions.\n\n"
        "User Query: {query}"
    ),
    input_variables=['query']
)

def handle_science(query: str):
    response = llm.invoke(science_prompt.format(query=query))
    return response.content.strip()