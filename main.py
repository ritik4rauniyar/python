# print("hello python")

# name = 'ram'
# age =34
# address ='ktm'

# print(name)
# print(age)
# print(address)


name =input("Enter name")
print("my name is",name)

print("============Gazzs Traders========")
print("1. Iphone(Rs:50000) 2. Huawei(Rs:45000) 3. HTC (Rs:30000)")
product_name=""
Iphone_price=0
Huawei_price=0
Htcprice=0
quantity=0

option =int(input("Enter quantity: "))
if option==1:
    product_name="Iphone"
    Iphone_price=quantity*50000

elif option==2:
    quantity = int(input("enter quantuty: "))
    product_name= "Huwaei"
    Huawei_price=quantity*45000

elif option==3:
    quantity = int(input("Enter quantity: "))
    product_name= "HTC"
    Htcprice=quantity*30000

else:
    print("Invalid option")
    exit()


print("delivery option: 1. Home(Rs:1000) 2. Pickup(Rs:0)")
delivery_price=0
deivery_option=int(input("Enter delivery option: "))
if deivery_option==1:
    delivery_price=1000

print("packing option 1. plastic bag(Rs:500) 2. Bag(Rs:1000) 3. Gift Box(Rs:5000)")
Packing_price=0
packing_option=int(input("Enter packing option"))
if packing_option==1:
    packing_price=500
elif packing_option==2:
    packing_price=1000
elif packing_option==3:
    packing_price=5000

Total= Iphone_price+ Huawei_price+ Htcprice


print("Location 1. KTM(Rs:13%) tax 2. LTP(FREE) tax 3. BKT(FREE)")
tax_amount=0
location_option=int(input("Enter location option: "))
if location_option==1:
    tax_amount=Total*0.13

grand_total = Total + delivery_price + packing_price + tax_amount
name = input("Enter your name: ")
address = input("enter your address: ")
phone = input("enter your phone number: ") 
print("========Invoice=======") 
print("Name", name)
print("Address", address)
print("Phone", phone)
print("Product", product_name)
print("Qunatity", quantity)
print("Total", Total) 
print("Delivery Price" , delivery_price)
print("Packing Price" , packing_price)
print("Tax Amount", tax_amount)
print("Grand Total", grand_total)
print("======Thank you for shipping with us======")








