from openai import OpenAI
from flask import jsonify, request
from tools.toolbox import HelperTools
from dotenv import load_dotenv
import os
import json
tools=HelperTools()
load_dotenv()
request_keys = ['ingredients', 'allergies']
prompt_request = """Suggest {0} {1} with ingredients including {2}; 
                 considering that I'm allergic to {3}. Provide the results only in Json format."""
client = OpenAI(
  api_key=os.getenv("OPENAI_APIKEY_RECIPE") 
)
def getCompletion(prompt, model="gpt-3.5-turbo-1106"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
    )
  
    return json.loads(response.choices[0].message.content)

def getRecipe(nbrOfResults=1):
    # We will use a json format to send the transaction with all keys: ingredients and allergies.
    json_data_request = request.get_json()
    
    user_specs = tools.stringify_request(json_data_request, request_keys)
    
    # Format prompt request to send to chatgpt
    user_request = tools.generate_ai_prompt_msg(prompt_request, nbrOfResults, user_specs)
    response=getCompletion(user_request)
    print(response)
    return {"message":response}
