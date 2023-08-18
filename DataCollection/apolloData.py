import requests
import os
import json

from entity.apolo_pojo import Apollo_Data
from utils.dbUtils.dbUtils import executeMany


APOLLO_KEY = os.environ.get('APOLLO_KEY')

check_health_url = "https://api.apollo.io/v1/auth/health"

headers = {
    "Content-Type": "application/json",
    "Cache-Control": "no-cache"
}
params = {
    "api_key": APOLLO_KEY
}

response = requests.get(check_health_url, headers=headers, params=params).json()

if response['healthy'] and response['is_logged_in']:
    people_search_url = "https://api.apollo.io/v1/people/search"
    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache"
    }
    
    pages = 10

    for page_no in range(1, pages+1):
        payload = {
            "api_key": APOLLO_KEY,
            "q_organization_domains": "apollo.io\ngoogle.com",
            "page": page_no,
            "person_titles": ["Data Engineer", "Engineering Manager"],
            "person_locations":["United States"],
            "q_organization_domains": "google\napple\nbigcommerce",
        }



        response = requests.post(people_search_url, headers=headers, data=json.dumps(payload))
        peopleList = response.json()['people']
        print(len(peopleList))
        apolo_list = []
        for people in peopleList:
            apolo_data = Apollo_Data(people)
            apolo_list.append(apolo_data)
        print(peopleList)
        executeMany(apolo_list)

else:
    print("Invalid API Key")