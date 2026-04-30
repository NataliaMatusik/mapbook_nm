from mapbook_lib.model import users
from mapbook_lib.controller import read_data, add_users, remove_user

while True:
    print('0 - zakoncz program')
    print('1- wyswietl znajomych')
    print('2- dodaj znajomego')
    print('3- usuń znajomego')

    choose=input('wybierz opcje: ')
    if choose =='0':
        break
    if choose == '1':
        read_data(users[1:])
    if choose == '2':
        add_users(users)
    if choose == '3':
        remove_user(users)
