#shipping
# obtain user country
country = input("Enter your country: ")
province = input("Eter your province: ")

#calculate cost of shipping
shippingCost = 0.0

if country == "Canada" :
    if province == "AB" or province == "BC" :
        shippingCost = 10.0
    else :
        shippingCost = 5.0
else :
    shippingCost = 10.0

print("shipping cost to %s, %s: $%.2f" % (province, country, shippingCost))
