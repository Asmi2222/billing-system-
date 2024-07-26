# function to read the laptops from the text file
def read(filename):
laptop_dict = {}
with open(filename, "r") as file:
for line in file:
specs = line.strip().split(", ")
name, company, price, quantity, processor, graphics = specs
laptop_dict[name] = {
"company": company,
"price": float(price.strip("$")),
"quantity": int(quantity),
"processor": processor,
"graphics": graphics
}
return laptop_dict
filename = "laptop.txt"
laptop_dict = read(filename)
