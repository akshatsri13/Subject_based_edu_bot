from llm_setup import llm, PromptTemplate


history_prompt = PromptTemplate(
    template=(
        "You are a knowledgeable and helpful History expert. "
        "Answer questions clearly, briefly, and accurately. "
        "Only answer questions related to History — including ancient, medieval, and modern events, civilizations, and leaders. "
        "If the question is not related to History, politely respond that you can only answer History-related questions.\n\n"
        "User Query: {query}"
    ),
    input_variables=['query']
)

def handle_history(query: str):
    response = llm.invoke(history_prompt.format(query=query))
    return response.content.strip()