from sqlalchemy import Column, Integer, String,ForeignKey, DateTime
from sqlalchemy.orm import relationship
import datetime
from .db import Base

# model/table

class Sport(Base):
    __tablename__ = 'sports'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)

class Manager(Base):
    __tablename__ = 'managers'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    dob = Column(DateTime(timezone=True), default=None)
    nationality = Column(String(20))
    country_code = Column(String(20))
    gender = Column(String(20))
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)

class Venue(Base):
    __tablename__ = 'venues'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    capacity = Column(Integer)
    city_name = Column(String(20))
    country = Column(String(20))
    map_coordinates = Column(String(40))
    country_code = Column(String(20))
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    country = Column(String(20))
    country_code = Column(String(20))
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)

class League(Base):
    __tablename__ = "leagues"

    # fields 
    id = Column(Integer, primary_key=True, index=True)
    league_name = Column(String(20))
    league_country = Column(String(20))
    region = Column(String(20))
    gender = Column(String(20))
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship("Category", foreign_keys=[category_id])

class LeagueAltName(Base):
    __tablename__ = "league_alt_name"

    # fields 
    id = Column(Integer, primary_key=True, index=True)
    league_name = Column(String(20))
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)
    league_id = Column(Integer, ForeignKey('leagues.id'))
    league = relationship("League", foreign_keys=[league_id])

class Season(Base):
    __tablename__ = "seasons"

    # fields 
    id = Column(Integer, primary_key=True, index=True)
    season_name = Column(String(20))
    start_date = Column(DateTime(timezone=True), default=None)
    end_date = Column(DateTime(timezone=True), default=None)
    year = Column(Integer)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)
    league_id = Column(Integer, ForeignKey('leagues.id'))
    league = relationship("League", foreign_keys=[league_id])

class Team(Base):
    __tablename__ = "teams"

    # fields 
    id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String(20))
    country = Column(String(20))
    country_code = Column(Integer)
    abbreviation = Column(String(20))
    gender = Column(String(20))
    category_id = Column(Integer, ForeignKey('category.id'))
    league_id = Column(Integer, ForeignKey('leagues.id'))
    sport_id = Column(Integer, ForeignKey('sports.id'))
    manager_id = Column(Integer, ForeignKey('managers.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)
    
    league = relationship("League", foreign_keys=[league_id])
    category = relationship("Category", foreign_keys=[category_id])
    sport = relationship("Sport", foreign_keys=[sport_id])
    manager = relationship("Manager", foreign_keys=[manager_id])
    venue = relationship("Venue", foreign_keys=[venue_id])

class TeamAltName(Base):
    __tablename__ = "team_alt_name"

    # fields 
    id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String(20))
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)
    team_id = Column(Integer, ForeignKey('teams.id'))
    league = relationship("Team", foreign_keys=[team_id])

class Standing(Base):
    __tablename__ = "standings"
    id = Column(Integer, primary_key=True, index=True)
    season_id = Column(Integer, ForeignKey('seasons.id'))
    league_id = Column(Integer, ForeignKey('leagues.id'))
    team_id = Column(Integer, ForeignKey('teams.id'))
    rank = Column(Integer, default=None)
    round_number = Column(Integer, default=None)
    points = Column(Integer, default=None)
    match_won = Column(Integer, default=None)
    match_loss = Column(Integer, default=None)
    match_draw = Column(Integer, default=None)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)
    season = relationship("Season", foreign_keys=[season_id])
    league = relationship("League", foreign_keys=[league_id])
    team = relationship("Team", foreign_keys=[team_id])

class SeasonLeagueTeams(Base):
    __tablename__ = "season_league_teams"
    id = Column(Integer, primary_key=True, index=True)
    season_id = Column(Integer, ForeignKey('seasons.id'))
    league_id = Column(Integer, ForeignKey('leagues.id'))
    team_id = Column(Integer, ForeignKey('teams.id'))
    team_name = Column(String(20))
    short_name = Column(String(20))
    abbreviation = Column(String(20))
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)
    
    league = relationship("League", foreign_keys=[league_id])
    season = relationship("Season", foreign_keys=[season_id])
    team = relationship("Team", foreign_keys=[team_id])

class Referee(Base):
    __tablename__ = "referees"
    # fields 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    dob = Column(DateTime(timezone=True), default=None)
    nationality = Column(String(20))
    country_code = Column(String(20))

class Player(Base):
    pass

class PlayerStat(Base):
    pass

class TeamStat(Base):
    pass

class MatchEvent(Base):
    pass

class MatchStat(Base):
    pass

class TeamELo(Base):
    pass