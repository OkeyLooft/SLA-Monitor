import handlers
import utils

def main():
    utils.print_header_SLA()

    while True:
        utils.print_menu()
        print()
        try:
            user_input = int(input("Выберите подходящий вариант: "))
        except ValueError:
            print("Убедитесь, что ввели именно номер варианта")

        if user_input == 7:
            break
        elif user_input > 7 or user_input < 1:
            print(50 * '-')
            print("Выберите значение в диапазоне 1-7")
        elif user_input == 1:
            handlers.create_ticket()
            handlers.add_to_json()



if __name__ == "__main__":
    main()