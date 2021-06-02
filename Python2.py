import json
price = 50 

x = {
  	"Product name": "Werable Device to trace Covid-19",
  	"Price of the product $i": price,
  	"Delivery": "Free"
  	}

if price < 30:
  raise Exception("Product pricing error- undervalued")

y = json.dumps(x) 
print(y)
