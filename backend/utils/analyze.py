import random

def analyze_image(image_bytes):
    # Здесь будет модель на базе YOLO/CLIP. Пока — мок-оценка
    actions = ["Поездка на велосипеде", "Сортировка отходов", "Посадка дерева"]
    scores = [5, 3, 10]  # Экобаллы за действия
    index = random.randint(0, 2)
    return {
        "action": actions[index],
        "eco_score": scores[index],
        "message": f"Молодец! {actions[index]} принесло {scores[index]} экобаллов."
    }
