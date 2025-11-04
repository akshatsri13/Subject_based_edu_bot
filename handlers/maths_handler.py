from llm_setup import llm, PromptTemplate


maths_prompt = PromptTemplate(
    template=(
        "You are a Maths expert. "
        "Answer the user's question clearly and concisely. "
        "Show steps only if necessary.\n\n"
        "User Query: {query}"
    ),
    input_variables=['query']
)
def handle_maths(query: str):
    response = llm.invoke(maths_prompt.format(query=query))
    return response.content.strip()