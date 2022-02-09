from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins=["*"]


app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

science_subs=['physics','chemistry','maths','biology','computer']
arts_subs=['history','geography']
@app.get('/')
def read_root():
    return {'Home':'World'}

@app.get('/subjects/{subjects}')
def read_subject(subjects:str):
    subs=subjects.split(',')
    science_nums=sum(i in subs for i in science_subs)
    arts_nums=sum(i in subs for i in arts_subs)
    if science_nums>=arts_nums:
        return {'sub':'Science'}
    else:
        return {'sub':'Arts'}

  