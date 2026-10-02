students = {
    "alice": [92, 88, 95],
    "bob": [75, 80, 70],
    "charlie": [55, 62, 58],
    "diana": [100, 98, 97],
    "ethan": [83, 79, 85],
}


def main():
    while True:
        print("1. Look up a student\n2. Print class summary\n3. Add a student\n4. Quit")
        choice = int(input("Choice: "))
        if choice == 1:
            lookup()
        elif choice == 2:
            summary()
        elif choice == 3:
            adding()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid number!")


def lookup():
    student = input("Student name: ").lower()
    if student in students:
        scores = students[student]
        avg = average(scores)
        print(f"Average: {avg:.1f}")
        print(f"Letter grade: {letter_grade(avg)}")
        print(f"Status: {status(avg)}")
    else:
        print("Student not found!")


def average(scores):
    return sum(scores) / len(scores)


def letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def status(avg):
    if avg >= 70:
        return "PASS"
    else:
        return "FAIL"


def summary():
    total = 0
    for student, scores in students.items():
        avg = average(scores)
        print(f"{student}: {avg:.1f} ({letter_grade(avg)})")
        total += avg
    print(f"Class average: {total / len(students):.1f}")


def adding():
    name = input("New student's name: ").lower()
    if name in students:
        print("Student already exists!")
    else:
        scores = []
        for i in range(3):
            score = int(input(f"Score {i + 1}: "))
            scores.append(score)
        students[name] = scores


main()
