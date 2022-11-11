#correct - 100/100
aircompany_name = input()
tickets_adults = int(input())
tickets_children = int(input())
price_adult = float(input())
service_fee = float(input())
price_child = price_adult * 0.3
price_child += service_fee
price_adult += service_fee
total_price = price_adult * tickets_adults + price_child * tickets_children
profit = 0.2 * total_price

print(f"The profit of your agency from {aircompany_name} tickets is {profit:.2f} lv.")