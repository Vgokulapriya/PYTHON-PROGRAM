# Track sales data
# Seeing retailer hit their sale traget
# Checking their are product still in stock

stock = int(input())
product_sold = int(input())
target = int(input())

target_hit = product_sold == target
print("hit product sale target:")
print(target_hit)

current_stock = stock - product_sold
in_stock = current_stock != 0
print("product in stock :")
print(in_stock)
