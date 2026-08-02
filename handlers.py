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

        id_ = []
        for d in data:
            id_num = d.get('id')
            id_.append(id_num)
        if id_ == []:
            number = 0
        else:
            id_max = max(id_)
            number = 0
            number = id_max + 1


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

def show_tickets():
    with open(DB_PATH, "r", encoding="utf-8") as f:
        data=json.load(f)
    
    print("ID | NAME          | STATUS      | HOURS LEFT")
    print(50 * '-')
    now = datetime.now().replace(microsecond=0)
    for d in data:
        dt = datetime.strptime(d["created_at"], "%Y-%m-%d %H:%M:%S")
        delta = now - dt
        print(f"{d['id']:<3}|{d['name']:<15}|{d['status']:<13}|{delta}")
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
    with open(DB_PATH, "r", encoding="utf-8") as f:
        data=json.load(f)
    for d in data:
        print(d)
    print(50 * '-')
    id_input = int(input("Введите ID таска: "))
    data_by_id = [item for item in data if item.get('id') == id_input]
    while True:
        print(data_by_id, "<-- Итоговый вид Таска")
        print(50 * '-')    
        print("1. OPEN \n2. IN_PROGRESS \n3. CLOSED \n4. EXPIRED \n5. EXIT")
        change_input = input("Введите номер статуса на который вы хотите изменить таск: ")
        if change_input == '5':
            break
        elif change_input == '1':
            data_by_id[0]["status"] = 'OPEN'
            with open(DB_PATH, 'w', encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        elif change_input == '2':
            data_by_id[0]["status"] = 'IN_PROGRESS'
            with open(DB_PATH, 'w', encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        elif change_input == '3':
            data_by_id[0]["status"] = 'CLOSED'
            with open(DB_PATH, 'w', encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        elif change_input == '4':
            data_by_id[0]["status"] = 'EXPIRED'
            with open(DB_PATH, 'w', encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        else:
            print("Введите допустимый номер")

def del_ticket():
    with open(DB_PATH, "r", encoding="utf-8") as f:
        data=json.load(f)

    while True: 
        for d in data:
            print(d)
        print(50 * '-')
        del_input = input("Выберите ID тикета который хотите удалить(Или введите Q): ").lower()
        if del_input == "q":
            break
        del_input = int(del_input)
        data_by_id = [item for item in data if item.get('id') == del_input]

        print(data_by_id)
        que_input = input("Вы уверены ?(y/N) ")
        print(50 * '-')
        if que_input == "y":
            data = [item for item in data if item.get('id') != del_input]

            with open(DB_PATH, 'w', encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            
        elif que_input == "n":
            print(50 * '-')
            for d in data:
                print(d)
            pass
        
