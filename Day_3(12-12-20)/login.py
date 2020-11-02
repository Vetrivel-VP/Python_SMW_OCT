uname = input('Enter the Username:')
pswd = input('Enter the password:')
if uname == 'Sample':
    if pswd == 'Sample@123':
        print(f'Welcome : {uname}, You Logged in successfully')
    else:
        print('Passwrod Mismatch')
else:
    print('Invalid Username')
