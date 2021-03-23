import apiKey
from ApiReader import reader

class Player:
    def __init__(self, id):
        response = reader.get_SUMMONER_BYID_V4(id, apiKey.key)
        self.name = response['name']
        self.id = id
        self.accountId = response['accountId'] 

    def getMastery(self, championId):
        return reader.get_CHAMPION_MASTERY_V4(self.id, championId, apiKey.key)['championPoints']

    def getRank(self):
        response = reader.get_SUMMONER_LEAGUE_V4(self.id, apiKey.key)
        tiers = {'DIAMOND' : 6, 'PLATINUM': 5, 'GOLD': 4, 'SILVER': 3, 'BRONZE': 2, 'IRON': 1}
        divisions = {'I': (4/5), 'II': (3/5), 'III': (2/5), 'IV': (1/5)}
        rank = 0
        for queueType in response:
            tier = queueType['tier']
            division = queueType['rank']
            lp = queueType['leaguePoints']
            rank = max(rank, tiers[tier] + divisions[division] + (lp * (1/5) / 100))
        return rank

    def getWinrate(self):
        games = reader.get_MATCHES_V4(self.accountId, apiKey.key)
        gameIds = []
        sampleSize = 4
        for i in range(1, sampleSize):
            gameIds.append(games['matches'][i]['gameId'])
        wins = 0
        for game in gameIds:
            response = reader.get_MATCH_V4(game, apiKey.key)
            didWin = response['teams'][0]['win'] == 'Win'
            for p in response['participantIdentities']:
                if p['player']['summonerId'] == self.id:
                    if p['participantId']<= 5:
                        if didWin:
                            wins += 1
                    else:
                        if not didWin:
                            wins += 1
        return wins/sampleSize