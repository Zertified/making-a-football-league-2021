import requests
import json

API_KEY = 'fdd49bbd-0cc2-42c4-beab-909953923df9'

clubs_string = '''

{"count":20,"count_total":810,"page":1,"page_total":41,"items_per_page":20,"items":[{"id":1,"name":"Arsenal","league":13},{"id":2,"name":"Aston Villa","league":14},{"id":3,"name":"Blackburn Rovers","league":14},{"id":4,"name":"Bolton Wanderers","league":14},{"id":5,"name":"Chelsea","league":13},{"id":7,"name":"Everton","league":13},{"id":8,"name":"Leeds United","league":14},{"id":9,"name":"Liverpool","league":13},{"id":10,"name":"Manchester City","league":13},{"id":11,"name":"Manchester United","league":13},{"id":12,"name":"Middlesbrough","league":14},{"id":13,"name":"Newcastle United","league":13},{"id":14,"name":"Nottingham Forest","league":14},{"id":15,"name":"Queens Park Rangers","league":14},{"id":17,"name":"Southampton","league":13},{"id":18,"name":"Tottenham Hotspur","league":13},{"id":19,"name":"West Ham United","league":13},{"id":21,"name":"Bayern M\u00fcnchen","league":19},{"id":22,"name":"Borussia Dortmund","league":19},{"id":23,"name":"Borussia M'gladbach","league":19}]}

'''

data = json.loads(clubs_string)

for club in data['items']:
	print(club['name'])
	