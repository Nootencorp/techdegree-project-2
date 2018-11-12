import csv

def read_file(local_file):
    """Reads a local csv file and returns ordered dictionary of variables.
    Then dumps contents of dictionary into a separate list."""
    with open(local_file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ',')
        players = list(reader)
        return players


def sort_players(reader):
    """Sort players into two lists based on soccer experience."""
    exp_players = []
    inexp_players = []

    for player in reader:
        if player['Soccer Experience'] == 'YES':
            exp_players.append(player)
        else:
            inexp_players.append(player)
    return exp_players, inexp_players


def assign_players(sorted_players, team_list):
    """Iterates through a list of players sorted by soccer experience and assigns players to teams.
    Team assignment occurs by looping though the index numbers of the list of teams
    and creates a new dictionary entry for each player's team."""
    index = 0
    player_list = []
    teams = []
    for key, value in team_list.items():
        teams.append(key)
    for exp_group in sorted_players:
        for player in exp_group:
            player['Team'] = teams[index]
            player_list.append(player)
            if index < 2:
                index += 1
            else:
                index = 0
    return player_list


def draft(team_list, player_list):
    """Looks at each individual player's assigned team and appends the player to
    that team's list of players."""
    for player in player_list:
        team = player['Team']
        if team in team_list:
            team_list[team].append(player)
    return team_list


def write_roster(teams):
    """Writes a text file that displays the teams, players, and player info."""
    file = open('teams.txt', 'a')
    for team, players in teams.items():
        file.write("\n" + team + "\n" + "=" * 90 + "\n")
        for player in players:
            name = player['Name']
            experience = player['Soccer Experience']
            guardians = player['Guardian Name(s)']
            file.write("Name: {}, Soccer Experience: {}, Guardian(s): {}\n".format(name, experience, guardians))


if __name__ == "__main__":
    team_list = {
        'Sharks': [],
        'Dragons': [],
        'Raptors': []
    }
    players = read_file('soccer_players.csv')
    sorted_players = sort_players(players)
    player_list = assign_players(sorted_players, team_list)
    teams = draft(team_list, player_list)
    write_roster(teams)
