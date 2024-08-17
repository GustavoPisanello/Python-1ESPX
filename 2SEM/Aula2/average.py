def Average():
    students_grades = [(85, 90, 88),
                        (60, 75, 68),
                        (68, 80, 90),
                        (80, 90, 72)];

    students_names = ("Laura", "Paulo", "Ana", "José");
    
    averages = []
    for i in students_grades:
        plus = 0
        for k in i:
            plus += k;
        average = plus / len(students_grades[0]);
        averages.append(str(round(average, 2)))
    averages = tuple(averages)
    data = []

    z = 0
    while z < len(students_names):
        data.append(f"Aluna: {students_names[z]} | Nota: {averages[z]}")
        z += 1
    
    data = tuple(data)    
    return data

print(Average())


