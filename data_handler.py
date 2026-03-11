import csv
def doctor_category():
    """הפונקציה יוצרת קובץ csv של רופאים"""
    try:
        with open("doctors.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["person_id", "name", "gender", "age", "specialty", "address", "password"])
    except Exception as E:
        print(E)

doctor_category()


def patient_category():
    try:
        """הפונקציה יוצרת קובץ csv של חולים"""
        with open("patients.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["person_id", "name", "gender", "age", "sensitivities", "address"])

    except Exception as E:
        print(E)

patient_category()


"""יש פה שני פונקציות שהם בעצם מתודות שכל אחת צריך להשים ב class המתאים"""
# def save_doctor(self):
#     with open("doctors.csv", "a", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow([self.person_id,self.name, self.gender, self.age, self.specialty, self.address, self.password])



# def save_patient(self):
#     with open("patients.csv", "a", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow([self.person_id,self.name, self.gender, self.age, self.sensitivities, self.address])


def login_details(name, id):
    try:
        with open("doctors.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[1] == name and row[0] == id:
                    password = input("הזן סיסמה")
                    if password == row[-1]:
                        return

        with open("patients.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == name and row[1] == id:
                    return
    except Exception as E:
        print(E)