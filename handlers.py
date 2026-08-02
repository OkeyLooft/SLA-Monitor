from datetime import datetime
import json
from pathlib import Path
import uuid
import utils

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database.json"

def create_ticket():
    yes_or_no = ""
    while yes_or_no != "y":
        ticket_name = input("Введите название тикета: ")
        discription_ticket = input("Введите описание тикета: ")
        while True:
            try:
                time_sla = int(input("Введите время SLA: "))
                break
            except ValueError:
                print("Проверьте что вы ввели числовое значение")
    # Пытаюсь реализовать списки и словари, что бы при выводе выводилось читаемое чтиво для понятности, все ли верно ввбили в тикет
        print(50 * '-')

        with open(DB_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        number = 0
        for d in data:
            if 'id' in d:
                number += 1
                    
        datetime_now = datetime.now()
        ticket_dict = {
                "id": number,
                "name": ticket_name,
                "description": discription_ticket,
                "created_at": f"{datetime_now.year}-{datetime_now.month}-{datetime_now.day} {datetime_now.hour}:{datetime_now.minute}:{datetime_now.second}",
                "sla": time_sla,
                "status": "OPEN"
            }
        for keys, values in ticket_dict.items():
            print(f"{keys}: {values}")

    # Запрос ОС по тикету
        while True:
            yes_or_no = input("Все верно ?(y/N) ").lower()
            if yes_or_no =="n":
                break
            elif yes_or_no == 'y':
                break
            else:
                print("Введите y/N")

    return ticket_dict

def add_to_json(tic_dict):
    data = []
    if DB_PATH.exists() and DB_PATH.stat().st_size > 0:
        with open(DB_PATH, "r", encoding="utf-8") as f:
            data=json.load(f)

    data.append(tic_dict)

    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def show_ticket():
    with open(DB_PATH, "r", encoding="utf-8") as f:
        data=json.load(f)
    
    print("ID | NAME          | STATUS | HOURS LEFT")
    print(50 * '-')
    for d in data:
        print(f"{d['id']:<3}|{d['name']:<15}|{d['status']:<8}|")
        print(50 * '-')

def find_ticket():
    with open(DB_PATH, "r", encoding="utf-8") as f:
        data=json.load(f)
    while True:
        print(50 * '-')
        print("1. ID \n2. NAME \n3. STATUS \n4. Exit ")
        print(50 * '-')
        user_input = input("Введите подходящий номер: ")
        if user_input == '4':
            break
        elif user_input == '1':
            print(50 * '-')
            id_input = int(input("Введите ID таска: "))
            data_by_id = [item for item in data if item.get('id') == id_input]
            print(data_by_id)
        elif user_input == '2':
            print(50 * '-')
            name_input = input("Введите NAME таска: ")
            data_by_id = [item for item in data if item.get('name') == name_input]
            print(data_by_id)
        elif user_input == '3':
            print(50 * '-')
            status_input = input("Введите STATUS таска: ").upper()
            data_by_id = [item for item in data if item.get('status') == status_input]
            for d in data_by_id:
                print(d)

def change_status():
    pass
