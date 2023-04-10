from sqlalchemy.orm import Session
from . import models, schemas

#############  CREATE  #############

def create_league(db: Session, obj_in: schemas.League):
    data = models.League(**obj_in.dict())
    db.add(data)
    db.commit()
    db.refresh(data)

    return data

def create_league_alt(db: Session, obj_in: schemas.LeagueAlt):
    data = models.LeagueAltName(**obj_in.dict())
    db.add(data)
    db.commit()
    db.refresh(data)

    return data

def create_season(db: Session, obj_in: schemas.Season):
    data = models.Season(**obj_in.dict())
    db.add(data)
    db.commit()
    db.refresh(data)

    return data

def create_team(db: Session, obj_in: schemas.Team):
    data = models.Team(**obj_in.dict())
    db.add(data)
    db.commit()
    db.refresh(data)

    return data

def create_team_alt(db: Session, obj_in: schemas.TeamAlt):
    data = models.TeamAltName(**obj_in.dict())
    db.add(data)
    db.commit()
    db.refresh(data)

    return data

######################### GET ALL #############################

def get_leagues(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.League).offset(skip).limit(limit).all()

def get_leagues_alt(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.LeagueAltName).offset(skip).limit(limit).all()

def get_seasons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Season).offset(skip).limit(limit).all()

def get_teams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Team).offset(skip).limit(limit).all()

def get_teams_alt(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TeamAltName).offset(skip).limit(limit).all()

########################## GET BY ID ################################

def get_league(db: Session, id: int):
    return db.query(models.League).filter(models.League.id == id).first()

def get_league_alt(db: Session, id: int):
    return db.query(models.LeagueAltName).filter(models.LeagueAltName.id == id).first()

def get_season(db: Session, id: int):
    return db.query(models.Season).filter(models.Season.id == id).first()

def get_team(db: Session, id: int):
    return db.query(models.Team).filter(models.Team.id == id).first()

def get_team_alt(db: Session, id: int):
    return db.query(models.TeamAltName).filter(models.TeamAltName.id == id).first()

########################## GET BY name ################################

def get_league_name(db: Session, league_name: str):
    return db.query(models.League).filter(models.League.league_name == league_name).first()

def get_league_alt_league_id(db: Session, league_id: int):
    return db.query(models.LeagueAltName).filter(models.LeagueAltName.league_id == league_id)

def get_season_name(db: Session, season_name: str):
    return db.query(models.Season).filter(models.Season.season_name == id).first()

def get_team_name(db: Session, team_name: str):
    return db.query(models.Team).filter(models.Team.team_name == team_name).first()

def get_team_alt_team_id(db: Session, team_id: int):
    return db.query(models.TeamAltName).filter(models.TeamAltName.team_id == team_id)

