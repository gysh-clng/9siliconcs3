class Patient:
    def __init__(self,name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_bill_amount(self):
        return self.__bill_amount
    def set_bill_amount(self,bill_amount):
        self.__bill_amount = bill_amount
    def calculate_bill(self):
        return self.__bill_amount
    def patient_type(self):
        print("Patient Type: Regular Patient")

class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.8
    def patient_type(self):
        print("Patient Type: Senior Citizen")

class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85
    def patient_type(self):
        print("Patient Type: PhilHealth Member")

print("Hospital Billing System")
print("-------------------------")
patient1 = Patient("Juan Dela Cruz", 15000.00) # Patient 1 Output
print(f"Patient Name: {patient1.get_name()}")
patient1.patient_type()
print(f"Original Bill: ₱{patient1.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{patient1.calculate_bill():,.2f}")
print("")
patient2 = SeniorPatient("Maria Santos", 15000.00) # Patient 2 Output
print(f"Patient Name: {patient2.get_name()}")
patient2.patient_type()
print(f"Original Bill: ₱{patient2.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{patient2.calculate_bill():,.2f}")
print("")
patient3 = PhilHealthPatient("Pedro Reyes", 15000.00) # Patient 3 Output
print(f"Patient Name: {patient3.get_name()}")
patient3.patient_type()
print(f"Original Bill: ₱{patient3.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{patient3.calculate_bill():,.2f}")
print("-------------------------")