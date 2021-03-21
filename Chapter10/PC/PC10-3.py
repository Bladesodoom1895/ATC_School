#Employee class program

#define the class
class Employee:
    #initialize the class
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    #method to set the employee name
    def set_name(self, name):
        self.__name = name

    #method to set the employee id
    def set_id_number(self, id_number):
        self.__id_number

    #method to set the employee department
    def set_department(self, department):
        self.__department = department

    #method to set the employee job title
    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id_number

    def get_department(self):
        return self.__department

    def get_job(self):
        return self.__job_title


#function to get the employee information
def get_info():
    #get employee info from user
    name = input("Enter the employees name: ")
    id_number = int(input("Enter the employee's id number: "))
    department = input("Enter the employee's department: ")
    job_title = input("Enter the employee's job_title: ")
    return name, id_number, department, job_title


def main():
    print("Employee 1")
    #get employee1 information
    name, id_number, department, job_title = get_info()
    #create the instance with the information
    employee1 = Employee(name, id_number, department, job_title)

    print()
    print('Employee 2')
    #get employee2 information
    name, id_number, department, job_title = get_info()
    #create the instance with the information
    employee2 = Employee(name, id_number, department, job_title)

    print()
    print('Employee 3')
    #get employee3 information
    name, id_number, department, job_title = get_info()
    #create the instance with the information
    employee3 = Employee(name, id_number, department, job_title)

    #display the data for employee 1
    print()
    print('The data you entered for employee 1 is: ')
    print('Name: ', employee1.get_name())
    print('ID Number: ', employee1.get_id())
    print('Department: ', employee1.get_department())
    print('Job Title: ', employee1.get_job())

    print()
    print('The data you entered for employee 2 is: ')
    print('Name: ', employee2.get_name())
    print('ID Number: ', employee2.get_id())
    print('Department: ', employee2.get_department())
    print('Job Title: ', employee2.get_job())

    print()
    print('The data you entered for employee 3 is: ')
    print('Name: ', employee3.get_name())
    print('ID Number: ', employee3.get_id())
    print('Department: ', employee3.get_department())
    print('Job Title: ', employee3.get_job())


main()