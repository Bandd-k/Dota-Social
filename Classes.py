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

    id = Column("account_id", INTEGER, primary_key=True, nullable=False)  # pylint: disable=invalid-name

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<User(%(id)s)>" % self.__dict__


class Match(DECLARATIVE_BASE):

    __tablename__ = 'Match'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column("match_id", VARCHAR(45), primary_key=True, nullable=False)  # pylint: disable=invalid-name
    match_seq_num = Column(INTEGER, nullable=False)
    start_time = Column(INTEGER, nullable=False)
    lobby_type = Column(INTEGER, nullable=False)
    first_blood_time = Column(INTEGER, nullable=False)
    season = Column(INTEGER, nullable=False)
    radiant_win = Column(BOOLEAN, nullable=False)
    duration = Column(INTEGER, nullable=False)
    start_time = Column(INTEGER, nullable=False)
    tower_status_radiant = Column(INTEGER, nullable=False)
    tower_status_dire = Column(INTEGER, nullable=False)
    barracks_status_radiant = Column(INTEGER, nullable=False)
    barracks_status_dire = Column(INTEGER, nullable=False)
    cluster = Column(INTEGER, nullable=False)
    human_players = Column(INTEGER, nullable=False)
    leagueid = Column(INTEGER, nullable=False)
    game_mode = Column(INTEGER, nullable=False)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Match(%(id)s)>" % self.__dict__


class UserMatch(DECLARATIVE_BASE):

    __tablename__ = 'User_Match'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    match_id = Column(VARCHAR(45), autoincrement=False, primary_key=True, nullable=False)
    player_slot = Column(INTEGER)
    hero_id = Column(INTEGER)
    account_id = Column(INTEGER, autoincrement=False, primary_key=True, nullable=False)
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

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<UserMatch(%(match_id)s, %(account_id)s)>" % self.__dict__


class Pick(DECLARATIVE_BASE):

    __tablename__ = 'Picks'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    match_id = Column(VARCHAR(45), autoincrement=False, primary_key=True, nullable=False)
    order = Column(INTEGER, autoincrement=False, primary_key=True, nullable=False)
    team = Column(BOOLEAN, nullable=False)
    is_pick = Column(BOOLEAN, nullable=False)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Pick(%(match_id)s, %(order)s)>" % self.__dict__


class AbilitiesUpgrade(DECLARATIVE_BASE):

    __tablename__ = 'Abilities_upgrades'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    match_id = Column(VARCHAR(45), autoincrement=False, primary_key=True, nullable=False)
    account_id = Column(INTEGER, autoincrement=False, primary_key=True, nullable=False)
    level = Column(INTEGER, autoincrement=False, primary_key=True, nullable=False)
    ability = Column(INTEGER)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<AbilitiesUpgrade(%(level)s, %(match_id)s, %(account_id)s)>" % self.__dict__
