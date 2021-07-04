# Importing User Data
import json, hashlib, stdiomask
users=[]
with open('users_data.json', 'r') as file:
    users = json.load(file)


def auth_check(username, password):
    user_exist = list(filter(lambda user: user["username"] == username, users))
    if len(user_exist):
        hash_pass = hashlib.md5(password.encode('UTF-8')).hexdigest()
        pass_check = list(map(lambda user: 1 if user["password"] == hash_pass else 0, user_exist))
        print(pass_check)
        return pass_check[0]
    return -1


def main():
    username = input("Enter username: ")
    password = stdiomask.getpass(mask='*')
    authenticated_user = auth_check(username, password)
    if authenticated_user == 1:
        return 'Welcome!'
    elif authenticated_user == -1:
        return 'I don\'t know you.'
    else:
        return 'Wrong Password, Please Correct It.'


if __name__ == '__main__':
    print(main())