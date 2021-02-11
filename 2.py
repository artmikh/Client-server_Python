import json

def write_order_to_json(item, quantity, price, buyer, date):
    orders = {}
    with open('orders.json', 'r', encoding='utf-8') as order_file:
        orders = json.load(order_file)
    orders['orders'].append({
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    })

    with open('orders.json', 'w', encoding='utf-8') as json_file:
        json.dump(orders, json_file, indent=4)

write_order_to_json('Телевизор', '5', '10000', 'Кто-то', '10.02.2021')
write_order_to_json('Магнитофон', '2', '5000', 'Другой', '10.02.2021')