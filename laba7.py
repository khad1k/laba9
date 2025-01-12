class Employee:
    name = 'name'
    id_num = 'id_num'

    def __init__(self, name, id_num):
        self.name = name
        self.id_num = id_num


    def get_info(self):
        return self.name, self.id_num


class Manager(Employee):
    department = 'department'

    def __init__(self, name, id_num, department):
        Employee.__init__(self, name, id_num)
        self.department = department


    def manage_project(self):
        return self.department


class Technician(Employee):
    specialization = 'specialization'

    def __init__(self, name, id_num, specialization):
        Employee.__init__(self, name, id_num)
        self.specialization = specialization


    def _perform_maintenance(self):
        return self.specialization


class TechManager(Manager, Technician):
    employees = []

    def __init__(self, name, id_num, department, specialization):
        Manager.__init__(self, name, id_num, department)
        Technician.__init__(self, name, id_num, specialization)
        self.tech = (name, id_num, department, specialization)


    def add_employee(self, name, id_num, specialization, department):
        TechManager.employees.append((name, id_num, specialization, department))

    def get_team_info(self):
        return TechManager.employees

a = TechManager(1, 2, 3, 4)
a.add_employee(2, 3, 4, 5)
print(TechManager.employees)
print(a.__dict__)


