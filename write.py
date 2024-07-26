def write(laptop_dict, filename):
with open(filename, "w") as file:
for name, details in laptop_dict.items():
company = details["company"]
price = "${:.2f}".format(details["price"])
quantity = details["quantity"]
processor = details["processor"]
graphics = details["graphics"]
line = "{}, {}, {}, {}, {}, {}\n".format(name, company, price,

quantity, processor, graphics)
file.write(line)