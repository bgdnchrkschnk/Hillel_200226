class ITEmployee:
    equipment = "Laptop"

    def __init__(self, name: str, years_of_experience: int, profession, is_employed: bool):
        # self.name = name
        self.years_of_experience = years_of_experience
        self.profession = profession
        self.is_employed = is_employed
        self.skills = []
        self.department = "IT"

    def cv(self):
        cv: dict = self.__dict__
        cv['equipment'] = self.equipment
        print(cv)


d = {"key": "value"}
d['key_2'] = "value_2"
print(d)





# employee = ITEmployee("Ivan", 2, "AQA", False)
employee_2 = ITEmployee("Oleg", 5, "QA", False)
# employee.equipment = "Desktop"
#
# employee.skills.append("Python")
# employee.skills.append("API")
#
# employee.cv()
employee_2.cv()

employee_2.profession = "DEV"

employee_2.cv()
