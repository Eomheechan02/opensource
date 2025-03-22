# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 05:17:37 2025

@author: User
"""

def input_students():
    students = []
    for i in range(5):
        student = {}
        print(f"{i + 1}번째 학생 입력")
        student['id'] = input("학번: ")
        student['name'] = input("이름: ")
        student['english'] = int(input("영어: "))
        student['c_language'] = int(input("C-언어: "))
        student['python'] = int(input("파이썬: "))
        students.append(student)
    return students

def calculate_total_average(students):
    for student in students:
        student['total'] = student['english'] + student['c_language'] + student['python']
        student['average'] = student['total'] / 3
        
def calculate_grade(students):
    for student in students:
        avg = student['average']
        if avg >= 90:
            student['grade'] = 'A'
        elif avg >= 80:
            student['grade'] = 'B'
        elif avg >= 70:
            student['grade'] = 'C'
        elif avg >= 60:
            student['grade'] = 'D'
        else:
            student['grade'] = 'F'    
            
def calculate_rank(students):
    for student in students:
        rank = 1
        for other_student in students:
            if student['total'] < other_student['total']:
                rank += 1
        student['rank'] = rank

def print_students(students):
    print("\n성적관리 프로그램")
    print("=" * 95)
    print(f"{'학번':<15}{'이름':<10}{'영어':<8}{'C-언어':<8}{'파이썬':<8}{'총점':<8}{'평균':<8}{'학점':<6}{'등수':<6}")
    print("=" * 95)
    for student in students:
        print(f"{student['id']:<17}{student['name']:<12}{student['english']:<9}{student['c_language']:<10}{student['python']:<10}{student['total']:<10}{student['average']:<10.2f}{student['grade']:<8}{student['rank']:<6}")
    print("=" * 95)                              
        
def main():
    students = input_students()
    calculate_total_average(students)
    calculate_grade(students)
    calculate_rank(students)
    print_students(students)    
        
if __name__ == "__main__":
    main()
        
        