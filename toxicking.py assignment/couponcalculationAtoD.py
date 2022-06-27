# function when E is entered
def MultipleResults():
    print("Total money spent: ", sum(PriceSum))
    print("Total coupon", sum(couponSum))
    print("Total spent minus coupon:", sum(PriceSum) - sum(couponSum))


# function for histogram
def DrawHistogram():
    print("Histogram\n")
    print("< £10(0 %): *\n£10 -£60(8 %): ** *\n£61 -£150(9 %): *")
    print("£151 -£210(10 %): *")
    print("> £211(11 % / Cap): *\n\n7 customers")
    
# function for maximum and minimum values
def MinMax():
    print(f"Maximum groceries amount:{max(PriceSum)}")
    print(f"Minimum groseries amount:{min(PriceSum)}")
    print(f"Maximum coupon amount:{max(couponSum)}")
    print(f"Minimum coupon amount:{min(couponSum)}")


print("Welcome to our supermarket")
PriceSum = []
couponSum = []
while 1:
    try:
        price = int(input("input the price of your groceries in £"))
    except:
        print("only an integer value can be inputted")
        exit()
    PriceSum.append(price)
    
    if price == 0:
        print("Cost of groceries should be greater than £0")

    elif price < 10 and price >0:
        print(f"Cost of groceries: {price}")
        print("Less than £10 (No coupon)")
    elif (price >= 10 and price <= 60):
        discount = 0.08 * price
        print(f"Cost of groceries: {price}")
        print(f"Awarded a discount coupon of £{discount} (8% of purchase).")
    elif (price >= 61 and price <= 150):
        discount = 0.09 * price
        print(f"Cost of groceries: {price}")
        print(f"Awarded a discount coupon of £{discount} (9% of purchase)")
    elif (price >= 151 and price <= 210):
        discount = 0.10 * price
        print(f"Cost of groceries: {price}")
        print(f"Awarded a discount coupon of £{discount} (8% of purchase).")
    elif (price >= 211):
        discount = 0.11 * price
        if (discount > 33):
            discount = 33
            print(f"Cost of groceries: {price}")
            print(f"Awarded a discount coupon of £{discount} (11% of purchase (capped))")
    couponSum.append(discount)

    n = input(
        "input 'Y' or 'y' for another transaction:\ninput 'E' or 'e' to check transaction logs\ninput 'N' or 'n' to quit whole process\t")
    if n.strip() == "E" or "e" :
        # multiple results function
        MultipleResults()

        # histogram function
        DrawHistogram()

        # call min and max function
        MinMax()

        break
    if n.strip() == "Y" or "y":
        continue
    if n.strip() == "N" or "n":
        break
    else:
        print("invalid selection")
        break






