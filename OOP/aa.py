sp=int(input())
no_of_varietys=int(input())
total_weight=0
cost_price=0
for i in range(no_of_varietys):
    quantity=int(input())
    price=int(input())
    cost_price+=quantity*price
    total_weight+=quantity
total_selling_price=total_weight*sp
# print(total_weight)
# print(cost_price)

percentage=((total_selling_price-cost_price)/cost_price)*100
print(percentage)
