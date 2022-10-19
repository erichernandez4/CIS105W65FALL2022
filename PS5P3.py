counter = 0

total_exams1 = 0.0

response = input("Do you want to start this program (yes or no)")

while response == "yes":
  counter = counter + 1 
  last_name = (input("enter student last name "))
  score1 = float(input("enter the 1st exam score "))
  score2 = float(input("enter the 2nd exam score "))
  average_score = (score1 + score2)/2
  print(last_name, " has an average of ",average_score )
  total_exams1 = total_exams1 + score1
  response = input("Do you want to start this program (yes or no)")

avgex1 = total_exams1 / counter
print("number of students ", counter)
print("average exam score 1", avgex1)