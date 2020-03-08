#!/bin/python3

if __name__ == '__main__':
    student_marks = {}
    for _ in range(int(input())):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum=0.00
    for element in student_marks[query_name]:
        sum=sum+element #calculate sum
    #store variable till 2 places of decimal
    print('%.2f' % round(sum/len(student_marks[query_name]),2))