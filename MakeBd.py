from Classes import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import dota2api
#conncting to databases
engine = create_engine('mysql://root@localhost/dotadb',echo=False) #echo to log mysql
Session = sessionmaker(bind=engine)
session = Session()
api = dota2api.Initialise("9CCA0C9897E63A56712A9E9EB9B78D65")
# now session is resposible for database cursor

def testik():
    engine = create_engine('mysql://root@localhost/dotadb',echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    testUser = User(87,None,'kdk',100,0,1000,1000,20)
    session.add(testUser)
    ourUser = session.query(User).filter_by(nickname="kdk").first()
    return ourUser

#methods to work with DataBase
def addUserToBase(account_id,team_id,nickname,wins,loses,gpm,xpm,kda):
    if (team_id):
        addTeamToBase(team_id)
    addingUser = User(account_id,team_id,nickname,wins,loses,gpm,xpm,kda)
    session.add(addingUser)
    session.commit()

# test method without logo and so on, Only name and id
def addTeamToBase(team_id):
    name # make request to get name of team
    addingTeam = Team(team_id,name)
    session.commit()

#def addMatchToBase(match_id,match_seq_num,start_time,lobby_type,first_blood_time,
#                 season,radiant_win,duration,tower_status_radiant,tower_status_dire,
#                 barracks_status_radiant,barracks_status_dire,cluster,human_players,leagueid,game_mode):
# example 1968338912
def addOneMatchToBase(match_id=1968338912):
    match = api.get_match_details(match_id)
    addingMatch = Match(match['match_id'],match['match_seq_num'],match['start_time'],match['lobby_type'],match['first_blood_time'],match['radiant_win'],
                        match['duration'],match['tower_status_radiant'],match['tower_status_dire'],match['barracks_status_radiant'],match['barracks_status_dire'],match['cluster'],match['human_players'],match['leagueid'],match['game_mode'])
    session.add(addingMatch)
    session.commit()
    players = match['players']
    for player in players:
        if session.query(User).filter_by(account_id = player['account_id']).count()==0:
            inf =api.get_player_summaries(convert_to_64_bit(player['account_id']))
            if len(inf['players'])==0:# dota account is hidden
                nwUser = User(account_id=player['account_id'],nickname="Loser has hidden his account")
                session.add(nwUser)
            else:
                nwUser = User(account_id=player['account_id'],nickname=inf['players'][0]['personaname']) #can be problem
                session.add(nwUser)
            #add Match- user
                nwUserMatch = UserMatch(match_id,player['player_slot'],player['hero_id'],player['account_id'],player['item_0'],player['item_1'],player['item_2'],player['item_3'],player['item_4'],player['item_5'],player['kills'],player['deaths'],player['assists'],player['leaver_status'],player['gold'],player['last_hits'],player['denies'],player['gold_per_min'],player['xp_per_min'],player['gold_spent'],player['hero_damage'],player['tower_damage'],player['hero_healing'],player['level'])
                session.add(nwUserMatch)
            # add abilities upgrade(and for Capitans mode)
    #return match

#extra method to get steam_id from account id
def convert_to_64_bit(number):
     return number + 76561197960265728
