from operations import *
import datetime
from write import *
# function to handle the purchase of laptops from manufacturer
def purchase(laptop_dict):
purchased_laptop = []
net_amount = 0
while True:
name = input("Enter the name of the laptop you want to purchase or type
'e' to exit: ")
# Exit the loop if user types 'e'
if name == 'e':
break
# Check if the laptop is in the store
if name not in laptop_dict:
print("Laptop not found.")
continue
# Get the quantity of laptops to be purchased
quantity = int(input("Enter the quantity to purchase: "))
# Check if the quantity is valid
if quantity <= 0:
print("Invalid quantity.")
continue

# Get the price of the laptop
price = laptop_dict[name]["price"]

net_amount = net_amount + price * quantity
print(name,net_amount)

# Update the quantity of laptops in the store
laptop_dict[name]["quantity"] += quantity
# Write the updated laptop details to the file
write(laptop_dict, "laptop.txt")
# Add the purchased laptop details to the list
purchased_laptop.append({
"name": name,
"company": laptop_dict[name]["company"],
"quantity": quantity,
"price": laptop_dict[name]["price"]
})
vat = calculate_vat(net_amount)
gross_amount = net_amount + vat
# Display the total amount and VAT
print("Total amount (without VAT): ${:.2f}".format(net_amount))
print("VAT (13%): ${:.2f}".format(vat))
print("Total amount (with VAT): ${:.2f}".format(gross_amount))
# Generate bill if any laptops were purchased
if purchased_laptop:
bill_name = generate_bill_name("purchase")
# Write bill to file
with open(bill_name, "w") as file:
file.write("Ash Laptop Land\n")
file.write("Kupondol, lalitpur\n")
file.write("Phone No:9851045654\n")
file.write("\n")
file.write("Date: {}\n".format(datetime.datetime.now().strftime("%Y-

%m-%d %H:%M:%S")))

file.write("\n")
file.write("---------------------------------------------------------

------------------------------")
file.write("\n")
file.write("{:<20}{:<15}{:<15}{:<10}\n".format("Name", "Company",

"Quantity", "Price"))
file.write("\n")
file.write("---------------------------------------------------------

------------------------------")
file.write("\n")
for laptop in purchased_laptop:
file.write("{:<20}{:<15}{:<15}{:<10}\n".format(laptop["name"],

laptop["company"], laptop["quantity"], laptop["price"]))

file.write("\n")
file.write("{:<20}{:<15}{:<15}{:<10}\n".format("", "", "Subtotal:",

net_amount))

file.write("{:<20}{:<15}{:<15}{:<10}\n".format("", "", "VAT (13%):",

vat))

file.write("{:<20}{:<15}{:<15}{:<10}\n".format("", "", "Total:",

gross_amount))
print("Bill generated at: {}".format(bill_name))
