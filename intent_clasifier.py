from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
import json
from llm_setup import llm ,intent_prompt

load_dotenv()



system_prompt = """
  **System Prompt:**

You are an intelligent intent classification model for an educational chatbot.  
Your goal is to classify the user’s question into one of the following **main intents**:  
`maths`, `science`, `history`, or `fallback`.  

Use the context, examples, and descriptions below to decide the correct intent.

---

### 📘 INTENT DEFINITIONS

#### 🧮 1. Maths
**Description:** Handles all mathematical topics, calculations, and conceptual explanations.  

**Examples:**
- Solve 2x + 3 = 7  
- What is sin(90°)?  
- Find the mean of 10, 20, and 30  
- Explain the area of a triangle  
- What is integration?  

---

#### 🔬 2. Science
**Description:** Covers all scientific domains — physics, chemistry, and biology.  

**Examples:**
- What is Newton's first law of motion?  
- What is an atom?  
- Explain photosynthesis  
- What is DNA?  
- What are acids and bases?  

---

#### 🏛️ 3. History
**Description:** Handles questions about past events, civilizations, wars, empires, and famous people.  

**Examples:**
- When did World War I begin
- When did World War II begin?  
- Who was Ashoka the Great?  
- What is the Indus Valley Civilization?  
- Explain the Mughal Empire  
- Who was Mahatma Gandhi?  

---

#### 💬 4. Fallback  
**Description:**  
Handles any question that is **not related to Maths, Science, or History**.  
If the user asks something outside these subjects — such as personal questions, general knowledge, technology, entertainment, or any unrelated topic — this intent should trigger.  

When this intent is detected, the assistant should politely decline and guide the user back to supported topics.  
It should **not attempt to answer** non-educational questions.  

**Response Style:**  
Be polite, brief, and educational in tone.  

---

### 🧠 INSTRUCTION

Analyze the user’s query and return your result **strictly in JSON format**:


{
  "intent": "<main_intent_name>"
}

"""

def classify_intent_llm(query: str):
    """
    Classify user query into intent, and confidence.
    """

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-lite",
        temperature=0.7,
        api_key=os.environ["GEMINI_API_KEY"]
    )

    intent_prompt = PromptTemplate(
        input_variables=["system_prompt", "user_query"],
        template="""
{system_prompt}

Now analyze the following user query and respond only in JSON format.

User Query: "{user_query}"
"""
    )

    final_prompt = intent_prompt.format(
        system_prompt=system_prompt, 
        user_query=query
    )

    response = llm.invoke(final_prompt)
    raw_output = response.content.strip()
    print(raw_output)

    if raw_output.startswith("```"):
        raw_output = raw_output.strip("`").replace("json", "").strip()

    result = json.loads(raw_output)
    return result
    