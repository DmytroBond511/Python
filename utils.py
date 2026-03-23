def calculate_bonus(salary, experience):
    if 2 <= experience < 5:
        percent = 2
    elif 5 <= experience < 10:
        percent = 5
    elif experience >= 10:
        percent = 10
    else:
        percent = 0

    bonus = salary * percent / 100
    total = salary + bonus

    return percent, bonus, total


def translate(text_key, lang):
    translations = {
        "uk": {
            "language": "Мова: Українська",
            "salary": "Зарплата",
            "experience": "Стаж",
            "bonus_percent": "Надбавка (%)",
            "bonus_amount": "Надбавка (грн)",
            "total": "Всього"
        },
        "en": {
            "language": "Language: English",
            "salary": "Salary",
            "experience": "Experience",
            "bonus_percent": "Bonus (%)",
            "bonus_amount": "Bonus (UAH)",
            "total": "Total"
        }
    }

    if lang not in translations:
        lang = "uk"

    return translations[lang].get(text_key, text_key)