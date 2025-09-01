menu = {
    "popcorn": 100,
    "soda": 50,
    "candy": 30,
    "nachos": 120,
    "hotdog": 90
}
cart=[]
total=0
for key,value in menu.items():
    print(f"{key:10}:{value:.2f}")
while True:
    food=input("select food to buy or tipe  q to quit: ").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("food is not in the menu!")   
print("\n----- Your Cart -----")
for item in cart:
    print(f"- {item} : ₹{menu[item]}")
    total += menu[item]

print(f"\nTotal Amount to Pay: ₹{total}")
print("Thank you for your order!")
