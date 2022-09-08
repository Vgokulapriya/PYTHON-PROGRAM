# shipping cost calculator

international_shipping = True

total = int(input("Enter the total:"))
shipping_cost = int(input("Enter the shipping cost:"))

if international_shipping:
    shipping_cost += 15
    print("International base cost applied")

if total <= 50:
    shipping_cost += 20
elif total <= 100:
    shipping_cost += 15
else:
    shipping_cost += 5 
print(f"shipping cost:{shipping_cost}")          
 