import datetime
# function to generate unique bill name
def generate_bill_name(transaction_type):
now = datetime.datetime.now()
timestamp = now.strftime("%Y%m%d%H%M%S")
return "{}_{}.txt".format(transaction_type, timestamp)
# function to calculate VAT amount
def calculate_vat(total_amount):
vat_rate = 0.13
return total_amount * vat_rate