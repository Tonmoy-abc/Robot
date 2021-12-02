import json
import os

import requests

cdir = os.path.abspath('python\\apis\\google_search\\')
# set up the request parameters
def search(query):
    params = {
      'api_key': 'BE0F5DB119CE4C19825D5C2DC33527DC',
      'q': query,
      'include_answer_box': 'true',
      'gl': 'bd',
      'hl': 'en'

    }
    # make the http GET request to Scale SERP
    api_result = requests.get('https://api.scaleserp.com/search', params)
    # save data to data.json
    with open(cdir+"\\data.json", 'w') as f:
        json.dump(api_result.json(), f)
    # return data.json
    with open(cdir+"\\data.json", encoding='utf8') as f:
        data = json.load(f)
        return data

def search_description(query):
    try:
        description = search(query=query)["knowledge_graph"]["description"]
        if description != None:
            return description
        else:
            return None
    except:
        return None
