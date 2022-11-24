import os.path


# Function Created for checking whether the username/email is satisfying the conditions.

def username(value):
    list1 = []
    condition = ['@', '.']
    for i in value:
        list1.append(i)
    if list1[0].isalpha():
        if condition[0] in list1 and condition[1] in list1:
            if ' ' not in list1:
                if list1[(list1.index('@') + 1)] != condition[1]:
                    for i in range((list1.index('@')), len(list1)):
                        if condition[1] == list1[i]:
                            file = open('TEXT.txt', 'r')
                            for j in file:
                                if value not in j:
                                    continue
                                else:
                                    return 'Same username already exists, Please give different username'

                            else:
                                return 'Pass'

                        else:
                            continue
                    else:
                        return '\'.\' IS NOT AFTER \'@\' IN THE USERNAME, PLEASE TRY AGAIN.............'
                else:
                    return '\'.\' IS NOT ALLOWED TO PRESENT AFTER \'@\', PLEASE TRY AGAIN.............'
            else:
                return 'SPACE IS NOT ALLOWED IN USERNAME, PLEASE TRY AGAIN.............'
        else:
            return '\'@\' or \'.\' IS MISSING IN USERNAME, PLEASE TRY AGAIN.............'
    else:
        return 'USERNAME SHOULD START WITH ALPHABET AND SPECIAL CHARACTERS , PLEASE TRY AGAIN.............'


# Function Created for checking whether the password is satisfying the conditions.

def password(p):
    list2 = []
    testCasePassword = 'Pass'
    for i in p:
        list2.append(i)
    if 5 < len(list2) < 16:

        for i in range(0, len(list2)):
            if list2[i].isdigit():
                break
        else:
            return 'No numeric in password, Please try again...'

        for i in range(0, len(list2)):
            if list2[i].isupper():
                break
        else:
            return 'No uppercase letter, Please try again...'

        for i in range(0, len(list2)):
            if list2[i].islower():
                break
        else:
            return 'No lowercase letter, Please try again...'

        for i in range(0, len(list2)):
            if not list2[i].isalnum():
                if list2[i] != ' ':
                    break

        else:
            return 'No special character, Please try again...'

        for i in range(0, len(list2)):
            if list2[i] != ' ':
                continue
            else:
                return 'space not allowed in password, Please try again...'

    else:
        return 'Password length too short or too long, Please try again...'

    if testCasePassword == 'Pass':
        # print('Your password is in correct format')
        return testCasePassword


# Function created to add LOGIN DETAILS in text file:
def login_details_add_in_db(r, i, b, y):
    file = open('TEXT.txt', 'r+')
    file.readlines()
    # file.write('\n')
    file.write(r)
    file.write(',')
    file.write(i)
    file.write(',')
    file.write(b)
    file.write(',')
    file.write(y)
    file.write('\n')
    file.close()
    return 'Your Registration process completed.. Please Login now..'


# Function created for LOGIN:
def login_details_check(t, y):
    file = open('TEXT.txt', 'r+')
    for i in file:
        temp = i.split(',')
        if t == temp[0]:
            temp[-1] = temp[-1].replace('\n', '')
            if y == temp[-1]:
                return 'Pass'
            else:
                return 'Fail'

    else:
        return 'Account not exist..Please Register first..'


# Function created for Security Questions:

def acc_rec_ques(h, y, z):
    file = open('TEXT.txt', 'r')
    for i in file:
        list3 = i.split(',')
        if h == list3[0]:
            if y == list3[1] and z == list3[2]:
                return 'Pass'

            else:
                return 'Your answers for Security questions are Wrong..'


# Function created to Get old Password during FORGET PASSWORD condition:

def get_old_pw(rithi):
    file = open('TEXT.txt', 'r')
    for rithi in file:
        old = rithi.split(',')
        if rithi == old[0]:
            old[-1] = old[-1].replace('\n', '')
            return old[-1]


# Function created to add New Password during FORGET PASSWORD condition:

def add_new_pw(m, y, z):
    with open('TEXT.txt', 'r+') as file:
        total_Datas = file.readlines()
        count = 0
        file.seek(0)
        for i in file:
            if m in i:
                r = total_Datas.index(i)
                count = count + 1
                break
        if count == 1:
            newone = input('Enter new password: ')
            newone_re = input('Re-Enter new password: ')
            if newone == newone_re:
                pwcheck = password(newone)
                if pwcheck == 'Pass':
                    total_Datas[r] = (m + ',' + y + ',' + z + ',' + newone + '\n')
                    file = open('TEXT.txt', 'w+')
                    file.seek(0)
                    file.writelines(total_Datas)
                    file.close()
                    return 'Password successfully updated.. Login now..'
                else:
                    return pwcheck
            else:
                return 'Password mismatching.. Please enter password correctly..'


# REGISTRATION & LOGIN SYSTEM USING PYTHON, FILE HANDLING:


x = input('WHAT YOU WANT TO DO REGISTER / LOGIN TYPE IT ONLY IN (CAPITAL LETTER FORMAT):')

if os.path.exists('TEXT.txt'):
    pass
else:
    f = open('TEXT.txt', 'x')
    f.close()

# Step 1: Registration
if x == 'REGISTER':
    print('Create USERNAME & PASSWORD..')
    print('''Format for USERNAME: 
    1. Create USERNAME with '@' and '.' , but '.' should not be immediate next to '@'.
    2. USERNAME should not start with special characters..''')
    user = input('Enter USERNAME: ')
    o1 = username(user)
    if o1 == 'Pass':
        print(user, 'is valid..')
        print('''
        Format for PASSWORD: 
        1. PASSWORD length should be >5 and <16..
        2. PASSWORD should have Min.1 special character,1 digit,1 Uppercase,1 Lowercase characters atleast.....
        ''')
        passw = input('Enter PASSWORD: ')
        o2 = password(passw)
        if o2 == 'Pass':
            print(passw, 'is valid..')
            print('Please answer the below Security Question for SAFE ACCOUNT RECOVERY in future...')
            acc_rec_1 = input('Enter your Favourite place (in lowercase): ')
            acc_rec_2 = input('Enter your Favourite Color (in lowercase): ')
            if acc_rec_1.islower() == acc_rec_2.islower():
                print(login_details_add_in_db(user, acc_rec_1, acc_rec_2, passw))
            else:
                print('Security answers not in Lowercase.. Please Try again..')
        else:
            print(o2)
    else:
        print(o1)

# Step 2: Login
if x == 'LOGIN':
    print('Enter your USERNAME & PASSWORD for LOGIN..')
    user = input('Enter USERNAME: ')
    passw = input('Enter PASSWORD: ')

    o3 = login_details_check(user, passw)
    if o3 == 'Pass':
        print('LOGIN successful!!..Project is Success..')
    elif o3 == 'Fail':
        print('PASSWORD is wrong..')
        pwcheck1 = int(input('Press 1 for FORGET PASSWORD/Press 2 to Re-try LOGIN: '))
        if pwcheck1 == 1:
            print('Answer the security questions to access your account..')
            acc_rec_1 = input('Enter your Favourite place (in lowercase): ')
            acc_rec_2 = input('Enter your Favourite Color (in lowercase): ')
            op = acc_rec_ques(user, acc_rec_1, acc_rec_2)
            if op == 'Pass':
                print('GREAT... Now you can access your account..')
                a = int(input('Press 1 to get OLD PASSWORD / Press 2 to add NEW PASSWORD: '))
                if a == 1:
                    print('Your OLD PASSWORD is', get_old_pw(user))
                if a == 2:
                    print(add_new_pw(user, acc_rec_1, acc_rec_2))
            else:
                print(op)
        else:
            print('Please go for LOGIN page..')
    else:
        print(o3)