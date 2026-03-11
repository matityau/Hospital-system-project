def list_of_dept(departments):
    """"בניתי לולא שעוברת על הרשימה של המחלקות
    ומדפיסה לי אותם בצורה שלכול מחלקה יש מספר """
    count = 1
    for dept in departments:
        print(f"For department {dept} press {count}")
        count += 1
    """בניתי אפשרות בחירה של הלקוח
    ואם הוא מכניס מספר או str לא מהרישמה
    מודפסת הודעה מתיאה וחוזרת האפשרות בחירה"""
    while True:
        choice = int(input("Enter a choice "))
        count = 1
        while count != len(departments) + 1:
            if choice == count:
                return departments[count - 1]
            count += 1
        print("please enter a number from the list")




hospital_departments = [
    "Emergency Room",    # מיון
    "Cardiology",        # קרדיולוגיה
    "Pediatrics",        # ילדים
    "Maternity",         # יולדות
    "Internal Medicine", # פנימית
    "Orthopedics",       # אורטופדיה
    "Oncology",          # אונקולוגיה
    "Intensive Care"     # טיפול נמרץ
]


def write_numbers_list():
    """"הפונקציה יוצרת קובץ טקסט עם מספר בשביל התור.
    אני החלטתי שהמספר הרשוני הוא 10 כי ככה היה בלי"""
    try:
        numbers = 10
        with open("list_of_numbers.txt", "w", encoding="utf-8") as f:
            f.write(str(numbers))

    except Exception as E:
        print(E)

""""בסוף צריך לתת תנאי להפעלה של הפונקציה"""
write_numbers_list()



def numbers_list():
    """"הפונקציה מחזירה את המספר שיש בקובץ טקסט."""
    try:
        with open("list_of_numbers.txt", "r") as f:
            r = f.readlines()
            return r[0]
    except Exception as E:
        print(E)



def new_number(num):
    """"הפונקציה מקבלת את המספר שיש בקובץ טקסט ומוסיפה לו 1+ ."""
    try:
        with open("list_of_numbers.txt", "w") as f:
            n = int(num) + 1
            f.write(str(n))
    except Exception as E:
        print(E)



def queue_number(departments, numbers, dept):
    """"הפונקציה מחזירה מספר תור לפי המחלקה"""

    if dept == departments[0]:
        queue_num = f"A{numbers}"
        new_number(numbers)
        return queue_num

    elif dept == departments[1]:
        queue_num = f"B{numbers}"
        new_number(numbers)
        return queue_num

    elif dept == departments[2]:
        queue_num = f"C{numbers}"
        new_number(numbers)
        return queue_num

    elif dept == departments[3]:
        queue_num = f"D{numbers}"
        new_number(numbers)
        return queue_num

    elif dept == departments[4]:
        queue_num = f"E{numbers}"
        new_number(numbers)
        return queue_num

    elif dept == departments[5]:
        queue_num = f"F{numbers}"
        new_number(numbers)
        return queue_num

    elif dept == departments[6]:
        queue_num = f"G{numbers}"
        new_number(numbers)
        return queue_num

    elif dept == departments[7]:
        queue_num = f"H{numbers}"
        new_number(numbers)
        return queue_num


print(queue_number(hospital_departments, numbers_list(), list_of_dept(hospital_departments)))
