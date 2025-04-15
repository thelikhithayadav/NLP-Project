from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionConfirmTrip(Action):
    def name(self) -> Text:
        return "action_confirm_trip"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        destination = tracker.get_slot("destination")
        date = tracker.get_slot("departure_date")

        if destination and date:
            dispatcher.utter_message(
                text=f"✅ Your trip to **{destination.title()}** on **{date}** has been confirmed. Bon voyage! 🌍✈️"
            )
        else:
            dispatcher.utter_message(
                text="I need both the destination and departure date to confirm your trip."
            )

        return []
