class hrsystem():
    name = ""
    salary = 0
    kpi = 0
    employee = ['Bob','Candy','Jony', "Kelly"]

    @classmethod
    def record(cls):
        cls.name = input("name: ")
        cls.salary = int(input("salary: "))
        cls.kpi = int(input("kpi: "))

    @classmethod
    def print_record(cls):
        if cls.check_name():
            print("It's our employee!")
            print("Here is the information of " + cls.name)
            print("The salary is " + str(cls.salary))
            print("The kpi is " + str(cls.kpi))
            cls.kpi_rating()
        else:
            print("It's not our employee! ")

    @classmethod
    def check_name(cls):
        if cls.name not in cls.employee:
            return False
        else:
            return True

    @classmethod
    def kpi_rating(cls):
        if cls.kpi > 95:
            print("excellent! ")
        else:
            print("Come on! ")

hrsystem.record()
hrsystem.print_record()
hrsystem.check_name()
