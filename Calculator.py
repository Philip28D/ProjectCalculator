def calculator():
    # Inițializează valoarea curentă (valoarea implicită este 0)
    current_value = 0.0

    # Afișarea valorii inițiale
    print(current_value)

    while True:
        # Obțineți datele introduse de utilizator și elimină toate spațiile albe de început și sfârșit
        user_input = input("> ").strip()

        # Verifică dacă utilizatorul dorește să iasă
        if user_input == 'x':
            break

        # Împărțiți intrarea în operație și număr
        if user_input[0] in ('+', '-', '*', '/', '='):
            operator = user_input[0]
            number = float(user_input[1:])

            # Efectuarea operațiunii specificate
            if operator == '+':
                current_value += number
            elif operator == '-':
                current_value -= number
            elif operator == '*':
                current_value *= number
            elif operator == '/':
                if number != 0:  # Împărțirea la 0 nu este permisa
                    current_value /= number
                else:
                    print("Invalid operation (division by zero)")
                    continue
            elif operator == '=': # Setarea valorii curente
                current_value = number
            else:
                print("Invalid operation")
                continue

            # Afișarea valorii curente
            print(current_value)
        else:
            print("Invalid operation")


calculator()