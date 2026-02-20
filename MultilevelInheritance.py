class User:
    def login(self):
        print("User logged in")

class Employee(User):
    def work(self):
        print("Employee is working")

class Manager(Employee):
    def manage(self):
        print("Manager is managing team")

m = Manager()

m.login()
m.work()
m.manage()