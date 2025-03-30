# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 18:04:27 2025

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

def insert_student(students):
    student = {}
    print("새 학생 입력")
    student['id'] = input("학번: ")
    student['name'] = input("이름: ")
    student['english'] = int(input("영어: "))
    student['c_language'] = int(input("C-언어: "))
    student['python'] = int(input("파이썬: "))
    students.append(student)
    calculate_total_average(students)
    calculate_grade(students)
    calculate_rank(students)
    

def delete_student(students):
    student_id = input("삭제할 학생의 학번을 입력하세요: ")
    for student in students:
        if student['id'] == student_id:
            students.remove(student)
            print(f"학번 {student_id} 학생이 삭제되었습니다.")
            calculate_rank(students)
            return
    print("해당 학번의 학생을 찾을 수 없습니다.")

def search_student(students):
    keyword = input("검색할 학번 또는 이름을 입력하세요: ")
    found_students = [student for student in students if student['id'] == keyword or student['name'] == keyword]

    if found_students:
        print("\n검색된 학생 정보:")
        print("=" * 80)
        for student in found_students:
            print(f"학번: {student['id']}, 이름: {student['name']}, 총점: {student['total']}, 평균: {student['average']:.2f}, 학점: {student['grade']}, 등수: {student['rank']}")
        print("=" * 80)
    else:
        print("해당하는 학생을 찾을 수 없습니다.")

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

def sort_students_by_total(students):
    students.sort(key=lambda x: x['total'], reverse=True)
    print("총점 기준으로 학생들이 정렬되었습니다.")
    calculate_rank(students)

def count_80jumup_students(students):
    count = sum(1 for student in students if student['average'] >= 80)
    print(f"평균 80점 이상인 학생 수: {count}명")

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
        
    while True:
        print("\n메뉴:")
        print("1. 성적 출력")
        print("2. 학생 추가")
        print("3. 학생 삭제")
        print("4. 학생 검색")
        print("5. 총점 기준 정렬")
        print("6. 80점 이상 학생 수 출력")
        print("7. 종료")
        choice = input("선택: ")

        if choice == '1':
            print_students(students)
        elif choice == '2':
            insert_student(students)
        elif choice == '3':
            delete_student(students)
        elif choice == '4':
            search_student(students)
        elif choice == '5':
            sort_students_by_total(students)
        elif choice == '6':
            count_80jumup_students(students)
        elif choice == '7':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 선택하세요.")        
        
        
if __name__ == "__main__":
    main()