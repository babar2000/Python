# tuple starting from round bracket and its value cannot change
data_base : list[tuple[str,str]] = [("zain","123"),("ali",345),("qasim","789")]
input_user : str = input("Enter user name:")
input_password : str = input("Enter user password:")

for row in data_base:
    user, password = row
    if input_user == user and input_password == password:
    print("Valid User")
    break
else:
    print("Not found or invalid user name")

    
    