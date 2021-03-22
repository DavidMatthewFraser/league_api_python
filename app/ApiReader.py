# tiers = ['DIAMOND', 'PLATINUM', 'GOLD', 'SILVER', 'BRONZE', 'IRON']
# divisions = ['I', 'II', 'III', 'IV']

import requests

class ApiReader:
    # API Request Functions
    def get_SUMMONER_V4(name, api_key):
        SUMMONER_V4 = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
        return requests.get(SUMMONER_V4 + name + "?api_key=" + api_key).json()

    def get_LEAGUE_V4(tier, division, page, api_key):
        LEAGUE_V4 = 'https://na1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/'
        return requests.get(LEAGUE_V4 + tier + "/" + division + "?page=" + str(page) + "&api_key=" + api_key).json()

    def get_MATCHES_V4(id, api_key):
        MATCHES_V4 = 'https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/'
        return requests.get(MATCHES_V4 + id + "?api_key=" + api_key).json()

    def get_MATCH_V4(match_id, api_key):
        MATCH_V4 = 'https://na1.api.riotgames.com/lol/match/v4/matches/'
        return requests.get(MATCH_V4 + str(match_id) + "?api_key=" + api_key).json()

    # def format_response(json):
    #     for key,value in json.items():
    #         print(str(key) + ': ' + str(value))