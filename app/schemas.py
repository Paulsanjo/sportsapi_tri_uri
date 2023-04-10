from typing import List, Optional
from pydantic import BaseModel


class LeagueBase(BaseModel):
    league_name: str
    league_country: str

class League(LeagueBase):
	id: Optional[int]


	class Config:
        orm_mode = True

class LeagueAltBase(BaseModel):
    league_name: str
    league_id: int

class LeagueAlt(LeagueAltBase):
	id: Optional[int]


	class Config:
        orm_mode = True

class SeasonBase(BaseModel):
    season_name: str
    league_id: int

class Season(SeasonBase):
	id: Optional[int]


	class Config:
        orm_mode = True

class TeamBase(BaseModel):
    team_name: str
    league_id: int

class Team(TeamBase):
	id: Optional[int]


	class Config:
        orm_mode = True

class TeamAltBase(BaseModel):
    team_name: str
    league_id: int

class TeamAlt(TeamAltBase):
	id: Optional[int]


	class Config:
        orm_mode = True