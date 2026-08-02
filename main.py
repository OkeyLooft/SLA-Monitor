import handlers
import utils

def main():
    utils.print_header_SLA()

    while True:
        utils.print_menu()
        print()
        try:
            user_input = int(input("Выберите подходящий вариант: "))
        except UnboundLocalError:
            print("Вы не ввели номера")
        except ValueError:
            print("Убедитесь, что ввели именно номер варианта")

        if user_input == 7:
            break
        elif user_input > 7 or user_input < 1:
            print(50 * '-')
            print("Выберите значение в диапазоне 1-7")
        elif user_input == 1:
            tic_dict = handlers.create_ticket()
            handlers.add_to_json(tic_dict)
        elif user_input == 2:
            handlers.show_tickets()
        elif user_input == 3:
            handlers.find_ticket()
        elif user_input == 4:
            handlers.change_status()
        elif user_input == 5:
            handlers.del_ticket()


if __name__ == "__main__":
    main()