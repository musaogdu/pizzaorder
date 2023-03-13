import csv
import datetime


with open("menu.txt", "w") as f:
    f.write("* Lütfen Bir Pizza Tabanı Seçiniz:\n")
    f.write("1: Klasik\n")
    f.write("2: Margarita\n")
    f.write("3: TürkPizza\n")
    f.write("4: Sade Pizza\n")
    f.write("* ve seçeceğiniz sos:\n")
    f.write("11: Zeytin\n")
    f.write("12: Mantarlar\n")
    f.write("13: Keçi Peyniri\n")
    f.write("14: Et\n")
    f.write("15: Soğan\n")
    f.write("16: Mısır\n")
    f.write("* Teşekkür ederiz!")


class Pizza:
    menu = {
        "Klasik Pizza": 30,
        "Margarita Pizza": 25,
        "Türk Pizza": 35,
        "Sade Pizza": 20
    }

    sauces = {
        "Zeytin": 4,
        "Mantarlar": 4,
        "Keçi Peyniri": 3,
        "Et": 8,
        "Soğan": 2,
        "Mısır": 1.5
    }

    def __init__(self, name, sauce):
        self.name = name
        self.sauce = sauce
        self.price = self.menu[name] + self.sauces[sauce]

    def __str__(self):
        return f"{self.name} pizza with {self.sauce} sauce - ${self.price:.2f}"

    @classmethod
    def show_menu(cls):
        print("Menu:")
        for name, price in cls.menu.items():
            print(f"{name} pizza: ${price:.2f}")
        print("\nSauces:")
        for i, (name, price) in enumerate(cls.sauces.items(), start=11):
            print(f"{i}: {name} sauce - ${price:.2f}")
        print("\nThank you!")

    @classmethod
    def create(cls):
        name_choice = input("Lütfen pizzanızı seçiniz:\n1: Klasik Pizza\n2: Margarita Pizza\n3: Türk Pizza\n4: Sade Pizza\n")
        name_dict = {"1": "Klasik Pizza", "2": "Margarita Pizza", "3": "Türk Pizza", "4": "Sade Pizza"}
        name = name_dict.get(name_choice)
        if name is None:
            print("Geçersiz seçim")
            return None
        sauce_choice = input(
            "Lütfen sos seçiniz:\n11: Zeytin\n12: Mantarlar\n13: Keçi Peyniri\n14: Et\n15: Soğan\n16: Mısır\n")
        sauce_dict = {"11": "Zeytin", "12": "Mantarlar", "13": "Keçi Peyniri", "14": "Et", "15": "Soğan", "16": "Mısır"}
        sauce = sauce_dict.get(sauce_choice)
        if sauce is None:
            print("Geçersiz seçim.")
            return None
        return cls(name, sauce)


class Order:
    def __init__(self, pizza, name, tc, card_num, card_pin):
        self.pizza = pizza
        self.name = name
        self.tc = tc
        self.card_num = card_num
        self.card_pin = card_pin
        self.timestamp = datetime.datetime.now()

    def total_price(self):
        return self.pizza.price

    def save_to_database(self):
        with open("Orders_Database.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(
                [self.name, self.tc, self.card_num, str(self.pizza), self.total_price(), self.timestamp, self.card_pin])


def main():
    Pizza.show_menu()
    pizza = None
    while pizza is None:
        pizza = Pizza.create()
    name = input("İsminizi giriniz. ")
    tc = input("T.C. kimlik numaranızı giriniz. ")
    card_num = input(" Kredi kartı numaranızı giriniz. ")
    card_pin = input("Kredi kartı şifrenizi giriniz. ")
    order = Order(pizza, name, tc, card_num, card_pin)
    print(f"\nOrder summary:\n{order.pizza}\nTotal price: ${order.total_price():.2f}")
    confirm = input("Siparişi onaylıyor musunuz? (e/h) ")
    if confirm.lower() == "e":
        order.save_to_database()
        print("Sipariş alındı.")
    else:
        print("Sipariş iptal edildi.")


if __name__ == "__main__":
    main()

