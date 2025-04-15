# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 02:55:08 2025

@author: User
"""

# 학생 객체를 생성
class Student:
    def __init__(self, student_id, name, english, c_language, python):
        self.student_id = student_id
        self.name = name
        self.english = english
        self.c_language = c_language
        self.python = python
        self.calculate_total_average()
        self.calculate_grade()
        self.rank = 1

# 총점과 평균 계산
    def calculate_total_average(self):
        self.total = self.english + self.c_language + self.python
        self.average = self.total / 3

# 점수에 따라 학점 계산
    def calculate_grade(self):
        if self.average >= 90:
            self.grade = 'A'
        elif self.average >= 80:
            self.grade = 'B'
        elif self.average >= 70:
            self.grade = 'C'
        elif self.average >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

# 학생 정보 출력
    def print_info(self):
        print(f"{self.student_id:<15}{self.name:<10}{self.english:<8}"
              f"{self.c_language:<8}{self.python:<8}{self.total:<8}"
              f"{self.average:<8.2f}{self.grade:<6}{self.rank:<6}")


# 학생 성적 관리 및 기능을 제공하는 클래스
class GradeManager:
    def __init__(self):
        self.students = []

# 지정된 수만큼 학생 정보를 입력받아 등록
    def input_students(self, count=5):
        for i in range(count):
            print(f"\n{i + 1}번째 학생 입력")
            student_id = input("학번: ")
            name = input("이름: ")
            english = int(input("영어: "))
            c_language = int(input("C-언어: "))
            python = int(input("파이썬: "))
            student = Student(student_id, name, english, c_language, python)
            self.students.append(student)
        self.calculate_ranks()

# 새로운 학생 정보 추가
    def insert_student(self):
        print("\n새 학생 입력")
        student_id = input("학번: ")
        name = input("이름: ")
        english = int(input("영어: "))
        c_language = int(input("C-언어: "))
        python = int(input("파이썬: "))
        student = Student(student_id, name, english, c_language, python)
        self.students.append(student)
        self.calculate_ranks()

# 학생 정보 삭제
    def delete_student(self):
        student_id = input("\n삭제할 학생의 학번을 입력하세요: ")
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"학번 {student_id} 학생이 삭제되었습니다.")
                self.calculate_ranks()
                return
        print("해당 학번의 학생을 찾을 수 없습니다.")

# 학생 정보 검색
    def search_student(self):
        keyword = input("\n검색할 학번 또는 이름을 입력하세요: ")
        found = [s for s in self.students if s.student_id == keyword or s.name == keyword]

        if found:
            print("\n검색된 학생 정보:")
            print("=" * 80)
            for student in found:
                student.print_info()
            print("=" * 80)
        else:
            print("해당하는 학생을 찾을 수 없습니다.")

# 학생들을 총점 기준으로 정렬
    def sort_students_by_total(self):
        self.students.sort(key=lambda x: x.total, reverse=True)
        self.calculate_ranks()
        print("\n총점 기준으로 학생들이 정렬되었습니다.")

# 학생들의 등수 계산
    def calculate_ranks(self):
        for student in self.students:
            student.rank = 1
            for other in self.students:
                if student.total < other.total:
                    student.rank += 1

# 평균 80점이상 학생수 출력
    def count_80jumup_students(self):
        count = sum(1 for student in self.students if student.average >= 80)
        print(f"\n평균 80점 이상인 학생 수: {count}명")

# 학생들의 성적 정보 출력
    def print_students(self):
        print("\n성적관리 프로그램")
        print("=" * 95)
        print(f"{'학번':<13}{'이름':<8}{'영어':<7}{'C-언어':<6}{'파이썬':<6}"
              f"{'총점':<6}{'평균':<6}{'학점':<4}{'등수':<5}")
        print("=" * 95)
        for student in self.students:
            student.print_info()
        print("=" * 95)

# 프로그램 시행 및 메뉴 표시와 실행
    def run(self):
        self.input_students()
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
                self.print_students()
            elif choice == '2':
                self.insert_student()
            elif choice == '3':
                self.delete_student()
            elif choice == '4':
                self.search_student()
            elif choice == '5':
                self.sort_students_by_total()
            elif choice == '6':
                self.count_80jumup_students()
            elif choice == '7':
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 선택입니다. 다시 선택하세요.")


if __name__ == "__main__":
    manager = GradeManager()
    manager.run()
