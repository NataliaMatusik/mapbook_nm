def read_data(users_data: list) -> None:
    for user in users_data:
        print(
            f'twój znajomy {user['username']} z miejscowosci {user['location']}) opublikowal {user['posts']} wiadomosci. Ostatnia wiadomosc {user['usermessage'][-1]}')

def add_users(users_data: list)->None:

    name=input('podaj imię: ')
    location=input('podaj lokalizacje:')
    posts=int(input('podaj liczbę postów'))
    usermessage=['']
    users_data.append({'username': name, 'location': location, 'posts': posts,
         'usermessage': usermessage})

    def remove_user(users_data: list) -> None:
        name = input('podaj imię użytkownika do usuniecia:')
        for user in users_data:
            if user['username'] == 'name':
                users_data.remove(user)