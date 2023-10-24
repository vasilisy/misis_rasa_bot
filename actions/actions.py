from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import sqlite3


class ActionSetPaid(Action):
    def name(self):
        return "action_set_paid"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        return [SlotSet("ONLY_BUDGET", False)]


class ActionSetBudget(Action):
    def name(self):
        return "action_set_budget"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        return [SlotSet("ONLY_BUDGET", True)]


class ActionRecommendations(Action):
    def name(self):
        return "action_find_recommendations"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        # подключаемся к бд
        connection = sqlite3.connect('misis.db')
        cursor = connection.cursor()

        # get slots and save as tuple
        info_score = tracker.get_slot("SCORE")
        info_subject = tracker.get_slot("SUBJECT")
        info_budget = tracker.get_slot("ONLY_BUDGET")

        if info_budget:
            cursor.execute("SELECT name FROM specializations JOIN subjects "
                           "ON specializations.id = subjects.id WHERE specializations.min_score_budget < (?) "
                           "AND subjects.subjects1 IN (?, ?, ?) AND subjects.subjects2 IN (?, ?, ?) AND subjects.subjects3 IN (?, ?, ?)",
                           (int(info_score), *info_subject, *info_subject, *info_subject))
        else:
            cursor.execute("SELECT name FROM specializations JOIN subjects "
                           "ON specializations.id = subjects.id WHERE specializations.min_score_platka < (?) "
                           "AND subjects.subjects1 IN (?, ?, ?) AND subjects.subjects2 IN (?, ?, ?) AND subjects.subjects3 IN (?, ?, ?)",
                           (int(info_score), *info_subject, *info_subject, *info_subject))

        # retrieve sqlite row
        data_raw = cursor.fetchall()

        if data_raw:
            # convert tuple to list
            data_list = list(data_raw)
            response = '\n'
            for row in data_raw:
                response += row[0]
                response += '\n'
            response += 'Если вас заинтересовало какое-то направление, то напишите его код.'
            # ответ если направления нашлись. 5 индекс отвечает за responses
            connection.close()
            return [SlotSet("RESULT", response)]
        else:
            # подходящих направлений не нашлось
            dispatcher.utter_message(response="utter_deny")
            connection.close()
            return [SlotSet("RESULT", '')]


class ActionDescription(Action):
    def name(self):
        return "action_give_description"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        # подключаемся к бд
        connection = sqlite3.connect('misis.db')
        cursor = connection.cursor()

        # get slots and save as tuple
        info_specialization = tracker.get_slot("SPECIALITY")

        cursor.execute("SELECT description FROM specializations_description JOIN specializations "
                       "ON specializations.id = specializations_description.id WHERE specializations.name LIKE ?",
                       (str(info_specialization) + '%',))

        # retrieve sqlite row
        data_raw = cursor.fetchall()
        data_list = list(data_raw)
        response = data_list[0][0]

        if data_raw:
            connection.close()
            return [SlotSet("DESCRIPTION", response)]
        else:
            connection.close()
            return [SlotSet("DESCRIPTION", 'Направления с данным кодом нет в МИСИС.')]


class ActionPersonalInfoName(Action):
    def name(self):
        return "action_personal_info_name"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        name = tracker.latest_message.get('text')
        return [SlotSet("NAME", name)]


class ActionPersonalInfoNumber(Action):
    def name(self):
        return "action_personal_info_phone"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        phone = tracker.latest_message.get('text')
        return [SlotSet("PHONE", phone)]
