# -- Self Assessment --
#1. The first thing that I noticed was that the colon was not at the end of the for loop, 
# So I fixed that. But after I ran the code again, and I received an inxex error which led me to look at line 16, 
# and then I asked AI to explain what was wrong and it made me realize that lists are looked at starting from 0 and 
# the the list is only 5 items long, and it was trying to deliver a 6th item which was not there. So I changed the code to < instead of <= and it worked.
# After I ran the code again and realizd that the total was = to $90 instead of the total from the whole list,
# So what I did was look for the total function and realized that it wasnt adding together and to do that you need to add
# the + sign in front of the = sign to add all items together. 
# 2. Looking at the apply_discount function it is a function that looks at the parameters of the clients tier, 
# and if the client is gold member, it applies a 15% discount, then it checks if client is silver then applies 10% discount
# the if client is bronze it applies a 5% discount, and if they do not have a tier or it is anything ELSE, it applies no discount.
#3. No I did not use AI except for exercise 5 which we needed to ask AI for traceback and to figure out what was wrong, and 
# yes, although it helped me figure out what was wrong, it shortcut my information as I did not keep trying to exactly debug and figure out where the problem was. 
# Instead I asked where the problem is and it explained why the problem was what it was and, gave me the thinking to fix it.

# --Exercise #1 --
def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# # --Exercise #2 --
def apply_discount(price,tier):
    if tier == "gold":
        return price * 0.85  # 15% discount
    elif tier == "silver":
        return price * 0.90  # 10% discount
    elif tier =="bronze":
        return price * 0.95  # 5% discount
    else:
        return price  # no discount

original_price = 200
for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# # Notes: conditionals inside function, function inside of the loop

# # --Exercise #3 --
def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200, 0.07, 'gold') =  ${final_price(200, 0.07, 'gold'):.2f}") 

# --Exercise #4 -- 
orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]
for price, tier in orders:
    total = final_price(price, .07, tier)
    print(f"Order of ${price} with {tier} tier: Total = ${total:.2f}")

# -- Exercise #5 --
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale #looking over here wihtout the + sign in front of the = it only takes the last item out of the list and prints it but the + signs takes each item and adds it together to show the proper total of the list. 
print(f"Total: ${total}")

count = 0
for sale in sales: #SyntaxError: I need to put the colon at the end of the for loop to show how it is not connected to code in the block.
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): #the fix to the problem, since it counts from 0 to 5, but the list is <= 5 so it doesnt have a 5 th positionso it now will stop at position 4 with it being < symbol
    print(sales[i]) #IndexError: 
    i += 1


# -- Exercise #6 -- 
x = 100 # global x 

def double_it():
    x = 999 # local x
    return x *2

print(x)
print(double_it())
print(x)