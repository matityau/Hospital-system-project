import csv
def login_details(name, id):
    try:
        with open("doctors.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == name and row[1] == id:
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