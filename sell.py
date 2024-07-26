from operations import *
from write import *
import datetime

def sell(laptop_dict):
total_net = 0
shipping_cost = 0
tname = []
tcompany = []
tquantity = []
tunit = []
tprice = []
sell=[]
tflag = 0
gross_amount = 0
while True:
# Ask for laptop name to sell or 'e' to exit
name = input("Enter the name of the laptop you want to sell or type 'e'
to exit: ")
# Exit the loop if user enters 'e'
if name == 'e':
break
# Check if laptop is available in the stock
if name not in laptop_dict:
print("Laptop not found.")
break

# Ask for quantity of laptops to sell
quantity = int(input("Enter the quantity to sell: "))
# Check if quantity is less than zero
if quantity <= 0:
print("Invalid quantity.")

# Check if quantity is in the stock
if quantity > laptop_dict[name]["quantity"]:
print("We dont have that many quantity in stock.")
else:
tflag = 1
price = laptop_dict[name]["price"]
net_amount = price * quantity

tname.append(name)
tcompany.append(laptop_dict[name]["company"])
tquantity.append(quantity)
tunit.append(price)
tprice.append(net_amount)
total_net += net_amount

more_item = input("\nDo you want more laptops? (y/n): ")
if more_item == "n":
break

# Add shipping cost to gross amount if user wants
if tflag == 1:
shippingcost=input("do you want to ship? (y/n) : ")
if shippingcost == "y" :
shipping_cost = 20
gross_amount = total_net + shipping_cost
c_name = input("Enter your name : ")
phoneFlag = True
while phoneFlag:
try:
c_phone = int(input("Enter your phone number : "))
phoneFlag = False
except:
print("Please enter a valid numeric phone number")
print("\n")
c_address = input("Enter your address : ")
c_pay = input("Enter your payment method : ")
# Display customer bill with details
print(f"-"*20)
print("Customer invoice:")
print("Customer Name: {}".format(c_name))
print("Phone no. : {}".format(c_phone))
print("Address: {}".format(c_address))
print("Payment method {}".format(c_pay))
c = 0

print(f"\n")
print(f"-"*20)
print(f"\n")
print(f"Name: \tCompany: \t Quantity: \tUnit Price ($): \tNet Price: \t")
for name in tname:
print(f"\n{name}\t {tcompany[c]}\t {tquantity[c]} \t ${tunit[c]}

\t{tprice[c]} \n")

laptop_dict[name]["quantity"] = laptop_dict[name]["quantity"] -

tquantity[c]
c+=1
print(f"Total amount: ${total_net}")
print(f"Shipping Cost: ${shipping_cost}")
print(f"Total amount: ${total_net+shipping_cost}")
# Write updated stock to file
write(laptop_dict, "laptop.txt")

# Generate bill name
bill_name = generate_bill_name("sale")
# Write bill to file
with open(bill_name, "w") as file:
file.write("Ash Laptop Land\n")
file.write("Kupondol, lalitpur\n")
file.write("Phone No:9851045654\n")
file.write("\n")
file.write("Date:

{}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

file.write("\n")
file.write("Customer Name: {}\n".format(c_name))
file.write("Phone no. : {}\n".format(c_phone))
file.write("Address: {}\n".format(c_address))
file.write("Payment method {}\n".format(c_pay))
file.write("\n")
file.write("-----------------------------------------------------

----------------------------------")
file.write("\n")
file.write("{:<20}{:<15}{:<15}{:<10}\n".format("Name", "Company",

"Quantity", "Price"))

file.write("-----------------------------------------------------

----------------------------------")

c=0
for name in tname:
file.write("\n")
file.write("{:<20}{:<15}{:<15}{:<10}\n".format(name,

tcompany[c], tquantity[c], tprice[c]))
file.write("\n")
file.write("{:<20}{:<15}{:<15}{:<10}\n".format("", "",

"Subtotal:", total_net))

file.write("{:<20}{:<15}{:<15}{:<10}\n".format("", "", "Shipping

Cost:", shipping_cost))

file.write("{:<20}{:<15}{:<15}{:<10}\n".format("", "", "Total:",

gross_amount))

file.write("\t thank you for shoping with us")
print("Bill generated at: {}".format("bill.txt"))
print("Thank you for doing business with us.")
