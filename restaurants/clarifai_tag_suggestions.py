import json
import requests

#TODO: CRIO_TASK_MODULE_TAG_SUGGESTION
# As part of this module you are expected to complete the get_tags_suggestions() function
# Tasks:
# 1) You need to register as Clarifai developer to obtain an API Key to the Food Model
#    The Food model can be found here:
#    https://www.clarifai.com/models/food-image-recognition-model-bd367be194cf45149e75f01d59f77ba7
#    A sample request and response can be found in the above link
# 2) Use the food model to get implement tag suggestions

# Parameters
# ----------
# api_key : string
#     API Key for Clarifai
# image_url : string
#     publicly accessible URL of the image to get tag suggestions
# Return Type: list()
#   return a list of tags provided by the Clarifai API
def get_tags_suggestions(api_key, image_url):
    # write your code here
    
    tags=[]
    url = "https://api.clarifai.com/v2/models/bd367be194cf45149e75f01d59f77ba7/outputs"

    payload = '\n    {\n      \"inputs\": [\n        {\n          \"data\": {\n            \"image\": {\n              \"url\": \"'+image_url+'\"\n            }\n          }\n        }\n      ]\n    }'
    headers = {
    'Authorization': 'Key a68f2781c12d4ce8a1e45962900a2d98',
    'Content-Type': 'application/json',
    'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    response = json.loads(response.text.encode('utf8'))
    response=extract_values(response,'name')
    if response[1]=='rice':
        tags=response[1:]
    else:
        tags=response[2:]
    return tags

def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

def get_access_token(token_name):
    file_handle = open('access_tokens.sh', 'r+')
    lines = file_handle.readlines()
    file_handle.close()
    for line in lines:
        tokens = line.strip().split('=')
        if tokens[0] == token_name:
            return tokens[1].strip()
    return 'Not found'

if __name__ == '__main__':
    clarify_api_key = get_access_token('973f61480445455e8e7f1dfbbf6e168b')
    test_image_url = 'https://i.imgur.com/dlMjqQe.jpg'
    tags_suggessted = get_tags_suggestions(clarify_api_key, test_image_url)
    print(tags_suggessted)
