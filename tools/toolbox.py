import json

class HelperTools():
    
    def __init__(self):
        self.CLASS_NAME = type(self).__name__
        print("__init__")
    
    '''
    Create the request to send to chatgpt
    '''
    def generate_ai_prompt_msg(self, prompt_request, nbrOfResults, user_specs):
        recipe_placeholder = "recipe" if nbrOfResults == 1 else "recipes"
        request_msg = prompt_request.format(nbrOfResults, recipe_placeholder, user_specs["ingredients"].capitalize(), user_specs["allergies"].capitalize())
        print(f"generate_ai_prompt_msg={request_msg}\n")
        return request_msg

    '''
    Convert the json request received to string of ingredients, allergies, etc.
    This will be used to create the prompt request to chatgpt.
    '''
    def stringify_request(self, json_data_request, request_keys):
        try:
            user_specs = {}
            for key in request_keys:
                specification = json_data_request.get(key)
                user_specs[key] = ', '.join(s for s in specification)
                print(f"stringify_request -> success\n")
            return user_specs;
        except Exception as err:
            print(f"Error stringify_request -> {err}\n")
            
        
