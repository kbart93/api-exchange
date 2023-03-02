import requests

url = "https://api.nbp.pl/api/exchangerates/tables/A/"
body = requests.get(url)
response = body.json()

def showing_currencies():
    d = response[0]["rates"]
    values = [i["code"] for i in d]
    print(values)

def sell_currencies():
    currency = input("Jaką walutę chciałbyś sprzedać? [USD/EUR/CHF]")
    quantity = int(input(f"Ile {currency} chciałbyś sprzedać? "))

    for rate in response[0]["rates"]:
        if currency == rate["code"]:
            result = quantity * float(rate["mid"])
            print(f"Otrzymasz {round(result,2)} złotych.")
            break

def buy_currencies():
    currency = input("Jaką walutę chciałbyś kupić? [USD/EUR/CHF]")
    quantity = int(input(f"Ile {currency} chciałbyś kupić? "))

    for rate in response[0]["rates"]:
        if currency == rate["code"]:
            result = quantity * float(rate["mid"])
            print(f"Potrzebujesz {round(result,2)} złotych aby kupić {quantity} {currency}.")
            break

def bank_fee():
    currency = input("Jaką walutę chciałbyś sprzedać/kupić? [USD/EUR/CHF]")
    quantity = int(input(f"Ile {currency} chciałbyś sprzedać/kupić? "))

    for rate in response[0]["rates"]:
        if currency == rate["code"]:
            result = quantity * float(rate["mid"]*0.05)
            print(f"Kantor pobierze {round(result,2)} złotych za wymianę.")
            break


while True:
    print()
    print("KALKULATOR WYMIANY WALUT")
    print()
    print("1. Pokaż dostępne waluty.")
    print("2. Chce sprzedać walutę.")
    print("3. Chce kupić walutę.")
    print("4. Sprawdź opłaty kantoru za wymianę walut.")
    print("5. Zakończ.")
    print()

    choice = int(input("Wybierz opcję: "))

    if choice == 1:
        showing_currencies()

    if choice == 2:
        sell_currencies()

    if choice == 3:
        buy_currencies()

    if choice == 4:
        bank_fee()

    if choice == 5:
        print("Do zobaczenia!")
        break