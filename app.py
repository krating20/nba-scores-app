from flask import Flask, render_template
from nba_api.live.nba.endpoints import scoreboard

app = Flask(__name__)

@app.route('/')
def index():
    # Today's Score Board
    games = scoreboard.ScoreBoard()

    # Get game information
    games_info = []
    for game in games.get_dict()['scoreboard']['games']:
        # Extract team tricodes
        home_team_tricode = game['homeTeam']['teamTricode']
        away_team_tricode = game['awayTeam']['teamTricode']

        # Format game code
        game_code = f"{home_team_tricode} vs {away_team_tricode}"

        game_info = {
            'gameCode': game_code,
            'gameStatusText': game['gameStatusText'],
            'homeTeam': {
                'teamTricode': home_team_tricode,
                'score': game['homeTeam']['score']
            },
            'awayTeam': {
                'teamTricode': away_team_tricode,
                'score': game['awayTeam']['score']
            }
        }
        games_info.append(game_info)

    return render_template('index.html', games_info=games_info)

if __name__ == '__main__':
    app.run(debug=True)
