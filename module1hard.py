grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_rating_students = {}
students_ = sorted(students)
for i in range(0, len(students_)):
    average_ball_ = sum(grades[i]) / len(grades[i])
    average_rating_students.update({students_[i]: average_ball_})
print(average_rating_students)
