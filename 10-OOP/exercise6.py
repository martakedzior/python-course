# 6▹ Utwórz klasę Pracownik.
#     Pracownik ma stanowisko, wynagrodzenie, imie, nazwisko, staz pracy.
#     Pracownik powinen miec roczne podwyżki wg. dowolnie wymyślonego sposobu liczenia. Pracownik powinen odprowadzać podatek
#     o wysokoci zależnej od swoich zarobków oraz minimalną składkę zdrowotną.
#     Pracownik powinien mieć pole typu boolowskiego zawierające status studenta. Jeśli pracownik jest studentem jego
#     składka zdrowotna wynosi 0%.
#     Wszyscy pracownicy mają wspólną nazwę firmy. Spółgłoski imienia i nazwiska wraz z nazwą firmy .com tworzą adres mailowy.
#     Np.
#     Adam Kowalski Love Python Company
#     email -> smkwlsk@lovepythoncompany.com

class Employee:
    COMPANY = "Love Python Company"

    def __init__(self, job_title, salary, first_name, surname, seniority, is_student):
        self.job_title = job_title
        self.salary = salary
        self.first_name = first_name
        self.surname = surname
        self.seniority = seniority
        self.is_student = is_student

    def yearly_raise(self):
        pass

    def tax(self):
        return self.salary * 0.19

    def health_tax(self):
        if self.is_student:
            health_tax = 0
        else:
            health_tax = 7.75

        return health_tax

    def email(self):
        list_of_letters = ["b","c","d","f","g","h","j","k","m","n","l","p","r","s","t","w","y","z"]
        name = str(self.first_name + self.surname).lower()
        email = ""
        for letter in name:
            if letter in list_of_letters:
                email = email + letter

        return email + "@lovepythoncompany.com"


if __name__ == "__main__":
    marek = Employee("QA Engineer", 10000.00, "Marek", "Kowalski", 2, False)
    print(marek.email())
    print(marek.tax())



