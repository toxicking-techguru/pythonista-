

Grocery_data = 10
discount = 10*0.08
print (f"awarded a discount coupon of",discount,"(8% of purchase)" )
Grocery_data = 14
discount = 14*0.8
print ("awarded a discount coupon of",discount,"(8% of purchase)" )
Grocery_data = 58
discount = 58*0.8
print (f"awarded a discount coupon of",discount,"(8% of purchase)" )
Grocery_data = 62
discount = 62*0.09
print (f"awarded a discount coupon of",discount,"(8% of purchase)" )
Grocery_data = 200
discount = 200*0.1
print (f"awarded a discount coupon of",discount,"(8% of purchase)" )
Grocery_data = 8 
print  (" If less than £10 no coupons ")
Grocery_data = 512
print  (" Awarded a discount coupon  of £33 (cappe)  \t\n")
Total_Grocery_data = 10+14 + 58+ 62+200+8+ 512
print (" Total groceries ",Total_Grocery_data)
Total_discount = 0.8+1.12 + 4.64+ 5.58+20+33
print (" Total discount: ",Total_discount )
Total_groceries=864
Total_discount=65.14
newprice=Total_groceries-Total_discount
print (" Groceries – discount:", newprice )
print ("Histogram")

def histogram( price ):
    for n in price:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
          

        print(output)
histogram([1,3,1,1,1]),(['<£10 (0%)','£10-£60 (8%)','£61-£150 (9%)'])
histogram = [1,3,1,1,1]


print(sum(histogram),"Customers")



