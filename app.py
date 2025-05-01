from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = 'd3ef7dd97626be8c185409d60b469c68'
BASE_URL = 'https://v3.football.api-sports.io'

HEADERS = {
    'x-apisports-key': API_KEY
}

ARSENAL_TEAM_ID = 42  # Arsenal F.C.

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team')
def get_team_info():
    url = f"{BASE_URL}/teams?id={ARSENAL_TEAM_ID}"
    response = requests.get(url, headers=HEADERS)
    data = response.json()

    team = data['response'][0]['team']
    venue = data['response'][0]['venue']
    return render_template('team.html', team=team, venue=venue)

@app.route('/fixtures')
@app.route('/fixtures')
def get_team_fixtures():
    url = f"{BASE_URL}/fixtures?team={ARSENAL_TEAM_ID}&next=5"
    response = requests.get(url, headers=HEADERS)
    
    # Print the response to check if it's correct
    print(response.json())
    
    data = response.json()
    fixtures = data['response']
    return render_template('fixtures.html', fixtures=fixtures)

@app.route('/standings')
def get_team_standings():
    url = f"{BASE_URL}/standings?league=39&season=2023"
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    standings = data['response'][0]['league']['standings']
    return render_template('standings.html', standings=standings)

@app.route('/livescores')
def get_live_scores():
    url = f"{BASE_URL}/fixtures?live=all"
    response = requests.get(url, headers=HEADERS)
    
    # Print response for debugging purposes
    print(response.json())
    
    data = response.json()
    live_scores = data['response']
    
    return render_template('livescores.html', live_scores=live_scores)


if __name__ == '__main__':
    app.run(debug=True)
