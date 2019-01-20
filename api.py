from flask import Flask, request, jsonify

app = Flask(__name__)

#sample inventory data (for testing purposes)
products = [
    {'id': 'W1000',
    'title': 'lip balm',
    'price': 3.99,
    'inventory_count': 100},
    {'id': 'W1001',
    'title': 'mittens',
    'price': 8.99,
    'inventory_count': 50},
    {'id': 'W1002',
    'title': 'scarf',
    'price': 30.00,
    'inventory_count': 20},
    {'id': 'F1000',
    'title': 'ultraboost sneakers',
    'price': 170.00,
    'inventory_count': 0}
]

@app.route('/') #route() binds a URL to a function
def home():
    return "Welcome to Christina's Marketplace!"

#query all products
@app.route('/inventory/all', methods=['GET'])
def all_products():
    return jsonify(products)

#query available products
@app.route('/inventory/available', methods=['GET'])
def available_products():
    result = []
    for prod in products:
        if prod['inventory_count'] > 0:
            result.append(prod)
    return jsonify(result)

@app.route('/inventory', methods=['GET'])
def purchase():
    if 'id' in request.args:
        id = request.args['id']
    else:
        return "Error: No id field provided. Please specify a product id."
    
    if 'quantity' in request.args:
        quantity = int(request.args['quantity'])
    else:
        return "Error: No quantity field provided. Please specify a product purchase quantity."
    
    for prod in products:
        if prod['id'] == id and prod['inventory_count'] > 0:
            quantity_purchased = min(prod['inventory_count'],quantity)
            prod['inventory_count'] -= quantity_purchased
            return "PURCHASED Item: {}, Quantity: {}".format(prod['title'],quantity_purchased)
    return "Sorry, item id: {} is currently sold out.".format(id)

if __name__ == '__main__':
    app.debug = False
    app.run()