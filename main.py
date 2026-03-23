import json
import os
from utils import calculate_bonus, translate

FILE_NAME = "MyData.json"


def is_valid_data(data):
    try:
        exp = int(data["experience"])
        sal = float(data["salary"])
        return 0 <= exp <= 70 and sal >= 0
    except:
        return False


def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_data():
    if not os.path.exists(FILE_NAME):
        return None

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data = json.load(f)
        if is_valid_data(data):
            return data
    except:
        pass

    return None


def input_data():
    while True:
        try:
            experience = int(input("Введіть стаж (кількість років): "))
            if not (0 <= experience <= 70):
                raise ValueError

            salary = float(input("Введіть розмір зарплати (грн): ").replace(" ", ""))
            if salary < 0:
                raise ValueError

            lang = input("Введіть мову інтерфейсу (uk/en): ").lower()

            return {
                "experience": experience,
                "salary": salary,
                "lang": lang
            }

        except:
            print("Некоректні дані! Спробуйте ще раз.")


def main():
    data = load_data()

    if data is None:
        data = input_data()
        save_data(data)
        print(f"Дані збережено в файл {FILE_NAME}")
        return

    exp = data["experience"]
    sal = data["salary"]
    lang = data.get("lang", "uk")

    percent, bonus, total = calculate_bonus(sal, exp)

    print(translate("language", lang))
    print(f"{translate('salary', lang)}: {sal:.0f} грн. "
          f"{translate('experience', lang)}: {exp} роки.")
    print(f"{translate('bonus_percent', lang)}: {percent}%")
    print(f"{translate('bonus_amount', lang)}: {bonus:.0f} грн")
    print(f"{translate('total', lang)}: {total:.0f} грн")


if __name__ == "__main__":
    main()