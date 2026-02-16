item_price = int(input("Enter item price: "))
item_qty = int(input("Enter item quantity: "))
total = item_price*item_qty
if total<=25000:
    discount = total*0.05
elif total<=50000:
    discount = total*0.10
else:
    discount = total*0.20
net_amt = total-discount
print("\nTotal amount:",total,"\nDiscount:",discount,"\nNet amount:",net_amt)
