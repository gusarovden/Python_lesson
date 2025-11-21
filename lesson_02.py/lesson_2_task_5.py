def month_to_season(month):
    if not isinstance(month, int) or month < 1 or month > 12:
        raise ValueError("Номер месяца должен быть целым числом от 1 до 12")
    
    if month in (12, 1, 2):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    else:  # месяцы 9, 10, 11
        return "Осень"
    
print(month_to_season(2))   
print(month_to_season(5))   
print(month_to_season(8))   
print(month_to_season(11))  
print(month_to_season(12))   
