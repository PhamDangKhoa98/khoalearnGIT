'''hot= False
cold=True
if hot:
    print("At home")
elif cold:
    print("Eat Cream")
else:
    print("Go to school")
print("SO HOT")
'''
PriceHouse=1000000
GoodCredit= True
Score=7
if GoodCredit:
    KPriceHouse=0.1*PriceHouse
else:
    KPriceHouse=0.2*PriceHouse

print(f"House's Price is {KPriceHouse}")
if PriceHouse<10:
    print("Ngheo qua")
else:
    print("gia ngheo gia kho")

if GoodCredit and (Score>9):
    print("xung dang co 10 nguoi yeu")
if not(Score>9):
    print("Chua gioi lam dau")
