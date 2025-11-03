from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite",
    temperature=0.7,
    api_key=os.environ["GEMINI_API_KEY"]

)

intent_prompt = PromptTemplate(
    template="""
   You are an intelligent educational assistant designed to classify a user's question
into a specific academic subject category.

Your goal is to determine which of the following categories best fits the user’s query:

1. **history**  
   - Includes: historical events, timelines, civilizations, empires, wars, leaders, revolutions, ancient cultures, and any inquiry related to the study of the past.  
   - Example Queries:
       - "Who was the ruler of the Mughal Empire in the 16th century?"
       - "When did World War II end?"
       - "Tell me about the French Revolution."
   - Counterexamples (not history):
       - "Explain Newton’s laws of motion." → science  
       - "Solve 3x + 2 = 11." → maths

2. **science**  
   - Includes: questions about physical, biological, or chemical principles; scientific processes, inventions, discoveries, and technology-related natural science topics.  
   - Example Queries:
       - "What is the chemical formula of water?"
       - "Explain photosynthesis."
       - "Why do objects fall to the ground?"
   - Counterexamples:
       - "When did Einstein publish the theory of relativity?" → history  
       - "What is 5% of 200?" → maths

3. **maths**  
   - Includes: arithmetic, algebra, geometry, trigonometry, calculus, statistics, or any problem requiring numeric reasoning or mathematical operations.  
   - Example Queries:
       - "Find the area of a triangle with base 10 and height 5."
       - "What is 12 divided by 3?"
       - "Simplify the expression (2x + 3)(x - 4)."
   - Counterexamples:
       - "Who invented algebra?" → history  
       - "What is the speed of light?" → science

4. **fallback**  
   - Use this category for queries that:
       - Are conversational or general (e.g., greetings, jokes, opinions).
       - Are unrelated to the academic subjects listed above.
       - Contain multiple subjects or unclear intent.
   - Example Queries:
       - "How are you?"
       - "Tell me a fun fact."
       - "Write a story about a student."
       - "Compare Newton and Pythagoras." (Ambiguous → fallback)

**Important Instructions:**
- Reply **only** with the single category name: `history`, `science`, `maths`, or `fallback`.  
- Do **not** include explanations, punctuation, or additional words.  
- If the question overlaps multiple categories, choose the one that best matches the **primary educational intent**.  
- If you are uncertain, default to `fallback`.

---

User query: {query}

Your response (only one of: history / science / maths / fallback):
"""
)

def classify_intent_llm(query: str):
    intent_temp =f'''
    Categorize the user's query into one of these catgories:
   - history
   - science
   - maths
   - fallback
   Just reply with the category name only
   \n
   User query: {query}
    '''
    # prompt = intent_prompt.format(query=intent_temp)
    # print(intent_temp)
    response = llm.invoke(intent_temp)
    return response.content.strip()