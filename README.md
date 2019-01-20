# Flask Marketplace Project

A server side web api that can be used to fetch and purchase products in inventory. 

### Install dependencies
```
pip install -r requirements.txt
```

### Running Flask server
```
python api.py
```

### Testing functionalities
Once the server is running, try visiting the following URLs 

#### View all products in catalog
`http://127.0.0.1:5000/inventory/all`

#### View only **available** products in catalog
`http://127.0.0.1:5000/inventory/available`

#### Make a purchase
To make a purchase: provide the product id and quantity as parameters
Example:
The following endpoint is used to purchase two pairs of mittens (id: W1001 corresponds to mittens -- view catalog)

`http://127.0.0.1:5000/inventory?id=W1001&quantity=2`

