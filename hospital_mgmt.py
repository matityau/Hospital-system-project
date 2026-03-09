import random
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
        while count != 9:
            if choice == count:
                return departments[count - 1]
            count += 1
        print("please enter a number from the list")



def queue_number(departments, numbers, dept):
    """"הפונקציה מחזירה מספר תור לפי המחלקה"""

    if dept == departments[0]:
        queue_num = f"A{numbers}"
        return queue_num

    elif dept == departments[1]:
        queue_num = f"B{numbers}"
        return queue_num

    elif dept == departments[2]:
        queue_num = f"C{numbers}"
        return queue_num

    elif dept == departments[3]:
        queue_num = f"D{numbers}"
        return queue_num

    elif dept == departments[4]:
        queue_num = f"E{numbers}"
        return queue_num

    elif dept == departments[5]:
        queue_num = f"F{numbers}"
        return queue_num

    elif dept == departments[6]:
        queue_num = f"G{numbers}"
        return queue_num

    elif dept == departments[7]:
        queue_num = f"H{numbers}"
        return queue_num




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
numbers_list = random.randint(10,50)
print(queue_number(hospital_departments, numbers_list, list_of_dept(hospital_departments)))
