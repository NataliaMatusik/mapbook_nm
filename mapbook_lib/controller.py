def read_data(users_data: list) -> None:
    for user in users_data:
        print(
            f'twój znajomy {user['username']} z miejscowosci {user['location']}) opublikowal {user['posts']} wiadomosci. Ostatnia wiadomosc {user['usermessage'][-1]}')

