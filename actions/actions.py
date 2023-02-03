# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
## This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
#
#

# This files contains your custom actions which can be used to run

# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import requests
from rasa_sdk import Tracker,Action
from rasa_sdk.executor import CollectingDispatcher
import json
from datetime import datetime
import datetime
from tkinter import EventType
from typing import Any, Text, Dict, List, Union
import calendar


# def last_day_of_month(any_day):
#     # The day 28 exists in every month. 4 days later, it's always next month
#     next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
#     # subtracting the number of the current day brings us back one month
#     return next_month - datetime.timedelta(days=next_month.day)
# def last_day_of_month(any_day):
#     if any_day.month == 1:
#         year = any_day.year - 1
#         month = 12
#     else:
#         year = any_day.year
#         month = any_day.month - 1
#
#     # The day 28 exists in every month. 4 days later, it's always next month
#     next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
#     # subtracting the number of the current day brings us back one month
#     return next_month - datetime.timedelta(days=next_month.day)

def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1
class Action_Revenue(Action):
    def name(self) -> Text:
        return "action_Revenue"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons=[
            {"payload": "Revenue Report", "title": "Revenue Report"},
            {"payload": "Admission", "title": "Admission"}
        ]
        dispatcher.utter_message("Please select option from below", buttons=buttons)
        return []
class Action_Service(Action):
    def name(self) -> Text:
        return "action_revenue"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons=[
            {"payload": "Revenue Report", "title": "Revenue Report"},
            {"payload": "Admission", "title": "Admission"}
        ]
        dispatcher.utter_message("Please select option from below", buttons=buttons)
        return []
class Action_Revenue_sub(Action):
    def name(self) -> Text:
        return "action_Revenue_sub"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons=[
            {"payload": "Cluster_Revenue", "title": "Cluster"},
            {"payload": "Center_Revenue", "title": "Center"},
            {"payload": "Total_Revenue", "title": "Total"}
        ]
        dispatcher.utter_message("Choose an option from below.",buttons=buttons)
        return []
class ActionclusterSlot(Action):
    def name(self) -> Text:
        return "action_Cluster"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        buttons=[
            {"payload": "Madhapur_Revenue", "title": "Madhapur"},
            {"payload": "Andhra pradesh_Revenue", "title": "Andhra Pradesh"},
            {"payload": "vizag_Revenue", "title": "Vizag"},
            {"payload": "ROTA_Revenue", "title": "ROTA"},
            {"payload": "Maharastra_Revenue", "title": "Maharastra"}
        ]
        dispatcher.utter_message("Which Cluster you are looking for",buttons=buttons)
        return []
class ActionMadhapur(Action):
    def name(self) -> Text:
        return "action_madhapur_cluster"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        buttons=[
            {"payload": "Madh_Rev", "title": "Madhapur"},
            {"payload": "Madhapur - OPD_Rev", "title": "Madhapur - OPD"},
            {"payload": "MOI - Hitech_Rev", "title": "MOI - Hitech"},
            {"payload": "suyosha_Rev", "title": "Suyosha"},
            {"payload": "Chandanagar_Rev", "title": "Chandanagar"}
        ]
        dispatcher.utter_message("Madhapur Cluster",buttons=buttons)
        return []
class ActionTimeMADHAPUR(Action):
    def name(self) -> Text:
        return "action_Madhapur_cluster_time"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        u = tracker.get_slot("Madhapur_Revenue_unit1")
        k=u.replace("_Rev","")
        print(k)
        buttons=[
            {"payload": "what is the revenue for "+k+" today", "title": "Today"},
            {"payload": "what is the revenue for "+k+" yesterday", "title": "yesterday"},
            {"payload": "what is the revenue for "+k+" last month", "title": "MTD"}
        ]
        dispatcher.utter_message("Please select a Time Period",buttons=buttons)
        return []
class ActionUnitWise_Madh(Action):
    def name(self) -> Text:
        return "action_Madhunit"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        Madh_unit = tracker.get_slot("unit_Madh")
        print(Madh_unit)
        Madh= Madh_unit.replace(Madh_unit, "Madhapur")
        for d in data:
            if d["branch"] == Madh:
                message=dispatcher.utter_message("Hey,Here are the results"+"\nLocation: "+d["branch"]+ ",\nTarget: " + str(d["target"])+ ",\nAchieved: "+str(d["achieved"])+",\nLast Month Achieved: "+str(d["asondate"])+",\nAchieved Percentage: "+str(d["achievedpercentage"]))
                return []
class ActionGroup(Action):
    def name(self) -> Text:
        return "action_back"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        buttons=[
            {"payload": "Go To Menu", "title": "Go To Menu"},
            {"payload": "Exit", "title": "Exit"}
        ]
        dispatcher.utter_message(buttons=buttons)
        return []
class ActionUnitWise_Madopd(Action):
    def name(self) -> Text:
        return "action_Unit_MadOPD"
    def run(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        madh = tracker.get_slot("Unit_MAdhOPD")
        print(madh)
        M = madh.replace(madh, "Madhapur - OPD")
        for d in data:
            if d["branch"] == M:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + str(d["target"])+ ",\nAchieved: "+str(d["achieved"])+",\nAchieved Percentage: "+str(d["achievedpercentage"])+",\nLast Month Achieved: "+str(d["asondate"]))
                return []
class ActionUnit(Action):
    def name(self) -> Text:
        return "action_units"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        units = tracker.get_slot("units")
        print(units)
        unit=''
        try:
            unit=units[0].upper()+units[1:]
        except:
            print(dispatcher.utter_message("Please enter the correct unit name and the month and year for unit"))

        for d in data:
            if d["branch"] == unit:
                message=dispatcher.utter_message("Hey ,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + str(d["target"])+ ",\nAchieved: "+str(d["achieved"])+",\nAchieved Percentage: "+str(d["achievedpercentage"])+",\nLast Month Achieved: "+str(d["asondate"]))
                return []
class ActionUnitWiseMOI(Action):
    def name(self) -> Text:
        return "action_Unit_MOIhitech"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        hite = tracker.get_slot("Unit_Hite")
        print(hite)
        MOIH= hite.replace(hite, "MOI - Hitech")
        for d in data:
            if d["branch"] == MOIH :
                message=dispatcher.utter_message("Hey ,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + str(d["target"])+ ",\nAchieved: "+str(d["achieved"])+",\nAchieved Percentage: "+str(d["achievedpercentage"])+",\nLast Month Achieved: "+str(d["asondate"]))
                return []


class Actionandhracluster(Action):
    def name(self) -> Text:
        return "action_andhra_cluster"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict) -> List[EventType]:
        buttons = [
            {"payload": "Nellore_Revenue", "title": "Nellore"},
            {"payload": "Nellore Oncology_Revenue", "title": "NelloreOncology"},
            {"payload": "Kurnool_Revenue", "title": "Kurnool"}
        ]
        message=dispatcher.utter_message("Andhra cluster",buttons=buttons)
        return []
class ActionTimeANDHRA(Action):
    def name(self) -> Text:
        return "action_Andhra_cluster_time"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        u = tracker.get_slot("Andhra_Pradesh_Revenue_unit1")
        k=u.replace("_Revenue","")
        print(k)
        buttons=[
            {"payload": "what is the revenue for "+k+" today", "title": "Today"},
            {"payload": "what is the revenue for "+k+" yesterday", "title": "yesterday"},
            {"payload": "what is the revenue for "+k+" last month", "title": "MTD"}
        ]
        dispatcher.utter_message("Please select a Time Period",buttons=buttons)
        return []
class ActionUnitNellore(Action):
    def name(self) -> Text:
        return "action_Nellore"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        Nellore = tracker.get_slot("nellore_Unit")
        Nellore_unit= Nellore.replace(Nellore,"Nellore")
        for d in data:
            if d["branch"] == Nellore_unit:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + str(d["target"])+ ",\nAchieved: "+str(d["achieved"])+",\nAchieved Percentage: "+str(d["achievedpercentage"])+",\nLast Month Achieved: "+str(d["asondate"]))
                return []
class ActionNelloreOncology(Action):
    def name(self):
        return "action_Nellore_oncology"
    def run(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        # date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        Nellore = tracker.get_slot("Nellore_Oncology_unit")
        Nellore_health = Nellore.replace(Nellore, "Nellore Oncology")
        for d in data:
            if d["branch"] == Nellore_health:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + str(d["target"])+ ",\nAchieved: "+str(d["achieved"])+",\nLast Month Achieved: "+str(d["asondate"])+",\nAchieved Percentage: "+str(d["achievedpercentage"]))
                return []

class Actionvizagcluster(Action):
    def name(self) -> Text:
        return "action_vizag_cluster"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        buttons=[
            {"payload": "Vizianagaram_Rev", "title": "Vizianagaram"},
            {"payload": "Srikakulam_Rev", "title": "Srikakulam"},
            {"payload": "Vizag MVP_Rev", "title": "Vizag MVP"},
            {"payload": "W&C_Rev", "title": "Vizag W&C"}
        ]
        dispatcher.utter_message("Vizag Cluster",buttons=buttons)
        return []
class ActionTimeVizag(Action):
    def name(self) -> Text:
        return "action_Vizag_cluster_time"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        u = tracker.get_slot("vizag_Revenue_unit1")
        k= u.replace("_Rev","")
        print(k)
        buttons=[
            {"payload": "what is the revenue for "+k+" today", "title": "Today"},
            {"payload": "what is the revenue for "+k+" yesterday", "title": "yesterday"},
            {"payload": "what is the revenue for "+k+" last month", "title": "MTD"}
        ]
        dispatcher.utter_message("Please select a Time Period",buttons=buttons)
        return []
class ActionUnitWandC(Action):
    def name(self) -> Text:
        return "action_Unit_W&C"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        viz = tracker.get_slot("W&C_unit")
        Viz0_WC= viz.replace(viz, "Vizag W&C")
        for d in data:
            if d["branch"] == Viz0_WC :
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + str(d["target"])+ ",\nAchieved: "+str(d["achieved"])+",\nAchieved Percentage: "+str(d["achievedpercentage"])+",\nLast Month Achieved: "+str(d["asondate"]))
                return []
class ActionUnitMVP(Action):
    def name(self) -> Text:
        return "action_Unit_MVP"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        MVP = tracker.get_slot("MVP_Unit")
        print(MVP)
        VMVP= MVP.replace(MVP, "Vizag MVP")
        for d in data:
            if d["branch"] == VMVP:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + str(d["target"])+ ",\nAchieved: "+str(d["achieved"])+",\nAchieved Percentage: "+str(d["achievedpercentage"])+",\nLast Month Achieved: "+str(d["asondate"]))
                return []
class ActionROTA(Action):
    def name(self) -> Text:
        return "action_rota_cluster"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        buttons=[
            {"payload": "Karimnagar_Rev", "title": "Karimnagar"},
            {"payload": "Nizamabad_Rev", "title": "Nizamabad"},
            {"payload": "Kakinada_Rev", "title": "Kakinada"},
            {"payload": "Sangareddy_Rev", "title": "Sangareddy"},
            {"payload": "Begumpet_Rev", "title": "Begumpet"},
            {"payload": "Zaheerabad_Rev", "title": "Zaheerabad"}
        ]
        dispatcher.utter_message("ROTA Cluster",buttons=buttons)
        return []
class ActionTimeROTA(Action):
    def name(self) -> Text:
        return "action_ROTA_cluster_time"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        u = tracker.get_slot("ROTA_Revenue_unit1")
        k= u.replace("_Rev","")
        print(k)
        buttons=[
            {"payload": "what is the revenue for "+k+" today", "title": "Today"},
            {"payload": "what is the revenue for "+k+" yesterday", "title": "yesterday"},
            {"payload": "what is the revenue for "+k+" last month", "title": "MTD"}
        ]
        dispatcher.utter_message("Please select a Time Period",buttons=buttons)
        return []
class ActionMH(Action):
    def name(self) -> Text:
        return "action_mh_cluster"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        buttons=[
            {"payload": "Nashik_Rev", "title": "Nashik"},
            {"payload": "Aurangabad_Rev", "title": "Aurangabad"},
            {"payload": "Sangamner_Rev", "title": "Sangamner"},
            {"payload": "Navimumbai_Rev", "title": "Navimumbai"}
        ]
        dispatcher.utter_message("Maharastra Cluster",buttons=buttons)
        return []
class ActionTimeMH(Action):
    def name(self) -> Text:
        return "action_MH_cluster_time"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        u = tracker.get_slot("MH_Revenue_unit1")
        k= u.replace("_Rev","")
        print(k)
        buttons=[
            {"payload": "what is the revenue for "+k+" today", "title": "Today"},
            {"payload": "what is the revenue for "+k+" yesterday", "title": "yesterday"},
            {"payload": "what is the revenue for "+k+" last month", "title": "MTD"}
        ]
        dispatcher.utter_message("Please select a Time Period",buttons=buttons)
        return []
class Action_centres(Action):
    def name(self) -> Text:
        return "action_center"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        j=["Nizamabad_center", "Chandanagar_center", "Karimnagar_center", "Sangareddy_center", "Zaheerabad_center", "Srikakulam_center" , "Kurnool_center", "Vizianagaram_center", "Kakinada_center", "Aurangabad_center", "Nashik_center", "Sangamner_center", "Begumpet_center", "Navimumbai_center", "Nellore_center", "Nellore Oncology_center", "madhapur - OPD_center", "MOI  Hitech_center", "Madh_center", "MWC_center", "MVP_center", "W&C_center"]
        buttons=[
            {"payload": j[0], "title": "Nizamabad"},
            {"payload": j[1], "title": "Chandanagar"},
            {"payload": j[2], "title": "Karimnagar"},
            {"payload": j[3], "title": "Sangareddy"},
            {"payload": j[4], "title": "Zaheerabad"},
            {"payload": j[5], "title": "Srikakulam"},
            {"payload": j[6], "title": "Kurnool"},
            {"payload": j[7], "title": "Vizianagaram"},
            {"payload": j[8], "title": "Kakinada"},
            {"payload": j[9], "title": "Aurangabad"},
            {"payload": j[10], "title": "Nashik"},
            {"payload": j[11], "title": "Sangamner"},
            {"payload": j[12], "title": "Begumpet"},
            {"payload": j[13], "title": "Navimumbai"},
            {"payload": j[14], "title": "Nellore"},
            {"payload": j[15], "title": "Nellore Oncology"},
            {"payload": j[16], "title": "Madhapur - OPD"},
            {"payload": j[17], "title": "MOI  Hitech"},
            {"payload": j[18], "title": "Madhapur"},
            {"payload": j[19], "title": "MWC Hitech"},
            {"payload": j[20], "title": "Vizag MVP"},
            {"payload": j[21], "title": "Vizag W&C"}
        ]
        dispatcher.utter_message("Revenue Center",buttons=buttons)
        return []
class ActionTimeCenter(Action):
    def name(self) -> Text:
        return "action_Center_sub_time"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        u = tracker.get_slot("Center_sub_unit1")
        k= u.replace("_center","")
        print(k)
        buttons=[
            {"payload": "what is the revenue for "+k+" today", "title": "Today"},
            {"payload": "what is the revenue for "+k+" yesterday", "title": "yesterday"},
            {"payload": "what is the revenue for "+k+" last month", "title": "MTD"}
        ]
        dispatcher.utter_message("Please select a Time Period",buttons=buttons)
        return []
class ActionUnitWiseMWC(Action):
    def name(self) -> Text:
        return "action_Unit_MWC"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        hite = tracker.get_slot("MWC_unit")
        print(hite)
        H=hite.replace(hite, "MWC Hitech")
        for d in data:
            if d["branch"] == H :
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + str(d["target"])+ ",\nAchieved: "+str(d["achieved"])+",\nAchieved Percentage: "+str(d["achievedpercentage"])+",\nLast Month Achieved: "+str(d["asondate"]))
                return []
class ActionTimeTotal(Action):
    def name(self) -> Text:
        return "action_Total"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        u = tracker.get_slot("Group")
        k= u.replace("_Revenue","")
        print(k)
        buttons=[
            {"payload": "what is the revenue for "+k+" today", "title": "Today"},
            {"payload": "what is the revenue for "+k+" yesterday", "title": "yesterday"},
            {"payload": "what is the revenue for "+k+" last month", "title": "MTD"}
        ]
        dispatcher.utter_message("Please select a Time Period",buttons=buttons)
        return []
class ActionUnitTargets(Action):
    def name(self) -> Text:
        return "action_Group"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        unit = tracker.get_slot("Grand_Total")
        print(unit)
        units = unit.replace(unit, "Total")
        for d in data:
            if d["branch"] == units:
                message = dispatcher.utter_message("Hey,Here are the results " + "\nLocation: " + d["branch"] + ",\nTarget: " + str(d["target"]) + ",\nAchieved: " + str(d["achieved"]) + ",\nAchieved Percentage: " + str(d["achievedpercentage"]) + ",\nLast Month Achieved: " + str(d["asondate"]))
                return []
class ActionUnitsMonth(Action):
    def name(self) -> Text:
        return "action_units_month"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        datestr = datetime.datetime.strptime(date1, "%Y-%m-%d")
        print(datestr)
        year = datestr.year
        month = datestr.month
        last_day = calendar.monthrange(year, month)[1]
        final_date = datetime.date(year, month, last_day)
        print(final_date)
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": str(final_date)}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        units = tracker.get_slot("units")
        print(units)
        unit=''
        try:
            unit=units[0].upper()+units[1:]
        except:
            print(dispatcher.utter_message("Please enter the correct unit name and the month and year for unit"))

        for d in data:
            if d["branch"] == unit:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + str(d["target"])+ ",\nAchieved: "+str(d["achieved"])+",\nAchieved Percentage: "+str(d["achievedpercentage"])+",\nLast Month Achieved: "+str(d["asondate"]))
                return []
class ActionUnitNelloreMonth(Action):
    def name(self) -> Text:
        return "action_Nellore_month"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        datestr = datetime.datetime.strptime(date1, "%Y-%m-%d")
        print(datestr)
        year = datestr.year
        month = datestr.month
        last_day = calendar.monthrange(year, month)[1]
        final_date = datetime.date(year, month, last_day)
        print(final_date)
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": str(final_date)}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        Nellore = tracker.get_slot("nellore_Unit")
        Nellore_unit= Nellore.replace(Nellore,"Nellore")
        for d in data:
            if d["branch"] == Nellore_unit:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + str(d["target"])+ ",\nAchieved: "+str(d["achieved"])+",\nAchieved Percentage: "+str(d["achievedpercentage"])+",\nLast Month Achieved: "+str(d["asondate"]))
                return []
class ActionNelloreoncologyMonth(Action):
    def name(self):
        return "action_Nellore_oncology_month"
    def run(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        datestr = datetime.datetime.strptime(date1, "%Y-%m-%d")
        print(datestr)
        year = datestr.year
        month = datestr.month
        last_day = calendar.monthrange(year, month)[1]
        final_date = datetime.date(year, month, last_day)
        print(final_date)
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date":str(final_date) }
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        Nellore = tracker.get_slot("Nellore_Oncology_unit")
        Nellore_health = Nellore.replace(Nellore, "Nellore Oncology")
        for d in data:
            if d["branch"] == Nellore_health:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + str(d["target"])+ ",\nAchieved: "+str(d["achieved"])+",\nAchieved Percentage: "+str(d["achievedpercentage"])+",\nLast Month Achieved: "+str(d["asondate"]))
                return []
class ActionUnitWiseMonthMadopd(Action):
    def name(self) -> Text:
        return "action_Unit_MadOPD_month"
    def run(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        datestr=datetime.datetime.strptime(date1,"%Y-%m-%d")
        print(datestr)
        year=datestr.year
        month=datestr.month
        last_day = calendar.monthrange(year, month)[1]
        final_date = datetime.date(year, month, last_day)
        print(final_date)
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": str(final_date)}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        madh = tracker.get_slot("Unit_MAdhOPD")
        print(madh)
        M = madh.replace(madh, "Madhapur - OPD")
        for d in data:
            if d["branch"] == M:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + str(d["target"])+ ",\nAchieved: "+str(d["achieved"])+",\nAchieved Percentage: "+str(d["achievedpercentage"])+",\nLast Month Achieved: "+str(d["asondate"]))
                return []
class ActionUnitWiseMOIMonth(Action):
    def name(self) -> Text:
        return "action_Unit_MOIhitech_month"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        datestr = datetime.datetime.strptime(date1, "%Y-%m-%d")
        print(datestr)
        year = datestr.year
        month = datestr.month
        last_day = calendar.monthrange(year, month)[1]
        final_date = datetime.date(year, month, last_day)
        print(final_date)
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": str(final_date)}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        hite = tracker.get_slot("Unit_Hite")
        print(hite)
        MOIH= hite.replace(hite, "MOI - Hitech")
        print(MOIH)
        for d in data:
            if d["branch"] == MOIH :
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + str(d["target"])+ ",\nAchieved: "+str(d["achieved"])+",\nAchieved Percentage: "+str(d["achievedpercentage"])+",\nLast Month Achieved: "+str(d["asondate"]))
                return []
class ActionUnitWise_Madh_Month(Action):
    def name(self) -> Text:
        return "action_Madhunit_month"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        datestr = datetime.datetime.strptime(date1, "%Y-%m-%d")
        print(datestr)
        year = datestr.year
        month = datestr.month
        last_day = calendar.monthrange(year, month)[1]
        final_date = datetime.date(year, month, last_day)
        print(final_date)
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": str(final_date)}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        Madh_unit = tracker.get_slot("unit_Madh")
        print(Madh_unit)
        Madh= Madh_unit.replace(Madh_unit, "Madhapur")
        for d in data:
            if d["branch"] == Madh:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + str(d["target"])+ ",\nAchieved: "+str(d["achieved"])+",\nAchieved Percentage: "+str(d["achievedpercentage"])+",\nLast Month Achieved: "+str(d["asondate"]))
                return []
class ActionUnitMVPMonth(Action):
    def name(self) -> Text:
        return "action_Unit_MVP_month"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        datestr = datetime.datetime.strptime(date1, "%Y-%m-%d")
        print(datestr)
        year = datestr.year
        month = datestr.month
        last_day = calendar.monthrange(year, month)[1]
        final_date = datetime.date(year, month, last_day)
        print(final_date)
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": str(final_date)}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        MVP = tracker.get_slot("MVP_Unit")
        print(MVP)
        VMVP= MVP.replace(MVP, "Vizag MVP")
        for d in data:
            if d["branch"] == VMVP:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + str(d["target"])+ ",\nAchieved: "+str(d["achieved"])+",\nAchieved Percentage: "+str(d["achievedpercentage"])+",\nLast Month Achieved: "+str(d["asondate"]))
                return []
class ActionUnitWandCMonth(Action):
    def name(self) -> Text:
        return "action_Unit_W&C_month"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        datestr = datetime.datetime.strptime(date1, "%Y-%m-%d")
        print(datestr)
        year = datestr.year
        month = datestr.month
        last_day = calendar.monthrange(year, month)[1]
        final_date = datetime.date(year, month, last_day)
        print(final_date)
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": str(final_date)}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        viz = tracker.get_slot("W&C_unit")
        Viz0_WC= viz.replace(viz, "Vizag W&C")
        for d in data:
            if d["branch"] == Viz0_WC :
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + str(d["target"])+ ",\nAchieved: "+str(d["achieved"])+",\nAchieved Percentage: "+str(d["achievedpercentage"])+",\nLast Month Achieved: "+str(d["asondate"]))
                return []
class ActionUnitWiseMWCMonth(Action):
    def name(self) -> Text:
        return "action_Unit_MWC_month"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        datestr = datetime.datetime.strptime(date1, "%Y-%m-%d")
        print(datestr)
        year = datestr.year
        month = datestr.month
        last_day = calendar.monthrange(year, month)[1]
        final_date = datetime.date(year, month, last_day)
        print(final_date)
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": str(final_date)}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        hite = tracker.get_slot("MWC_unit")
        print(hite)
        H=hite.replace(hite, "MWC Hitech")
        for d in data:
            if d["branch"] == H :
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + str(d["target"])+ ",\nAchieved: "+str(d["achieved"])+",\nAchieved Percentage: "+str(d["achievedpercentage"])+",\nLast Month Achieved: "+str(d["asondate"]))
                return []
class ActionUnitMonthg(Action):
    def name(self) -> Text:
        return "action_Group_month"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        datestr = datetime.datetime.strptime(date1, "%Y-%m-%d")
        print(datestr)
        year = datestr.year
        month = datestr.month
        print(month)
        last_day = calendar.monthrange(year, month)[1]
        final_date = datetime.date(year, month, last_day)
        print(final_date)
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": str(final_date)}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        unit = tracker.get_slot("Grand_Total")
        print(unit)
        units=unit.replace(unit,"Total")
        for d in data:
            if d["branch"] == units:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + str(d["target"])+ ",\nAchieved: "+str(d["achieved"])+",\nAchieved Percentage: "+str(d["achievedpercentage"])+",\nLast Month Achieved: "+str(d["asondate"]))
                return []
class Action_admission_sub(Action):
    def name(self) -> Text:
        return "action_admission_sub"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons=[
            {"payload": "Cluster_admission", "title": "Cluster"},
            {"payload": "Center_admission", "title": "Center"},
            {"payload": "Total_admission", "title": "Total"}
        ]
        dispatcher.utter_message("Choose an option from below.",buttons=buttons)
        return []
class Actionclusteradmission(Action):
    def name(self) -> Text:
        return "action_Cluster_admission"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        buttons=[
            {"payload": "Madhapur_admission", "title": "Madhapur"},
            {"payload": "Andhra Pradesh_admission", "title": "Andhra Pradesh"},
            {"payload": "Vizag_admission", "title": "vizag"},
            {"payload": "ROTA_admission", "title": "ROTA"},
            {"payload": "Maharastra_admission", "title": "Maharastra"}
        ]
        dispatcher.utter_message("Which Cluster you are looking for",buttons=buttons)
        return []
class ActionMadhapuradm(Action):
    def name(self) -> Text:
        return "action_madhapur_cluster_admission"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        buttons=[
            {"payload": "Madh_adm", "title": "Madhapur"},
            {"payload": "MWC_adm", "title": "Suyosha"},
            {"payload": "chandanagar_adm", "title": "Chandanagar"},
            {"payload": "MCI_adm", "title": "MCI"}
        ]
        dispatcher.utter_message("Maadhapur Cluster",buttons=buttons)
        return []
class ActionTimeMADHAPURa(Action):
    def name(self) -> Text:
        return "action_Madhapur_time_admission"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        u = tracker.get_slot("Madhapur_Revenue_unit1")
        k= u.replace("_adm","")
        print(k)
        buttons=[
            {"payload": "what is the admission for "+k+" today", "title": "Today"},
            {"payload": "what is the admission for "+k+" yesterday", "title": "yesterday"},
            {"payload": "what is the admission for "+k+" last month", "title": "MTD"}
        ]
        dispatcher.utter_message("Please select a Time Period",buttons=buttons)
        return []
class ActionUnitWiseMadhapur_admission(Action):
    def name(self) -> Text:
        return "action_Madhapur_admission"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api-2/admissions-pdf.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = json.dumps({"accesskey": "fc3276ee1e5a4024cfdf","date":date1})
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST",api_url, data=todo, headers=headers)
        l = response.json()
        m = l["admlist"]
        hite = tracker.get_slot("unit_Madh")
        print(hite)
        MAdh=hite.replace(hite,"Madhapur")
        for d in m:
            if d["branch"]==MAdh:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + d["plan"]+ ",\nAchieved: " + d["adm"]+ ",\nAchieved Percentage: "+d["ach"]+",\nMTD: "+d["mtd"]+",\nGap: "+d["gap"])
                return []
class ActionUnitWiseMWCadmission(Action):
    def name(self) -> Text:
        return "action_Unit_MWC_admission"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api-2/admissions-pdf.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = json.dumps({"accesskey": "fc3276ee1e5a4024cfdf", "date": date1})
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST", api_url, data=todo, headers=headers)
        l = response.json()
        m = l["admlist"]
        hite = tracker.get_slot("MWC_unit")
        print(hite)
        H=hite.replace(hite, "MWC Hitech")
        for d in m:
            if d["branch"] == H :
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + d["plan"]+ ",\nAchieved: " + d["adm"]+ ",\nAchieved Percentage: "+d["ach"]+",\nMTD: "+d["mtd"]+",\nGap: "+d["gap"])
                return []
class ActionUnitWiseMCI_admission(Action):
    def name(self) -> Text:
        return "action_Unit_MCI_admission"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api-2/admissions-pdf.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = json.dumps({"accesskey": "fc3276ee1e5a4024cfdf","date":date1})
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST",api_url, data=todo, headers=headers)
        l = response.json()
        m = l["admlist"]
        hite = tracker.get_slot("Unit_Hite")
        print(hite)
        MOIH= hite.replace(hite, "MCI")
        for d in m:
            if d["branch"]== MOIH:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + d["plan"]+ ",\nAchieved: " + d["adm"]+ ",\nAchieved Percentage: "+d["ach"]+",\nMTD: "+d["mtd"]+",\nGap: "+d["gap"])
                return []
class ActionSlotandhra(Action):
    def name(self) -> Text:
        return "action_andhra_cluster_admission"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict) -> List[EventType]:
        buttons = [
            {"payload": "Nellore_admission", "title": "Nellore"},
            {"payload": "Kurnool_admission", "title": "Kurnool"}
        ]
        message=dispatcher.utter_message("Andhra Cluster",buttons=buttons)
        return []
class ActionTimeANDHRAa(Action):
    def name(self) -> Text:
        return "action_Andhra_time_admission"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        u = tracker.get_slot("Andhra_Pradesh_Revenue_unit1")
        k= u.replace("_admission","")
        print(k)
        buttons=[
            {"payload": "what is the admission for "+k+" today", "title": "Today"},
            {"payload": "what is the admission for "+k+" yesterday", "title": "yesterday"},
            {"payload": "what is the admission for "+k+" last month", "title": "MTD"}
        ]
        dispatcher.utter_message("Please select a Time Period",buttons=buttons)
        return []
class ActionUnitNelloreadm(Action):
    def name(self) -> Text:
        return "action_Nellore_admission"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api-2/admissions-pdf.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = json.dumps({"accesskey": "fc3276ee1e5a4024cfdf","date":date1})
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST", api_url, data=todo, headers=headers)
        l = response.json()
        m = l["admlist"]
        Nellore = tracker.get_slot("nellore_Unit")
        Nellore_unit= Nellore.replace(Nellore,"Nellore")
        for d in m:
            if d["branch"]==Nellore_unit:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + d["plan"]+ ",\nAchieved: " + d["adm"]+ ",\nAchieved Percentage: "+d["ach"]+",\nMTD: "+d["mtd"]+",\nGap: "+d["gap"])
                return []
class ActionUnitWiseUnits_admission(Action):
    def name(self) -> Text:
        return "action_Unit_admission"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api-2/admissions-pdf.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = json.dumps({"accesskey": "fc3276ee1e5a4024cfdf","date":date1})
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST",api_url, data=todo, headers=headers)
        l = response.json()
        m = l["admlist"]
        hite = tracker.get_slot("units")
        print(hite)
        unit = ''
        try:
            unit = hite[0].upper() + hite[1:]
        except:
            print(dispatcher.utter_message("Please enter the correct unit name and the month and year for unit"))
        for d in m:
            if d["branch"]==unit:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + d["plan"]+ ",\nAchieved: " + d["adm"]+ ",\nAchieved Percentage: "+d["ach"]+",\nMTD: "+d["mtd"]+",\nGap: "+d["gap"])
                return []
class Actionvizaga(Action):
    def name(self) -> Text:
        return "action_vizag_cluster_admission"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        buttons=[
            {"payload": "vizianagaram_adm", "title": "Vizianagaram"},
            {"payload": "Srikakulam_adm", "title": "Srikakulam"},
            {"payload": "MVP_adm", "title": "Vizag MVP"},
            {"payload": "vizag W&C_adm", "title": "Vizag W&C"}
        ]
        dispatcher.utter_message("Vizag Cluster",buttons=buttons)
        return []
class ActionTimeVIZAGadm(Action):
    def name(self) -> Text:
        return "action_Vizag_time_admission"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        u = tracker.get_slot("vizag_Revenue_unit1")
        k= u.replace("_adm","")
        print(k)
        buttons=[
            {"payload": "what is the admission for "+k+" today", "title": "Today"},
            {"payload": "what is the admission for "+k+" yesterday", "title": "yesterday"},
            {"payload": "what is the admission for "+k+" last month", "title": "MTD"}
        ]
        dispatcher.utter_message("Please select a Time Period",buttons=buttons)
        return []
class ActionUnitVizagMVP(Action):
    def name(self) -> Text:
        return "action_Unit_vizag_MVP_admission"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api-2/admissions-pdf.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        m = l["admlist"]
        MVP = tracker.get_slot("MVP_Unit")
        print(MVP)
        VMVP= MVP.replace(MVP, "Vizag MVP")
        for d in m:
            if d["branch"] == VMVP:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + d["plan"]+ ",\nAchieved: " + d["adm"]+ ",\nAchieved Percentage: "+d["ach"]+",\nMTD: "+d["mtd"]+",\nGap: "+d["gap"])
                return []
class ActionUnitWandCadm(Action):
    def name(self) -> Text:
        return "action_Unit_W&C_admission"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api-2/admissions-pdf.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        m = l["admlist"]
        viz = tracker.get_slot("W&C_unit")
        Viz0_WC= viz.replace(viz, "Vizag W&C")
        for d in m:
            if d["branch"] == Viz0_WC:
                message = dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + d["plan"]+ ",\nAchieved: " + d["adm"]+ ",\nAchieved Percentage: "+d["ach"]+",\nMTD: "+d["mtd"]+",\nGap: "+d["gap"])
                return []
class ActionROTAaclus(Action):
    def name(self) -> Text:
        return "action_rota_cluster_admission"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        buttons=[
            {"payload": "Karimnagar_adm", "title": "Karimnagar"},
            {"payload": "Nizamabad_adm", "title": "Nizamabad"},
            {"payload": "Kakinada_adm", "title": "Kakinada"},
            {"payload": "begumpet_adm", "title": "Begumpet"},
            {"payload": "zaheerabad_adm", "title": "Zaheerabad"},
            {"payload": "Sangareddy_adm", "title": "Sangareddy"}
        ]
        dispatcher.utter_message("ROTA Cluster",buttons=buttons)
        return []
class ActionTimeROTAadm(Action):
    def name(self) -> Text:
        return "action_ROTA_time_admission"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        u = tracker.get_slot("ROTA_admission_unit1")
        k= u.replace("_adm","")
        print(k)
        buttons=[
            {"payload": "what is the admission for "+k+" today", "title": "Today"},
            {"payload": "what is the admission for "+k+" yesterday", "title": "yesterday"},
            {"payload": "what is the admission for "+k+" last month", "title": "MTD"}
        ]
        dispatcher.utter_message("Please select a Time Period",buttons=buttons)
        return []
class ActionMHadm(Action):
    def name(self) -> Text:
        return "action_mh_cluster_admission"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        buttons=[
            {"payload": "nashik_adm", "title": "Nashik"},
            {"payload": "Aurangabad_adm", "title": "Aurangabad"},
            {"payload": "navimumbai_adm", "title": "Navimumbai"},
            {"payload": "Sangamner_adm", "title": "Sangamner"},
            {"payload": "Pune_adm", "title": "Pune"}
        ]
        dispatcher.utter_message("Maharastra Cluster",buttons=buttons)
        return []
class ActionTimeMHadm(Action):
    def name(self) -> Text:
        return "action_MH_time_admission"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        u = tracker.get_slot("MH_Revenue_unit1")
        k=u.replace("_adm","")
        print(k)
        buttons=[
            {"payload": "what is the admission for "+k+" today", "title": "Today"},
            {"payload": "what is the admission for "+k+" yesterday", "title": "yesterday"},
            {"payload": "what is the admission for "+k+" last month", "title": "MTD"}
        ]
        dispatcher.utter_message("Please select a Time Period",buttons=buttons)
        return []
class Action_centreadm(Action):
    def name(self) -> Text:
        return "action_Center_admission"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        j=["Nizamabad_center_adm", "Karimnagar_center_adm", "Sangareddy_center_adm", "Kurnool_center_adm", "Kakinada_center_adm", "Aurangabad_center_adm", "nashik_center_adm", "Sangamner_center_adm", "Nellore_center_adm", "MCI_center_adm", "vizag W&C_center_adm","Vizianagaram_center_adm","MVP_center_adm","Madh_center_adm","MWC_center_adm","Begumpet_center_adm","Navimumbai_center_adm","Zaheerabad_center_adm","Srikakulam_center_adm","Pune_center_adm","Chandanagar_center_adm"]
        buttons=[
            {"payload": j[0], "title": "Nizamabad"},
            {"payload": j[1], "title": "Karimnagar"},
            {"payload": j[2], "title": "Sangareddy"},
            {"payload": j[3], "title": "Kurnool"},
            {"payload": j[4], "title": "Kakinada"},
            {"payload": j[5], "title": "Aurangabad"},
            {"payload": j[6], "title": "Nashik"},
            {"payload": j[7], "title": "Sangamner"},
            {"payload": j[8], "title": "Nellore"},
            {"payload": j[9], "title": "MCI"},
            {"payload": j[10], "title": "Vizag W&C"},
            {"payload": j[11], "title": "Vizianagaram"},
            {"payload": j[12], "title": "Vizag MVP"},
            {"payload": j[13], "title": "Madhapur"},
            {"payload": j[14], "title": "MWC Hitech"},
            {"payload": j[15], "title": "Begumpet"},
            {"payload": j[16], "title": "Navimumbai"},
            {"payload": j[17], "title": "Zaheerabad"},
            {"payload": j[18], "title": "Srikakulam"},
            {"payload": j[19], "title": "Pune"},
            {"payload": j[20], "title": "Chandanagar"}

        ]
        dispatcher.utter_message("Admission Center",buttons=buttons)
        return []
class ActionTimeCenteradm(Action):
    def name(self) -> Text:
        return "action_Center_sub_admission_time"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        u = tracker.get_slot("Center_sub_unit1")
        k= u.replace("_center_adm","")
        print(k)
        buttons=[
            {"payload": "what is the admission for "+k+" today", "title": "Today"},
            {"payload": "what is the admission for "+k+" yesterday", "title": "yesterday"},
            {"payload": "what is the admission for "+k+" last month", "title": "MTD"}
        ]
        dispatcher.utter_message("Please select a Time Period",buttons=buttons)
        return []
class ActionUnitWiseTarget_admission(Action):
    def name(self) -> Text:
        return "action_Total_admission"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        u = tracker.get_slot("Group")
        k= u.replace("_admission","")
        print(k)
        buttons=[
            {"payload": "what is the admission for "+k+" today", "title": "Today"},
            {"payload": "what is the admission for "+k+" yesterday", "title": "yesterday"},
            {"payload": "what is the admission for "+k+" last month", "title": "MTD"}
        ]
        dispatcher.utter_message("Please select a Time Period",buttons=buttons)
        return []
class ActionUnitTargetadm(Action):
    def name(self) -> Text:
        return "action_Group_admission"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api-2/admissions-pdf.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = json.dumps({"accesskey": "fc3276ee1e5a4024cfdf","date": date1})
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST",api_url, data=todo, headers=headers)
        l = response.json()
        m=l["admlist"]
        unit = tracker.get_slot("Grand_Total")
        units= unit.replace(unit,"Total")
        for d in m:
            if d["branch"]==units:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + d["plan"]+ ",\nAchieved: "+d["adm"]+",\nAchieved Percentage: "+d["ach"]+",\nMTD: "+d["mtd"]+",\nGap: "+d["gap"])
                return []
class ActionUnitWiseNellore_admission_month(Action):
    def name(self) -> Text:
        return "action_Unit_admission_month"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api-2/admissions-pdf.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        datestr = datetime.datetime.strptime(date1, "%Y-%m-%d")
        print(datestr)
        year = datestr.year
        month = datestr.month
        last_day = calendar.monthrange(year, month)[1]
        final_date = datetime.date(year, month, last_day)
        print(final_date)
        todo = json.dumps({"accesskey": "fc3276ee1e5a4024cfdf","date": str(final_date)})
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST",api_url, data=todo, headers=headers)
        l = response.json()
        m = l["admlist"]
        hite = tracker.get_slot("units")
        print(hite)
        unit = ''
        try:
            unit = hite[0].upper() + hite[1:]
        except:
            print(dispatcher.utter_message("Please enter the correct unit name and the month and year for unit"))
        for d in m:
            if d["branch"]==unit:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + d["plan"]+ ",\nAchieved: " + d["adm"]+ ",\nAchieved Percentage: "+d["ach"]+",\nMTD: "+d["mtd"]+",\nGap: "+d["gap"])
                return []
class ActionUnitW_CMonthadm(Action):
    def name(self) -> Text:
        return "action_Nellore_admission_month"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api-2/admissions-pdf.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        datestr = datetime.datetime.strptime(date1, "%Y-%m-%d")
        print(datestr)
        year = datestr.year
        month = datestr.month
        last_day = calendar.monthrange(year, month)[1]
        final_date = datetime.date(year, month, last_day)
        print(final_date)
        todo = json.dumps({"accesskey": "fc3276ee1e5a4024cfdf","date": str(final_date)})
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST", api_url, data=todo, headers=headers)
        l = response.json()
        m = l["admlist"]
        Nellore = "Nellore"
        Nellore_unit = Nellore.replace(Nellore, "Nellore")
        for d in m:
            if d["branch"]==Nellore_unit:
                message = dispatcher.utter_message("Hey,Here are the results "+ "\nLocation: "+ d["branch"]+ ",\nTarget: " + d["plan"]+ ",\nAchieved: "+ d["adm"]+ ",\nAchieved Percentage: " + d["ach"]+",\nMTD: "+d["mtd"]+",\nGap: "+d["gap"])
                return []
class ActionUnitWiseMCI_admission_month(Action):
    def name(self) -> Text:
        return "action_Unit_MCI_admission_month"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api-2/admissions-pdf.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        datestr = datetime.datetime.strptime(date1, "%Y-%m-%d")
        print(datestr)
        year = datestr.year
        month = datestr.month
        last_day = calendar.monthrange(year, month)[1]
        final_date = datetime.date(year, month, last_day)
        print(final_date)
        todo = json.dumps({"accesskey": "fc3276ee1e5a4024cfdf","date": str(final_date)})
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST",api_url, data=todo, headers=headers)
        l = response.json()
        m = l["admlist"]
        hite = tracker.get_slot("Unit_Hite")
        print(hite)
        MOIH= hite.replace(hite,"MCI")
        for d in m:
            if d["branch"]==MOIH:
                message=dispatcher.utter_message("Hey,Here are the results "+ "\nLocation: "+ d["branch"]+ ",\nTarget: " + d["plan"]+ ",\nAchieved: " + d["adm"]+ ",\nAchieved Percentage: "+d["ach"]+",\nMTD: "+d["mtd"]+",\nGap: "+d["gap"])
                return []
class ActionUnitWiseMVP_admission_month(Action):
    def name(self) -> Text:
        return "action_Vizag_MVP_admission_month"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api-2/admissions-pdf.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        datestr = datetime.datetime.strptime(date1, "%Y-%m-%d")
        print(datestr)
        year = datestr.year
        month = datestr.month
        last_day = calendar.monthrange(year, month)[1]
        final_date = datetime.date(year, month, last_day)
        print(final_date)
        todo = json.dumps({"accesskey": "fc3276ee1e5a4024cfdf","date": str(final_date)})
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST",api_url, data=todo, headers=headers)
        l = response.json()
        m = l["admlist"]
        hite = tracker.get_slot("MVP_Unit_adm")
        print(hite)
        Madh=hite.replace(hite,"Vizag MVP")
        for d in m:
            if d['branch']==Madh:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + d["plan"]+ ",\nAchieved: " + d["adm"]+ ",\nAchieved Percentage: "+d["ach"]+",\nMTD: "+d["mtd"]+",\nGap: "+d["gap"])
                return []
class ActionUnitWiseVizagW_admission_month(Action):
    def name(self) -> Text:
        return "action_Vizag_W&C_admission_month"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api-2/admissions-pdf.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        datestr = datetime.datetime.strptime(date1, "%Y-%m-%d")
        print(datestr)
        year = datestr.year
        month = datestr.month
        last_day = calendar.monthrange(year, month)[1]
        final_date = datetime.date(year, month, last_day)
        print(final_date)
        todo = json.dumps({"accesskey": "fc3276ee1e5a4024cfdf","date": str(final_date)})
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST", api_url, data=todo, headers=headers)
        l = response.json()
        m = l["admlist"]
        hite = tracker.get_slot("W&C_unit")
        print(hite)
        Madh=hite.replace(hite,"Vizag W&C")
        for d in m:
            if d["branch"]==Madh:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + d["plan"]+ ",\nAchieved: " + d["adm"]+ ",\nAchieved Percentage: "+d["ach"]+",\nMTD: "+d["mtd"]+",\nGap: "+d["gap"])
                return []
class ActionUnitWiseMWC_admission_month(Action):
    def name(self) -> Text:
        return "action_MWC_admission_month"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api-2/admissions-pdf.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        datestr = datetime.datetime.strptime(date1, "%Y-%m-%d")
        print(datestr)
        year = datestr.year
        month = datestr.month
        last_day = calendar.monthrange(year, month)[1]
        final_date = datetime.date(year, month, last_day)
        print(final_date)
        todo = json.dumps({"accesskey": "fc3276ee1e5a4024cfdf","date": str(final_date)})
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST",api_url, data=todo, headers=headers)
        l = response.json()
        m = l["admlist"]
        hite = tracker.get_slot("MWC_unit_adm")
        print(hite)
        Madh=hite.replace(hite,"MWC Hitech")
        for d in m:
            if d['branch']==Madh:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + d["plan"]+ ",\nAchieved: "+d["adm"]+ ",\nAchieved Percentage: "+d["ach"]+",\nMTD: "+d["mtd"]+",\nGap: "+d["gap"])
                return []
class ActionUnitWiseMadhapur_admission_month(Action):
    def name(self) -> Text:
        return "action_Madhapur_admission_month"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api-2/admissions-pdf.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        datestr = datetime.datetime.strptime(date1, "%Y-%m-%d")
        print(datestr)
        year = datestr.year
        month = datestr.month
        last_day = calendar.monthrange(year, month)[1]
        final_date = datetime.date(year, month, last_day)
        print(final_date)
        todo = json.dumps({"accesskey": "fc3276ee1e5a4024cfdf","date": str(final_date)})
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST",api_url, data=todo, headers=headers)
        l = response.json()
        m = l["admlist"]
        hite = tracker.get_slot("unit_Madh")
        print(hite)
        Madh=hite.replace(hite, "Madhapur")
        for d in m:
            if d["branch"]==Madh:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\ntarget: " + d["plan"]+ ",\nAchieved: " +d["adm"]+ ",\nAchieved Percentage: "+d["ach"]+",\nMTD: "+d["mtd"]+",\nGap: "+d["gap"])
                return []
class ActionUnitMonthadm(Action):
    def name(self) -> Text:
        return "action_Group_admission_month"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api-2/admissions-pdf.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        datestr = datetime.datetime.strptime(date1, "%Y-%m-%d")
        print(datestr)
        year = datestr.year
        month = datestr.month
        last_day = calendar.monthrange(year, month)[1]
        final_date = datetime.date(year, month, last_day)
        print(final_date)
        todo = json.dumps({"accesskey": "fc3276ee1e5a4024cfdf","date": str(final_date)})
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST",api_url, data=todo, headers=headers)
        l = response.json()
        m=l["admlist"]
        unit = tracker.get_slot("Grand_Total")
        print(unit)
        units = unit.replace(unit, "Total")
        for d in m:
            if d["branch"] == units:
                message=dispatcher.utter_message("Hey,Here are the results "+"\nLocation: "+d["branch"]+ ",\nTarget: " + d["plan"]+ ",\nAchieved: "+d["adm"]+",Achieved Percentage: "+d["ach"]+",\nMTD: "+d["mtd"]+",Gap: "+d["gap"])
                return []
j = []
class ActionFormName(Action):
    def name(self) -> Text:
        return "action_name"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        print(name)
        j.append(name)
        print(len(j))
        dispatcher.utter_message("Thank you "+name)
        j.pop()
        return []

