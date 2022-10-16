principle = float(input("Please enter the principle amount"))

maturity = float(input("Please enter the maturirt of the CD"))

if principle > 100000 and maturity == 5:
  rate = 0.06
elif principle < 100000 and maturity == 10:
  rate = 0.05
elif principle < 100000 and maturity ==5:
  rate = 0.04
else:
  rate = 0.02

first_year = principle * rate
print("principle ", principle)
print("interest rate",rate)
print("interest of the first year", first_year )