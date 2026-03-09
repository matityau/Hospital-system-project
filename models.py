
class Person:
    def __init__(self, person_id, name,age):
        self.person_id = person_id
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} (ID: {self.person_id})"


class Patient(Person):
    def __init__(self, person_id, name,age):
        super().__init__(person_id, name,age)
        self.assigned_department = None
        self.status = "Waiting"
        self.medical_notes = ""
        self.queue_number = ""

    def update_status(self, new_status):
        self.status = new_status
        


class Doctor(Person):

    def __init__(self, person_id, name, specialty,age):
        super().__init__(person_id, name,age)
        self.specialty = specialty

    def diagnose(self, patient, decision):

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