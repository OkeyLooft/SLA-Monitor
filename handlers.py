from datetime import datetime
import json

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

        print(50 * '-')
        datetime_now = datetime.now()
        ticket_dict = [{
                "id": 1,
                "name": ticket_name,
                "description": discription_ticket,
                "created_at": f"{datetime_now.year}-{datetime_now.month}-{datetime_now.day} {datetime_now.hour}:{datetime_now.minute}:{datetime_now.second}",
                "sla": time_sla,
                "status": "OPEN"
            }]
        for keys in ticket_dict:
            for key in keys:
                print(key)
        # for keys, values in dict(ticket_dict).items():
        #     print(f"{keys}: {values}")
        # print(50 * '-')

        while True:
            yes_or_no = input("Все верно ?(y/N) ").lower()
            if yes_or_no =="n":
                break
            elif yes_or_no == 'y':
                break
            else:
                print("Введите y/N")
    
    # ticket_dict = [
    #     {
    #     "id": 1,
    #     "name": ticket_name,
    #     "description": discription_ticket,
    #     "created_at": f"{datetime_now.year}-{datetime_now.month}-{datetime_now.day} {datetime_now.hour}:{datetime_now.minute}:{datetime_now.second}",
    #     "sla": time_sla,
    #     "status": "OPEN"
    # }
    # ]

    with open('database.json', 'a', encoding="utf-8") as f:
        json.dump(ticket_dict, f, indent=4, ensure_ascii=False)
        f.write('\n')

    return
create_ticket()

