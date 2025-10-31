inventory = []

unique_items = set()




item_descriptions = {
    "ключ-карта": "Открывает электронные двери.",
    "нож": "Помогает устранить монстра.",
    "фонарик": "Освещает темные коридоры."
}

enemies = {"монстр-страж"}


rooms = {
    1: "Лабораторная палата",
    2: "Химический коридор",
    3: "Центральный выход"
}


print("=== ПОБЕГ ИЗ ЛАБОРАТОРИИ ===")
print("Вы просыпаетесь в неизвестной лаборатории...")



print("\n--- УРОВЕНЬ 1 ---")
print(f"Локация: {rooms[1]}")
print("Вы заперты. Рядом стол и электронная дверь.")

found_key = False

while True:
    print("\n1 - Осмотреть стол")
    print("2 - Подойти к двери")
    print("3 - Проверить инвентарь")
    choice = input("Ваш выбор: ")

    if choice == "1":
        if not found_key:
            print("Вы нашли ключ-карту!")
            inventory.append("ключ-карта")
            unique_items.add("ключ-карта")
            found_key = True
        else:
            print("На столе больше ничего нет.")
    elif choice == "2":
        if "ключ-карта" in inventory:
            print("Вы открыли дверь и прошли дальше.")
            break
        else:
            print("Дверь заперта. Нужна ключ-карта!")
    elif choice == "3":
        if inventory:
            print("Инвентарь:", ", ".join(inventory))
        else:
            print("Инвентарь пуст.")
    else:
        print("Неверный ввод.")



print("\n--- УРОВЕНЬ 2 ---")
print(f"Локация: {rooms[2]}")
print("Перед вами монстр-страж!")

monster_alive = True

while True:
    print("\n1 - Осмотреть шкафчик")
    print("2 - Атаковать монстра")
    print("3 - Попробовать проскочить")
    print("4 - Проверить инвентарь")

    choice = input("Ваш выбор: ")

    if choice == "1":
        if "нож" not in inventory:
            print("Вы нашли нож! Очень полезно.")
            inventory.append("нож")
            unique_items.add("нож")
        else:
            print("Шкафчик пуст.")
    elif choice == "2":
        if "нож" in inventory:
            print("Вы применили нож и победили монстра!")
            enemies.remove("монстр-страж")
            monster_alive = False
        else:
            print("Монстр убил вас... GAME OVER")
            exit()
    elif choice == "3":
        if monster_alive:
            print("Монстр поймал вас... GAME OVER")
            exit()
        else:
            print("Вы прошли дальше.")
            break
    elif choice == "4":
        print("Инвентарь:", ", ".join(inventory))
    else:
        print("Неверный ввод.")



print("\n--- УРОВЕНЬ 3 ---")
print(f"Локация: {rooms[3]}")
print("Чтобы открыть выход, нужно ввести пароль.")

answers = ('42', '67')

attempts = 3
while attempts > 0:
    guess = input("Введите пароль (подсказка: главный ответ Вселенной): ").lower()
    if guess in answers:
        print("Пароль верный! Вы выбрались наружу!")
        break
    else:
        attempts -= 1
        print("Неверно. Осталось попыток:", attempts)

if attempts == 0:
    print("Вы заблокированы в лаборатории навсегда... GAME OVER")
    exit()



print("\nПОЗДРАВЛЯЮ! Вы успешно сбежали из лаборатории!")
print("Ваш инвентарь:", ", ".join(inventory))
print("Уникальные предметы:", unique_items)

