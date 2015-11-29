"""
This file has been automatically generated with workbench_alchemy v0.2.3
For more details please check here:
https://github.com/PiTiLeZarD/workbench_alchemy
"""

import os
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

if os.environ.get('DB_TYPE', 'MySQL') == 'MySQL':
    from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN, VARCHAR
else:
    from sqlalchemy import Integer, Boolean as BOOLEAN, String as VARCHAR

    class INTEGER(Integer):
        def __init__(self, *args, **kwargs):
            super(Integer, self).__init__()


DECLARATIVE_BASE = declarative_base()

    
    

class User(DECLARATIVE_BASE):

    __tablename__ = 'User'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    account_id = Column("account_id", INTEGER, primary_key=True, nullable=False)  # pylint: disable=invalid-name
    team_id = Column(INTEGER, ForeignKey("Team.team_id", onupdate="SET NULL", ondelete="CASCADE"), index=True)
    nickname = Column(VARCHAR(70))
    wins = Column(INTEGER)
    loses = Column(INTEGER)
    gpm = Column(INTEGER)
    xpm = Column(INTEGER)
    kda = Column(INTEGER)

    team = relationship("Team", foreign_keys=[team_id], backref="user")
    def __init__(self,account_id,team_id,nickname,wins,loses,gpm,xpm,kda):
        self.account_id = account_id
        self.team_id = team_id
        self.nickname = nickname
        self.wins = wins
        self.loses = loses
        self.gpm = gpm
        self.xpm = xpm
        self.kda = kda
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<User(%(account_id)s)>" % self.__dict__


class Match(DECLARATIVE_BASE):

    __tablename__ = 'Match'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    match_id = Column("match_id", VARCHAR(45), primary_key=True, nullable=False)  # pylint: disable=invalid-name
    match_seq_num = Column(INTEGER)
    start_time = Column(INTEGER)
    lobby_type = Column(INTEGER)
    first_blood_time = Column(INTEGER)
    radiant_win = Column(BOOLEAN)
    duration = Column(INTEGER)
    tower_status_radiant = Column(INTEGER)
    tower_status_dire = Column(INTEGER)
    barracks_status_radiant = Column(INTEGER)
    barracks_status_dire = Column(INTEGER)
    cluster = Column(INTEGER)
    human_players = Column(INTEGER)
    leagueid = Column(INTEGER)
    game_mode = Column(INTEGER)

    def __init__(self,match_id,match_seq_num,start_time,lobby_type,first_blood_time,
                 radiant_win,duration,tower_status_radiant,tower_status_dire,
                 barracks_status_radiant,barracks_status_dire,cluster,human_players,leagueid,game_mode):
        self.match_id = match_id
        self.match_seq_num = match_seq_num
        self.start_time = start_time
        self.lobby_type = lobby_type
        self.first_blood_time = first_blood_time
        self.radiant_win = radiant_win
        self.duration = duration
        self.tower_status_radiant = tower_status_radiant
        self.tower_status_dire = tower_status_dire
        self.barracks_status_radiant = barracks_status_radiant
        self.barracks_status_dire = barracks_status_dire
        self.cluster = cluster
        self.human_players = human_players
        self.leagueid = leagueid
        self.game_mode = game_mode
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Match(%(match_id)s)>" % self.__dict__


class UserMatch(DECLARATIVE_BASE):

    __tablename__ = 'User_Match'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    match_id = Column(
        VARCHAR(45), ForeignKey("Match.match_id", onupdate="CASCADE", ondelete="CASCADE"), autoincrement=False,
        primary_key=True, nullable=False
    )
    player_slot = Column(INTEGER)
    hero_id = Column(INTEGER)
    account_id = Column(
        INTEGER, ForeignKey("User.account_id"), autoincrement=False, index=True, primary_key=True, nullable=False
    )
    item_0 = Column(INTEGER)
    item_1 = Column(INTEGER)
    item_2 = Column(INTEGER)
    item_3 = Column(INTEGER)
    item_4 = Column(INTEGER)
    item_5 = Column(INTEGER)
    kills = Column(INTEGER)
    deaths = Column(INTEGER)
    assists = Column(INTEGER)
    leaver_status = Column(INTEGER)
    gold = Column(INTEGER)
    last_hits = Column(INTEGER)
    denies = Column(INTEGER)
    gold_per_min = Column(INTEGER)
    xp_per_min = Column(INTEGER)
    gold_spent = Column(INTEGER)
    hero_damage = Column(INTEGER)
    tower_damage = Column(INTEGER)
    hero_healing = Column(INTEGER)
    level = Column(INTEGER)

    match = relationship("Match", foreign_keys=[match_id], backref="userMatch")
    user = relationship("User", foreign_keys=[account_id], backref="userMatch")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<UserMatch(%(match_id)s, %(account_id)s)>" % self.__dict__


class Pick(DECLARATIVE_BASE):

    __tablename__ = 'Picks'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    match_id = Column(
        VARCHAR(45), ForeignKey("Match.match_id", onupdate="CASCADE", ondelete="CASCADE"), autoincrement=False,
        primary_key=True, nullable=False
    )
    order = Column(INTEGER, autoincrement=False, primary_key=True, nullable=False)
    team = Column(BOOLEAN, nullable=False)
    is_pick = Column(BOOLEAN, nullable=False)

    match = relationship("Match", foreign_keys=[match_id], backref="picks")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Pick(%(match_id)s, %(order)s)>" % self.__dict__


class AbilitiesUpgrade(DECLARATIVE_BASE):

    __tablename__ = 'Abilities_upgrades'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    match_id = Column(
        VARCHAR(45), ForeignKey("User_Match.match_id", onupdate="CASCADE", ondelete="CASCADE"), autoincrement=False,
        primary_key=True, nullable=False
    )
    account_id = Column(
        INTEGER, ForeignKey("User_Match.account_id", onupdate="CASCADE", ondelete="CASCADE"), autoincrement=False,
        primary_key=True, index=True
    )
    level = Column(INTEGER, autoincrement=False, primary_key=True, nullable=False)
    ability = Column(INTEGER)

    usermatch = relationship("UserMatch", foreign_keys=[match_id], backref="abilitiesUpgrades")
    usermatch = relationship("UserMatch", foreign_keys=[account_id], backref="abilitiesUpgrades")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<AbilitiesUpgrade(%(level)s, %(match_id)s, %(account_id)s)>" % self.__dict__


class Team(DECLARATIVE_BASE):

    __tablename__ = 'Team'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    team_id = Column("team_id", INTEGER, primary_key=True, nullable=False)  # pylint: disable=invalid-name
    name = Column(VARCHAR(45))
    def __init__(self,team_id,name):
        self.team_id = team_id
        self.name = name

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Team(%(team_id)s)>" % self.__dict__

