from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats


REGULAR_SEASON_RESULT_SET_NAME = "CareerTotalsRegularSeason"
PLAYOFF_RESULT_SET_NAME = "CareerTotalsPostSeason"
IMPORTANT_STAT_HEADERS = set(['REB', 'AST', 'STL', 'BLK', 'PTS'])


def get_player_by_name(player_name: str) -> str:
    '''
    This function takes a player's full name and 
    returns the players ID (as a string).
    '''
    matching_players = players.find_players_by_full_name(player_name)
    try:
        player_id = str(matching_players[0].get('id'))
    except IndexError:
        return None
    else:
        return player_id


def get_important_stats(player_id: str) -> dict:
    '''
    This function takes a player's ID (as a string)
    and returns a dictionary with the important stats (see IMPORTANT_STAT_HEADERS)

    note: the dictionary contains stats PER GAME, not totals
    '''

    # if player_id is already an ID don't do anything
    # otherwise look up the player and find their ID
    try: 
        int(player_id)
    except ValueError:
        player_id = get_player_by_name(player_id)

    if not player_id: 
        return 

    # api call
    all_stats = playercareerstats.PlayerCareerStats(player_id=player_id).get_dict()


    # everything after the api call is just processing
    for result_set in all_stats['resultSets']:
        if result_set['name'] == REGULAR_SEASON_RESULT_SET_NAME:
            regular_season_stats = result_set
        elif result_set['name'] == PLAYOFF_RESULT_SET_NAME:
            playoff_stats = result_set
    
    important_stats = dict()

    try:
        games = regular_season_stats['rowSet'][0][3] + playoff_stats['rowSet'][0][3]

        for index, header in enumerate(regular_season_stats['headers']):
            if header in IMPORTANT_STAT_HEADERS:
                reg = regular_season_stats['rowSet'][0][index]
                post = playoff_stats['rowSet'][0][index]
                if reg is None or post is None:
                    return
                important_stats[f"{header}_PER_GAME"] = (reg + post) / games
    except IndexError:
        # if anything goes wrong in the middle, just return None
        # this can happen when a player's records are incomplete for whatever reason
        return

    return important_stats
    


# # here, we try to get all the players' important stats
# # TODO: this is failing because the API calls are timing out
# all_player_stats = dict()
# for player in players.get_active_players():
#     all_player_stats[player['id']] = get_important_stats(player['id'])



def get_nearby_players(player_id: str) -> dict:
    '''
    takes player ID as a string and returns a dictionary
    of the closest players for each important stat
    '''
    this_stats = get_important_stats(player_id)
    closest_stats = None
    closest_players = None

    for player, that_stats in all_player_stats.items():
        print(player)
        if player['id'] == player_id:
            continue

        that_stats = get_important_stats(player['id'])
        if that_stats is None:
            continue

        if closest_stats is None:
            closest_stats = that_stats
            closest_players = dict()
            for stat in this_stats:
                closest_players[stat] = player['full_name']
            continue
        
        for stat in this_stats:
            current_dist = abs(this_stats[stat] - closest_stats[stat])
            new_dist = abs(this_stats[stat] - that_stats[stat])
            if new_dist < current_dist:
                closest_stats[stat] = that_stats[stat]
                closest_players[stat] = player['full_name']
    
    return closest_players

if __name__ == '__main__':
    c = get_important_stats('Lebron James')
    print(c)

