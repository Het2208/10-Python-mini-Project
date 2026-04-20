def spiCalculate(grade, credit, n):
    grade_points = {
        "A++": 10, "A+": 9, "A": 8,
        "B+": 7, "B": 6,
        "C+": 5, "C": 4,
        "D+": 3, "D": 2
    }

    total_credit = 0
    earned_weight = 0

    for i in range(n):
        gp = grade_points[grade[i]]
        earned_weight += gp * credit[i]
        total_credit += credit[i]

    spi = earned_weight / total_credit

    print("\n********** SPI Calculation **********")
    print(f"Earned Weight     : {earned_weight}")
    print(f"Total Credits     : {total_credit}")
    print(f"SPI               : {spi:.2f} / 10")
    print("****************************************")


def percentageCalculate(grade, credit, n):
    grade_points = {
        "A++": 10, "A+": 9, "A": 8,
        "B+": 7, "B": 6,
        "C+": 5, "C": 4,
        "D+": 3, "D": 2
    }

    earned_weight = 0
    max_weight = 0

    for i in range(n):
        gp = grade_points[grade[i]]
        earned_weight += gp * credit[i]
        max_weight += 10 * credit[i]  # 10 = max grade

    percentage = (earned_weight / max_weight) * 100

    print("\n********** Percentage Calculation **********")
    print(f"Earned Weight     : {earned_weight}")
    print(f"Max Weight        : {max_weight}")
    print(f"Percentage        : {percentage:.2f}%")
    print("********************************************")


def totalCalculate(grade, credit, n):
    grade_points = {
        "A++": 10, "A+": 9, "A": 8,
        "B+": 7, "B": 6,
        "C+": 5, "C": 4,
        "D+": 3, "D": 2
    }

    total_credit = 0
    earned_weight = 0
    max_weight = 0

    for i in range(n):
        gp = grade_points[grade[i]]
        earned_weight += gp * credit[i]
        max_weight += 10 * credit[i]
        total_credit += credit[i]

    print("\n********** Total Calculation **********")
    print(f"Total Credits     : {total_credit}")
    print(f"Earned Weight     : {earned_weight}")
    print(f"Max Weight        : {max_weight}")
    print(f"Ratio Earned      : {earned_weight}/{max_weight}")
    print("****************************************")


def displayinput(name, grade, credit, n):
    print("********** Input Display ***********")
    print(f"{'Subject name':<15}  {'Grade':<7}  {'Credit':<7}")
    for i in range(n):
        print(f"{name[i]:<15}  {grade[i]:<7}  {credit[i]:<7}")


def main():
    print("********************************")
    print("   Welcome to Spi Calculator")
    print("********************************")

    n = int(input("Enter a Number of Subject (1-10 normally) : "))

    while n <= 0:
        print("Subject count can never be less than 1")
        n = int(input("Enter a Number of Subject (1-10): "))

    name = []
    grade = []
    credit = []

    valid_grades = ["A++", "A+", "A", "B+", "B", "C+", "C", "D+", "D"]
    valid_credit = [1, 2, 3, 4, 5, 6]

    for i in range(n):
        name.append(input(f"\nEnter Name of Subject {i + 1} : "))

        g = input(f"Enter Grade of Subject {i + 1} (A++ to D) : ")
        while g not in valid_grades:
            print("Grade should be like [A++ , A+ , A , B+ , B , C+ , C , D+ , D]")
            g = input(f"Enter Grade of Subject {i + 1} : ")
        grade.append(g)

        c = int(input(f"Enter Credit of Subject {i + 1} (1 - 6) : "))
        while c not in valid_credit:
            print("Credit should be like [1,2,3,4,5,6]")
            c = int(input(f"Enter Credit of Subject {i + 1} : "))
        credit.append(c)

    choiceexit = True
    while choiceexit:
        print("\n*******************************")
        print("1. SPI")
        print("2. Percentage")
        print("3. Total")
        print("4. Display Input")
        print("5. Exit")
        print("*******************************\n")

        ch = int(input("Enter your choice : "))

        match ch:
            case 1:
                spiCalculate(grade, credit, n)
            case 2:
                percentageCalculate(grade, credit, n)
            case 3:
                totalCalculate(grade, credit, n)
            case 4:
                displayinput(name, grade, credit, n)
            case 5:
                choiceexit = False
            case _:
                print("Invalid Choice")

main()
