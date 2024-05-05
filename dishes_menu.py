import os
from pprint import pprint

path = os.path.join(os.getcwd(), 'dishes.txt')

# Задаем словарь с книгой рецептов
cook_book = {}
with open(path, 'r', encoding='utf-8') as f:
    # Через цикл пока имеются строки в файле достаем их в отдельные переменные
    while True:
        dish = f.readline().strip()
        if not dish:
            break
        ingredients_count = f.readline().strip()
        cook_book[dish] = []
        # Формируем готовые словари ингридиентов и включаем их в список блюда, пока эти ингридиенты есть
        while True:
            ing_info = f.readline().strip()
            if ing_info:
                ing_info = ing_info.split(" | ")
                cook_book[dish].append({'ingredient_name': ing_info[0], 'quantity': ing_info[1], 'measure': ing_info[2]}) 
            else: 
                break

def get_shop_list_by_dishes(dishes: list, person_count: int):
    """Функция для определения всех ингридиентов для блюд с учетом количества персон"""
    result = {}
    for dish, ingredients_list in cook_book.items():
        if dish in dishes:
            for ingredient in ingredients_list:
                result[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                         'quantity': int(ingredient['quantity']) * person_count}
    return result


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)