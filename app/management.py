import time

from flask import request
from spartan import Spartan
from pymongo import MongoClient

while True:
    try:
        client = MongoClient("mongodb://db.dungureanu.devops106:27017")
        break
    except Exception as ex:
        print(ex)
        print("Trying to connect to the database.")
        time.sleep(2)

db = client.spartans


def spartan_info(spartan_id_to_display):
    sparta_idx = int(spartan_id_to_display)
    record_search_result = db.clients_data.find({"sparta_id": sparta_idx})
    search_result_list = list(record_search_result)
    if len(search_result_list) > 0:
        spartan_details = search_result_list[0]
        return f"ID found with following details:\n{spartan_details}"
    return f"ID not found."


def read_spartan_from_json():
    if request.is_json:
        spartan_data = request.get_json()

        if len(spartan_data["first_name"]) > 1:
            s_fn = spartan_data["first_name"]
        else:
            return "ERROR: first name should have at least 2 characters."

        if len(spartan_data["last_name"]) > 1:
            s_ln = spartan_data["last_name"]
        else:
            return "ERROR: last name should have at least 2 characters."

        if int(spartan_data["birth_day"]) in range(1, 32):
            s_bd = spartan_data["birth_day"]
        else:
            return "ERROR: Day of birth should be a number between 1 and 31."

        if int(spartan_data["birth_month"]) in range(1, 13):
            s_bm = spartan_data["birth_month"]
        else:
            return "ERROR: Month of birth should be a number between 1 and 12."

        if int(spartan_data["birth_year"]) in range(1900, 2005):
            s_by = spartan_data["birth_year"]
        else:
            return "ERROR: Year of birth should be a number between 1900 and 2004."

        if len(spartan_data["course"]) > 2:
            s_co = spartan_data["course"]
        else:
            return "ERROR: Course name should have at least 3 characters."

        if len(spartan_data["stream"]) > 2:
            s_st = spartan_data["stream"]
        else:
            return "ERROR: Stream's name should have at least 3 characters."
        if check_id_in_db(spartan_data["sparta_id"]):
            return "ID already in database."
        else:
            s_id = spartan_data["sparta_id"]
        temp_spartan = Spartan(s_id, s_fn, s_ln, s_bd, s_bm, s_by, s_co, s_st)
        return temp_spartan
    else:
        return None


def add_to_db():
    spartan = read_spartan_from_json()

    if spartan is None:

        return "No valid data received."

    elif type(spartan) is str:

        return f"{spartan}"

    else:

        record = db.clients_data.insert_one(vars(spartan))
        return f"Entry saved{record}."


def check_id_in_db(id_to_check):
    records = db.clients_data.find({"sparta_id": id_to_check})
    data = list(records)
    return len(data) > 0


def display_db():
    data_list = list(db.clients_data.find())
    result = ""
    for each_entry in data_list:
        result += f"{each_entry}\n\n"
    return result

# def delete_from_db(id_to_delete):
#     global all_spartans_db
#     # load_db_from_file()
#     if id_to_delete in all_spartans_db.keys():
#         del all_spartans_db[id_to_delete]
#         save_db_as_json()
#         return f"Deleted entry with ID: {id_to_delete}"
#     else:
#         return f"ID: {id_to_delete} not in database."
