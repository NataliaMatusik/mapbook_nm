import folium
import requests
from bs4 import BeautifulSoup

def read_data(users_data: list) -> None:
    for user in users_data:
        print(
            f'twój znajomy {user['username']} z miejscowości {user['location']} opublikował {user['posts']} wiadomości. Ostatnia wiadomość {user['usermessage'][-1]}')


def add_user(users_data: list) -> None:
    name = input('Podaj imię: ')
    location = input('Podaj lokalizację: ')
    posts = int(input('Podaj liczbę postów: '))
    usermessage = ['']
    users_data.append({'username': name, 'location': location, 'posts': posts,
                       'usermessage': usermessage}, )


def remove_user(users_data: list) -> None:
    name = input('Podaj imię użytkownika do usunięcia: ')

    for user in users_data:
        if user['username'] == name:
            users_data.remove(user)


def update_user(users_data: list) -> None:
    name = input('Podaj imię użytkownika do zmiany: ')

    for user in users_data:
        if user['username'] == name:
            user['username'] = input('Podaj nowe imie: ')
            user['location'] = input('Podaj nową lokalizację: ')
            user['posts'] = int(input('Podaj liczbę postów'))



            users: list = [
                {'username': 'oliwia', 'location': 'Warszawa', 'posts': 1,
                 'usermessage': ['zyczenia1', 'kocham legie1', 'sprzedam opla1', 'kiwi1']},
                {'username': 'ola', 'location': 'Kraków', 'posts': 1,
                 'usermessage': ['zyczenia1', 'kocham legie1', 'sprzedam opla1', 'kiwi1']}
            ]

            def read_data(users_data: list) -> None:
                for user in users_data:
                    print(
                        f'Twój znajomy {user['username']} z miejscowości {user['location']} opublikował {user['posts']} wiadomości. Ostatnia wiadomość {user['usermessage'][-1]}')

            def get_coordinates(location: str) -> list:
                url = f'https://pl.wikipedia.org/wiki/{location}'
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

                response = requests.get(url, headers=headers)

                response_html = BeautifulSoup(response.text, 'html.parser')
                response_html_latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
                response_html_longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
                return [response_html_latitude, response_html_longitude]

            def get_mapa(users_data: list) -> None:

                m = folium.Map([52, 21], zoom_start=6)
                for user in users_data:
                    folium.Marker(
                        location=get_coordinates(user['location']),
                        tooltip="Click me!",
                        popup="Mt. Hood Meadows",
                        icon=folium.Icon(icon="cloud"),
                    ).add_to(m)

                m.save('mapa.html')