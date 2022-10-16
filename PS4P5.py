last_name = input("Please enter your last name")

salary = float(input("Please enter your salary"))

job_level = float(input("Please enter your job level"))

if job_level >= 10:
  br = 0.25
elif job_level > 9 or job_level > 5:
  br = 0.20
else:
  br = 0.10

bonus = br * salary

print(last_name)
print("This is your bonus", bonus)