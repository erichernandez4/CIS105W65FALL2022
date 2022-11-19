def exams(exam1,exam2,exam3):
    total_points = exam1 + exam2 + exam3
    average=  total_points / 300
    
    return total_points, average




last_name = input("Please enter your last name ")
exam1 = float(input("Please enter your exam score "))
exam2 = float(input("Please enter your exam score "))
exam3 = float(input("Please enter your exam score "))
total_points,average = exams(exam1,exam2,exam3)


print(last_name)
print("This is the total points of all scores", total_points)
print("These are the average scores ", average)