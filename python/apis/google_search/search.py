import json

import requests


# set up the request parameters
def search(query):
    params = {
      'api_key': 'BE0F5DB119CE4C19825D5C2DC33527DC',
      'q': query,
      'include_answer_box': 'true',
      'gl': 'us',
      'hl': 'en'

    }
    # make the http GET request to Scale SERP
    api_result = requests.get('https://api.scaleserp.com/search', params)
    # print the JSON response from Scale SERP
    return(json.dumps(api_result.json()))


def search_description(query):
    try:
        description = search(query=query)["knowledge_graph"]["description"]
        if description != None:
            return description
        else:
            return None
    except:
        return None

