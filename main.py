from logger import logger


@logger(path='logs/cook_logs.log')
def adding_dishes(quantity):
    cook_book = {}
    with open('receptes.txt', encoding='utf-8') as file:
        for i in range(quantity):
            name = file.readline().strip()
            cook_book[name] = []
            for i in range(int(file.readline())):
                dish = file.readline().split('|')
                cook_book[name].append(
                    {'ingredient_name': dish[0].strip(), 'quantity': int(dish[1]), 'measure': dish[2].strip()})
            file.readline()
    return cook_book


@logger(path='logs/shop_list_logs.log')
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = adding_dishes(4)
    products = {}
    for dish in dishes:
        for product in cook_book[dish]:
            product['quantity'] *= person_count
            name = product.pop('ingredient_name')
            if name not in products.keys():
                products[name] = product
            else:
                products[name]['quantity'] += product['quantity']
    return products


if __name__ == "__main__":
    get_shop_list_by_dishes(['Запеченный картофель', 'Фахитос', 'Утка по-пекински'], person_count=2)
