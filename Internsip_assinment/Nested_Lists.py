if __name__ == '__main__':
    student_grade=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_grade.append([name,score])
    sorted_score = sorted(list(set(x[1] for x in student_grade)))
    second_student = sorted_score[1]
    
    final_list_low = []
    for student in student_grade:
        if second_student == student[1]:
            final_list_low.append(student[0])
    
    for student in sorted(final_list_low):
        print(student)
