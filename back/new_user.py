from read_data import read_data
from index import index

class new_user:
    # def new_user(n):
    #     a = {}
    #     print("System--> Adding new store admin")
    #     new_username = input("System--> Enter the new username: ")
    #     new_password = input("System--> Password for new user: ")
    #     a[new_username] = new_password
    #     read_data.editdata(a, n)

    def new_user(n, z,database):
        a = {}
        print("System--> Adding new store admin")
        print("System--> Enter the new username:")
        while True:
            new_username = input("{}--> ".format(z))
            if new_username in database:
                print("\nSystem--> User Already exist in Database")
                print('System--> Please enter a new user')
            elif new_username is 'exit':
                index.start()
            else:
                break
        print("System--> Password for new user:")
        new_password = input("{}--> ".format(z))
        a[new_username] = new_password

        read_data.editdata(a, n)
        return a
