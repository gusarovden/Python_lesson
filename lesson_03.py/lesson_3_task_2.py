from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15 Pro", "+79111111111"),
    Smartphone("Samsung", "Galaxy S24", "+79222222222"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79333333333"),
    Smartphone("Google", "Pixel 8", "+79444444444"),
    Smartphone("OnePlus", "11R", "+79555555555")
]

for phone in catalog:
    print(f"{phone.brend} - {phone.model}. {phone.phone_number}")