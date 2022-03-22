"""Sample code for Chapter 2 string content."""

# String Concatenation
first_name = "Guido "
last_name = "van Russom"
print(first_name + last_name)
count = 1.9
count_text = str(count)
print(type(count_text), first_name + count_text)

# String Methods
sea = "Atlantic Ocean"
print(sea.lower())
sea = sea.upper()
print(sea)
print(sea.isupper())

sea = "Atlantic Ocean"
loc = sea.find("an")
print(loc, sea[:loc], sea[loc:])

sea = "Atlantic            Ocean"
words = sea.split()
print(words)
csv_words = ",".join(words)
print(csv_words)

# String Formatting
price = 350
tax = 0.07
output = "price = {}, tax = {}".format(price, tax)
print(output)

output = "tax = {1}, price = {0}".format(price, tax)
print(output)

output = "cost = ${:7.2f}".format(price + price * tax)
print(output)

price = 350
tax = 0.07
output = "price = {p}, tax = {t}".format(p=price, t=tax)
print(output)
output = "cost = ${cost:7.2f}".format(cost=price + price * tax)
print(output)

# Formatted String Literals
price = 350
tax = 0.07
output = f"£{price} £{tax} cost = £{price + price * tax:7.2f}"
print(output)

# Keyboard Input
years = input("Enter your age in years --> ")
ageindays = 365.25 * float(years)
print("Your age in days is {a:6.0f}".format(a=ageindays))
