
def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }
#gets players from home and away
home_players = game_dict()['home']['players']
away_players = game_dict()['away']['players']
all_players = home_players + away_players

#get the points per game for a given player
def num_points_per_game(player_name):
    i = 0
    while i < len(all_players):
        if player_name == all_players[i]['name']:
            player = all_players[i]
            player_points = player['points_per_game']
            return player_points
        i += 1

#gets the players age
def player_age(player_name):
    i = 0
    while i < len(all_players):
        if player_name == all_players[i]['name']:
            player = all_players[i]
            player_age = player['age']
            return player_age
        i += 1

#get the team colors for a given team name
home_team = game_dict()['home']
away_team = game_dict()['away']
def team_colors(team_name):
    if team_name == home_team['team_name']:
        home_team_color = home_team['colors']
        return home_team_color
    elif team_name == away_team['team_name']:
        away_team_color = away_team['colors']
        return away_team_color

#get the team names
def team_names():
    return [game_dict()['home']['team_name'],game_dict()['away']['team_name']]

#get the player numbers for a given team name
def player_numbers(team_name):
    if team_name == game_dict()['home']['team_name']:
        home_numbers = list()
        i = 0
        while i < len(home_players):
            player = home_players[i]
            player_number = player['number']
            home_numbers.append(player_number)
            i += 1
        return home_numbers    
    elif team_name  == game_dict()['away']['team_name']:
        away_numbers = list()
        i = 0
        while i < len(away_players):
            player = away_players[i]
            player_number = player['number']
            away_numbers.append(player_number)
            i += 1
        return away_numbers
    
#get the stats of a given player
def player_stats(player_name):
   for player in all_players:
        if player['name'] == player_name:
            return player

#calculate and print the average rebounds for each shoe brand
def average_rebounds_by_shoe_brand():
    brand_list = {"Nike": list(), "Adidas": list(), "Puma": list(), "Jordan": list()}

    for player in all_players:
        if player['shoe_brand'] == "Nike":
            brand_list["Nike"].append(player['rebounds_per_game'])
        elif player['shoe_brand'] == "Adidas":
            brand_list["Adidas"].append(player['rebounds_per_game'])
        elif player['shoe_brand'] == "Puma":
            brand_list["Puma"].append(player['rebounds_per_game'])
        elif player['shoe_brand'] == "Jordan":
            brand_list["Jordan"].append(player['rebounds_per_game'])

    for brand in brand_list:
        average = sum(brand_list[brand])/len(brand_list[brand])
        brand_list[brand] = round(average,2)
        print(f"{brand}:  {brand_list[brand]:.2f}",end="\n")
