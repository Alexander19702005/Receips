#Задание 1
import os

with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}

    for k in file:
        ingredients = []
        recepie_name = k.strip()
        #print(recepie_name)
        ingredients_count = file.readline()
        #print(ingredients_count)

        for p in range(int(ingredients_count)):
            recepie = file.readline().strip().split(' | ')
            product, quantity, weight = recepie
            ingredients.append({'ingredient_name': product, 'quantity': quantity, 'measure': weight})
        file.readline()
    cook_book[recepie_name]=ingredients
    print(cook_book)
    #print(t)
    #print(ingredients)




