from nba_api.live.nba.endpoints import scoreboard
import json

# Today's Score Board
games = scoreboard.ScoreBoard()

# json
data= games.get_dict()

games_info = []
for game in data['scoreboard']['games']:
    game_info = {
        'gameCode': game['gameCode'],
        'gameStatusText': game['gameStatusText'],
        'homeTeam': {
            'teamTricode': game['homeTeam']['teamTricode'],
            'score': game['homeTeam']['score']
        },
        'awayTeam': {
            'teamTricode': game['awayTeam']['teamTricode'],
            'score': game['awayTeam']['score']
        }
    }
    games_info.append(game_info)

# Printing the restructured game information
for game in games_info:
    print(game)
    