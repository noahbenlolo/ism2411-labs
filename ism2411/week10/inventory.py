#Refelection: 
# 1.The most suprising thing of how lists work is that they are mutable, meaning that they are able to be changed. This is helpful 
#because it allows for the ability to add and remove items from a list.
# 2. When dealing with lists, it can be helpful to use when calculating the monthly sales average. or different types of data that can be stored in a list.

#Exercise #1: Build a list

print("---Exercise 1: Build a list---")
inventory = ["pen","notebook","stapler","tape","marker"]
print(inventory)
print(len(inventory))

#Exercise #2: Index Practice
print("---Exercise 2: Index Practice---")
print(inventory[0]) # always grab the first item
print(inventory[-1]) # always grab the last item

middle = len(inventory) // 2
print(inventory[middle]) # grab the middle item (not hard coded)

print("---Exercise 3: Slicing Practice---")
print(inventory[:3]) # grab the first three items
print(inventory[-2:]) # grab the last two items
print(inventory[::2]) # grabs everyother item in the list

#-- Exercise #4: List Methods--
print("---Exercise 4: List Methods---")
inventory.append("envelope") #adds an item to the end of the list
inventory.append("tape") #adds an item to the end of the list

inventory.remove ("tape") #removes an item from the list
print(inventory)

inventory.sort()
print(inventory) #sorts the list in alphabetical order

# -- Exercise 5: Tuple Expansion --
print("---Exercise 5: Tuple Expansion---")
coords = (40.7128, -74.0060) # New York City coordinates

try:
    coords[0] = 99
except TypeError as error:
    print("Type Error Caught:", error) # Tuples are immutable, cannot change their values
    print("Tuples protect coordinates from being changed by accident.")


#--Exercise 6: List Average Sales --
print("---Exercise 6: List Average Sales---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Average sales: {average}")
print(f"Total sales: {total}")
print(f"Number of sales entries: {count}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

best = sales[0]
worst = sales [0]
for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount
print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}")

#--Exercise 7: Accumulator Pattern --
prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = [] #an empty list to hold the discounted prices
for price in prices:
    discounted.append(round(price * .9, 2)) # apply a 10% discount and round to 2 decimal places
print(prices)
print(discounted)

#--Exercise 8: Filtering--
print("---Exercise 8: Filtering---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for sale in sales:
    if sale > 300:
        high_sales.append(sale)
print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales)}")