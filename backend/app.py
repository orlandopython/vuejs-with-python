from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TeamOut(BaseModel):
    name: str
    city: str
    wins: int = 0
    losses: int = 0

class Team(TeamOut):
    id: int

teams = [
    Team(id=0, name="Magic", city="Orlando"),
    Team(id=1, name="Heat", city="Miami"),
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teams", response_model=list[TeamOut])
async def getTeams():
    return teams

@app.post("/team/{name}", response_model=TeamOut)
async def scoreTeam(name: str, win: bool = True):
    for team in teams:
        if team.name == name:
            if win:
                team.wins += 1
            else:
                team.losses += 1
            return team