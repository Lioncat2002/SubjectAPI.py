from typing import Optional

from fastapi import FastAPI
app=FastAPI()
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

  