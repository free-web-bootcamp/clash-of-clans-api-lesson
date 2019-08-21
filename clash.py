import requests

headers = {
    'authorization': 'Bearer tokengoeshere',
    'Accept': 'application/json'
}


def get_user():
    # this will get an account from the Clash of Clans API
    response = requests.get(
        'https://api.clashofclans.com/v1/players/%2380J99Y8Y', headers=headers)
    user_json = response.json()
    print('Your best trophies were ' + str(user_json['bestTrophies']))


def search_clans():
    # clan search api
    response = requests.get(
        'https://api.clashofclans.com/v1/clans?name=new%20zealand%20gold', headers=headers)
    clan_json = response.json()
    # now to go into items
    for clan in clan_json['items']:
        print(clan['name'] + ' is level: ' + str(clan['clanLevel']))


# these functions will be called
get_user()
search_clans()
