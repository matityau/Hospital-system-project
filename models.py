
class Person:
    def __init__(self, person_id, name,age,gender,address):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def __str__(self):
        return f"{self.name} (ID: {self.person_id})"


class Patient(Person):
    def __init__(self, person_id, name,age,gender,address,sensitivities):
        super().__init__(person_id, name,age,gender,address)
        self.sensitivities = sensitivities
        self.referrals = []
        self.prescriptions = []
        self.assigned_department = None
        self.status = "Waiting"
        self.medical_notes = ""
        self.queue_number = ""

    def request_medication(self, med_name):
        print(f"Patient {self.name} requested: {med_name}")
        self.prescriptions.append(med_name)

    def get_referral(self, department_name):
        print(f"Referral created for {self.name} to {department_name}")
        self.referrals.append(department_name)


    def update_status(self, new_status):
        self.status = new_status


def diagnose(patient, decision):

    decisions = {
        1: "Discharged Home",
        2: "Local Treatment Given",
        3: "Referred to External Lab/Scan"
    }
    result = decisions.get(decision, "Unknown Decision")
    patient.medical_notes = result
    if decision == 1:
        patient.update_status("Discharged")
    else:
        patient.update_status("Follow-up Required")
    return result


class Doctor(Person):
    def __init__(self, person_id, name, specialty, age,gender,address):
        super().__init__(person_id, name, age,gender,address)
        self.specialty = specialty
        self.password = ""



    def update_password(self, new_password):

        if len(new_password) < 8:
            return False, "הסיסמה קצרה מדי. עליה להכיל לפחות 8 תווים."


        if not any(char.isdigit() for char in new_password):
            return False, "הסיסמה חייבת להכיל לפחות ספרה אחת."

        if not any(char.isupper() for char in new_password):
            return False, "הסיסמה חייבת להכיל לפחות אות אחת גדולה (Upper case)."

        self.password = new_password
        return True, "הסיסמה עודכנה בהצלחה!"

    def add_password(self, password):
        if self.password == "":
            self.update_password(password)
        else:
            print("Password exist i n system")



class Department:

    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.patients_queue = []

    def add_patient(self, patient):
        patient.assigned_department = self.dept_name
        self.patients_queue.append(patient)
        print(f"Patient {patient.name} added to {self.dept_name}")

    def __str__(self):
        return f"Department: {self.dept_name} ({len(self.patients_queue)} patients in queue)"