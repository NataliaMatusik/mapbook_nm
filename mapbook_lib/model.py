users: list = [
    {'username': 'oliwia', 'location': 'lodz', 'posts': 1,
     'usermessage': ['zyczenia1', 'kocham legie1', 'sprzedam opla1', 'kiwi1']},
    {'username': 'paweł', 'location': 'ostroda', 'posts': 2,
     'usermessage': ['zyczenia2', 'kocham legie2', 'sprzedam opla2']},
    {'username': 'eliza', 'location': 'radom', 'posts': 3, 'usermessage': ['zyczenia3', 'kocham legie3']},
    {'username': 'filip', 'location': 'deblin', 'posts': 4,
     'usermessage': ['zyczenia4', 'kocham legie4', 'sprzedam opla4', 'kiwi4']},
]
def add_users(users_data: list)->None:


    print(users)
    name=input('podaj imię: ')
    location=input('podaj lokalizacje:')
    posts=int(input('podaj liczbę postów'))
    usermessage=[]
    users.append({'username': name, 'location': location, 'posts': posts,
         'usermessage': usermessage})
    print(users)

add_users(users)
