import json
import os
from dotenv import load_dotenv
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

class HelperTools():
    
    def __init__(self):
        self.CLASS_NAME = type(self).__name__
        load_dotenv()
        self.retrieved_secret = dict()
        self.kv_base_uri = "https://{0}.vault.azure.net"
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


    def get_secret(self, kv_env_name, env_secret_name):
        try:
            # Get api user key vault name. This user is the one who can interact with this api.
            kv_name_api_user = os.environ[kv_env_name]
            kv_uri = self.kv_base_uri.format(kv_name_api_user)
            
            # Create vault client to connect to the specific vault.
            credential = DefaultAzureCredential()
            client = SecretClient(vault_url = kv_uri, credential = credential)
            print("Vault connection - Success\n")
            
            # Retrieve the secret name
            secret_name = os.environ[env_secret_name]
            self.retrieved_secret = client.get_secret(secret_name)
            print(f"retrieved_secret.value={self.retrieved_secret.value}\n")
            
            print(f"get_secret -> success\n")
        except Exception as err:
            print(f"Error get_secret -> {err}\n")
            
    def is_valid_user_request(self, api_key_user):
        try:
            is_valid_user = True if api_key_user == self.retrieved_secret.value else False
            print(f"is_valid_user_request -> {is_valid_user}\n")
            return is_valid_user
        except Exception as err:
            print(f"Error is_valid_user_request -> {err}\n")
        
        
    def read_json_file(self, file_name: str):
        method_name = self.read_json_file.__name__

        try:
            data = dict()
            
            with open(file_name, 'r') as file:
                data = json.load(file)
                    
            return data
        except Exception as err:
            print(f"Error -> {self.CLASS_NAME} {method_name}: {err}")
            
        