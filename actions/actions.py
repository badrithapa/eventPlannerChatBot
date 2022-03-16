# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet
# from rasa_sdk.events import EventType
from rasa_sdk.events import AllSlotsReset

from db_mysql import insert_data
import mysql.connector
class AskForOcassionAction(Action):

    def name(self) -> Text:
        return "action_ask_ocassion_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="May I ask the ocassion you're celebrating?")

        return []

class AskForGuestAction(Action):
    def name(self) -> Text:
        return "action_ask_guest_slot"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="May I ask the number of guests?")

        return []

class AskForTimeAction(Action):
    def name(self) -> Text:
        return "action_ask_time_slot"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="May I ask the time you're celebrating?")

        return []

class SetToDB(Action):
    def name(self) -> Text:
        return "action_submit"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ocassion = tracker.get_slot("ocassion_slot")
        guest = tracker.get_slot("guest_slot")
        time = tracker.get_slot("time_slot")
        dispatcher.utter_message(text="Great! I will remember that you're celebrating {} at {} with {} guests.".format(ocassion, time, guest))
        insert_data(ocassion, guest, time)
        return []

class ResetSlots(Action):
    def name(self) -> Text:
        return "action_reset_slots"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # dispatcher.utter_message(text="Okay, I will forget everything I remembered.")
        return [AllSlotsReset()]