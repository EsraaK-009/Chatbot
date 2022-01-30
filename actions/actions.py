import json
from pathlib import Path
from typing import Any, Text, Dict, List

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from actions.country import check_country

class ActionCapital(Action):

    def name(self) -> Text:
        return "action_ask_capital"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        client_cap = "https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCapital"
        #print(tracker.latest_message)
        if len(tracker.latest_message['entities'])>0:
           for blob in tracker.latest_message['entities']:
              if blob['entity'] == 'country_name':
                country_value = blob['value']
                is_country, country = check_country(country_value)
                if is_country:
                    response = requests.post(client_cap, json ={'country':country})
                    if response.json()['success']==1:
                         capital = response.json()['body']['capital']
                         dispatcher.utter_message(text=f"The Capital of {country} is {capital}. Tell me if you want to know more.")
                         		
                    else:
                         dispatcher.utter_message(text=f"Very sorry, there's a problem right now :(")
                break
        else:
           dispatcher.utter_message(text=f"I can't find the country you wanted. Please write it again")
        return []
      
class ActionPopulation(Action):

    def name(self) -> Text:
        return "action_ask_population"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        client_pop = "https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getPopulation"
        if len(tracker.latest_message['entities'])>0:
           for blob in tracker.latest_message['entities']:
              if blob['entity'] == 'country_name':
                country_value = blob['value']
                is_country, country = check_country(country_value)
                if is_country:
                    response = requests.post(client_pop, json ={'country':country})
                    if response.json()['success']==1:
                         population = response.json()['body']['population']
                         dispatcher.utter_message(text=f"There are {population} person in {country}. Tell me if you want to know more.")  		
                    else:
                         dispatcher.utter_message(text=f"Very sorry, there's a problem right now :(")
                break
        else:
           dispatcher.utter_message(text=f"I can't find the country you wanted. Please write it again")
        return []
