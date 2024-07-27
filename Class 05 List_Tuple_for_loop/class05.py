# data_base : list[tuple[str,str]] = [("Samar", "445"), ("Ahmed", "123"), ("Shah","789")]

# for i in data_base:
#     print(i)

data_base : list[tuple[str,str]] = [("Samar", "445"), ("Ahmed", "123"), ("Shah","789")]

input_user : str = input("Enter Your Name: ")
input_password : str = input("Enter Your Password: ")


for i in data_base:
    user , password = i
    if input_user == user and input_password == password:
        print("valid user")
        break
else:
    print("not found or invalid user name")
