price=int(input("enter price:"))

if price>300:
    price=price*0.7
elif price>200 and price<=300:
    price=price*0.8
elif price>100 and price<=200:
    price=price*0.9
elif price>0 and price<=100:
    price=price*0.95
else:
    print("no discount")

print("final price =", price) 