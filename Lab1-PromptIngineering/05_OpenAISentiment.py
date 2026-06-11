import json

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(override=True)

system_message = """
Effectuez une analyse de sentiments basee sur les aspects des avis concernant
les ordinateurs portables presentes en entree.

Chaque avis peut comporter un ou plusieurs des aspects suivants : screen,
keyboard et pad.

Pour chaque avis presente en entree :
- Identifiez la presence d'au moins un des trois aspects.
- Attribuez une polarite de sentiment (positive, negative ou neutral)
  a chaque aspect.
- Organisez votre reponse dans un objet JSON avec les cles suivantes :
  - category : liste des aspects
  - polarity : liste des polarites correspondantes
- Si l'un des aspects n'est pas present dans l'avis, supposez que sa
  polarite est neutral.
"""

model = "gpt-5.2"

llm = ChatOpenAI(
    model=model,
    temperature=0,
    model_kwargs={"response_format": {"type": "json_object"}},
)

response = llm.invoke(
    [
        {"role": "system", "content": system_message},
        {"role": "user", "content": "L'écran est très bon, mais je n'ai pas aimé la souris. le clavier Ma fih Maytchaf"}
    ]
)

json_response = response.content
print(json_response)

result = json.loads(json_response)

print("\n")
print("Parsed JSON:", result)
print("First polarity:", result["polarity"][0])