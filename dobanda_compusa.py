# Calculating Future Values(one period): You have 100 USD today and you save it for one year at an interest rate of 3%

print(100*1.03)
print(100+100*0.03)

# Calculating Future Values(many periods): You have 100 USD today and you save it for three years at an interest rate of 3%

interest_rate=0.03   # 3% dobanda
period=3             # 3 ani
amount=100          # suma depusa

print(100*1.03*1.03*1.03)

print(amount*(1+interest_rate)**period)