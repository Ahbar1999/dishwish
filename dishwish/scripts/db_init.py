from recommender.models import Restaurant, Dish
import csv, json

def run():
    with open('recommender/restaurants_small.csv', newline='') as data:
        reader = csv.reader(data)
        for row in reader:
            if reader.line_num == 1:
                continue
            # print(reader.line_num, row)
            dishes = json.loads(row[3])
            for dish_name in dishes:
                # print(dish_name, dishes[dish_name])
                price = dishes[dish_name]
                try:
                    Restaurant.objects.get(id=int(row[0]))
                except Restaurant.DoesNotExist:
                    Restaurant.objects.create(id=int(row[0]), name=row[1], location=row[2]).save()
                try:
                    Dish.objects.get(name=dish_name)
                except Dish.DoesNotExist:
                    Dish.objects.create(name=dish_name, price=price, restaurant=Restaurant.objects.get(id=int(row[0]))).save()
        print(Restaurant.objects.all().count())
 

