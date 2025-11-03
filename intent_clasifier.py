# def classify_intent(query: str):
#     query = query.lower()

#     history_keywords = {
#     "ancient", "medieval", "modern", "war", "empire", "civilization", "dynasty",
#     "revolution", "independence", "treaty", "battle", "kingdom", "emperor",
#     "colonization", "constitution", "archaeology", "artifact", "timeline",
#     "industrial", "renaissance", "freedom", "monarchy", "conquest", "nationalism",
#     "roman", "greek", "british", "indian independence", "world war",
#     "historical event", "mughal", "ottoman", "democracy", "artifact", "excavation","chapter", "topic", "question", "explain", "describe"
#     }


#     science_keywords = {
#     "physics", "chemistry", "biology", "experiment", "energy", "atom", "molecule",
#     "reaction", "photosynthesis", "cell", "organ", "force", "motion", "gravity",
#     "electricity", "magnetism", "planet", "universe", "ecosystem", "genetics",
#     "dna", "evolution", "element", "compound", "acid", "base", "nucleus", "neuron",
#     "reproduction", "respiration", "matter", "light", "sound", "pressure", "speed",
#     "temperature", "mass", "friction", "chemical equation"
# }

#     maths_keywords = {
#     "algebra", "geometry", "trigonometry", "calculus", "statistics", "probability",
#     "number", "equation", "formula", "function", "integration", "differentiation",
#     "matrix", "vector", "ratio", "percentage", "mean", "median", "mode", "average",
#     "perimeter", "area", "volume", "factor", "multiple", "prime", "square root",
#     "logarithm", "theorem", "proof", "graph", "coordinate", "angle", "triangle",
#     "circle", "parabola", "limit", "derivative", "polynomial", "arithmetic",
#     "sequence", "series"
# }
    
#     if any(word in query for word in "history_keywords"):
#         return "history"
    
#     elif any(word in query for word in "science_keywords"):
#         return "science"
    
#     elif any(word in query for word in "maths_keywords"):
#         return "maths"
    

#     else:
#         return "fallback"
    

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
   Categorize the user's query into one of these catgories:
   - history
   - science
   - maths
   - fallback
   Just reply with the category name only
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
    print(intent_temp)
    response = llm.invoke(intent_temp)
    return response.content.strip()