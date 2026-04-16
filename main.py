

users:list=[
    {'username':'oliwia', 'location':'lodz','posts': 1,'usermessage':['zyczenia1','kocham legie1','sprzedam opla1','kiwi1']},
    {'username':'paweł', 'location':'ostroda','posts':2,'usermessage':['zyczenia2','kocham legie2','sprzedam opla2']},
    {'username':'eliza', 'location':'radom','posts': 3,'usermessage':['zyczenia3','kocham legie3']},
    {'username':'filip', 'location':'deblin','posts': 4,'usermessage':['zyczenia4','kocham legie4','sprzedam opla4','kiwi4']},
]

for user in users [1:]:
    print(f'twój znajomy {user['username']} z miejscowosci {user['location']}) opublikowal {user['posts']} wiadomosci. Ostatnia wiadomosc {user['usermessage'][-1]}')


#     twoj znajomy filip z miejscowosci deblin opublikowal 1 post o tresci: zyczenia
