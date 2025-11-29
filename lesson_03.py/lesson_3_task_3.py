from address import Address
from mailing import Mailing

# Адресат отправителя и получателя
sender_address = Address("125009", "Москва", "Тверская", "7", "15")
recipient_address = Address("603000", "Нижний Новгород", "Большая Покровская", "40", "22")

# Экземпляр
mailing = Mailing(
    to_address=recipient_address,
    from_sddress=sender_address,
    cost=400.00,
    track="RU123456789RU"
)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f" в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")