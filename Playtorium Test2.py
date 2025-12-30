#Item
Tshirt = {
    "Name": "T-Shirt",
    "Category": 'Clothing',
    "price": 350,
}
Hat = {
    "Name": "Hat",
    "Category": 'Accessories',
    "price": 250,
}
Hoodie = {
    "Name": "Hoodie",
    "Category": 'Clothing',
    "price": 700,
}
Watch = {
    "Name": "Watch",
    "Category": 'Accessories',
    "price": 850,
}
Bag = {
    "Name": "Bag",
    "Category": 'Accessories',
    "price": 640,
}
Belt = {
    "Name": "Belt",
    "Category": 'Accessories',
    "price": 230,
}

# Campaigns
Fixed_amount = {
    "Category": "Coupon",
    "type": "Fixed",
    "Discount": 50,
}
Percentage = {
    "Category": "Coupon",
    "type": "Percentage",
    "percentage": 10,
}
PercentagebyItem = {
    "Category": "On Top",
    "type": "Category_Percentage",
    "Category_Filter": "Clothing",
    "Percentage": 15,
}
Discountpoints = {
    "Category": "On Top",
    "type": "points",
    "points": 68,
}
Specialcampaigns = {
    "Category": "Seasonal",
    "type": "Special",
    "X": 300,
    "Y": 40,
}

def fixed(total, Discount):
    return total - Discount
def percentage(total, percentage):
    return total * (1 - percentage / 100)

def category_percentage(cart, Category, percentage):
    discount = 0
    for item in cart:
        if item.get("Category") == Category:
            discount += item.get("price") * (percentage / 100)
    return discount

def points_discount(total, points):
    discount = min(points, total * 0.2)
    return total - discount
    
def specialcampaign_discount(total, X, Y):
    return total - (total // X) * Y

def calculate_final_price(cart, campaigns):
    total = sum(item["price"] for item in cart)
    
    if campaigns["type"] == "Fixed":
        total = fixed(total, campaigns.get("Discount"))
    elif campaigns["type"] == "Percentage":
        total = percentage(total, campaigns.get("percentage"))
    elif campaigns["type"] == "Category_Percentage":
        total -= category_percentage(cart, campaigns.get("Category_Filter"), campaigns.get("Percentage"))
    elif campaigns["type"] == "points":
        total = points_discount(total, campaigns.get("points"))
    elif campaigns["type"] == "Special":
        total = specialcampaign_discount(total, campaigns.get("X"), campaigns.get("Y"))

    return total

cart = [Tshirt, Hat, Belt]
final_price = calculate_final_price(cart, Specialcampaigns)
print("Total Price : {}".format(final_price))