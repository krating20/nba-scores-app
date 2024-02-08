from nba_api.live.nba.endpoints import scoreboard
import json

# Today's Score Board
games = scoreboard.ScoreBoard()

# json
json_string = games.get_json()

data = json.loads(json_string)

# Extract game information

game_info = []

for game in data['scoreboard']['games']:
    game_code = game['gameCode']
    game_status_text = game['gameStatusText']
    home_score = game['homeTeam']['score']
    away_score = game['awayTeam']['score']
    home_team_tricode = game['homeTeam']['teamTricode']
    away_team_tricode = game['awayTeam']['teamTricode']

    game_data = {
        "gameCode": game_code,
        "gameStatusText": game_status_text,
        "homeTeam": {
            "teamTricode": home_team_tricode,
            "score": home_score
        },
        "awayTeam": {
            "teamTricode": away_team_tricode,
            "score": away_score
        }
    }
    game_info.append(game_data)

# Convert the list of game data into JSON format
json_output = json.dumps(game_info, indent=4)

# Print the JSON
print(json_output)
