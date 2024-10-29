# user = {'username': 'john'}

# def registration_of_user():
#     user['username'] = input('enter your user name ')
#     if user == user:
#         print ('username already exist')
#         user['username'] = input('enter a new username ')
#         return
#         user['password'] = input('enter password ')
#     else:
#         print('registration done')
    
# registration_of_user()

# user = {'username' : 'john'}

# def registration_of_user():
#     username = input('enter your username ')
#     if username == user:
#         print('user name already exist')
#     else:
#         password = input('enter password ')
#         return(print('registration successfull'))

# registration_of_user()

# def shape():
#     numbers = [5, 2, 5, 2]
#     for style in numbers:
#         (print('x' * style))

# shape()

# def form_letters_with_numbers():
#     numbers = [5, 2, 5, 2]
#     for x_count in numbers:
#         outfit = ''
#         for count in numbers:
#             outfit = 'x'
#             print('x' * x_count)

# form_letters_with_numbers()


'''user login, signup'''
user = {
    # 'user_name' : {
    #     'full_name': 'neme john',
    #     'password': '9118166837'
    # }
}

def register():
    user_name = input('enter a user name ')
    if user_name in user:
        print('pick another name')
        return
    
    full_name = input('enter your user name ')
    password_1 = input('enter your password ')
    user[user_name] = {'fullName': full_name, 'password': password_1}
    print('you have successfully registered')
    print(user)


#login function
def login():
    if not user:
        print('user has not registered')
        return
    userName = input('enter your user name ')
    password = input('enter your password ')
    if user.get(userName) and user[userName]['password'] == password:
        print (f'welcome back {user[userName]['fullname']}')


def main():
    current_user = None
    while True:
        print('\n option = register, login, quit')
        choice = input('input an option ').lower()

        if choice == 'register':
            register()
        elif choice == 'login':
            login()
        elif choice == 'quit':
            ('stopping program')
            break
        else:
            print('invalid input')

main()



