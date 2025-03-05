from fastapi import FastAPI, Depends ,status,Response,HTTPException,APIRouter
from . import schema , prac_models
from . prac_database import engine,SessionLoc
from sqlalchemy.orm import Session
from typing import List
from . hashing import Hash



app=FastAPI()
# app.router = 
prac_models.Base.metadata.create_all(engine) 

def get_db():
    db=SessionLoc()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog',status_code=status.HTTP_201_CREATED, tags=['Blogs'])
def create(request:schema.Alpha, db:Session= Depends(get_db)):
    new_blog= prac_models.Alpha(title=request.title, body=request.body , number=request.number)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.delete('/blog/{id}',status_code=status.HTTP_200_OK, tags=['Blogs'])
def delete(id, db:Session= Depends(get_db)):
    blog = db.query(prac_models.Alpha).filter(prac_models.Alpha.id==id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog of id {id} not found")
    
    blog.delete(synchronize_session=False)
    db.commit()

    return 'The blog is deleted successfully'

@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED, tags=['Blogs'])
def update(id , request:schema.Alpha,db:Session=Depends(get_db)):
    blog = db.query(prac_models.Alpha).filter(prac_models.Alpha.id==id)

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog of id {id} not found")
    
    blog.update(request.dict())
    db.commit()
    return 'Updated'




@app.get('/blog',response_model=List[schema.ShowAlpha], tags=['Blogs'])   # here we are getting multiple blogs so it cant return single blog so convert to list 
def index(db:Session= Depends(get_db)):
    blog= db.query(prac_models.Alpha).all()
    return blog

#using orm mode here
@app.get('/blog/{id}',status_code=status.HTTP_200_OK, response_model=schema.ShowAlpha, tags=['Blogs'])
def get_id(id,db:Session= Depends(get_db)):
    blog= db.query(prac_models.Alpha).filter(prac_models.Alpha.id==id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog id with {id} is not available")
    return blog


 
# ----------------FOR USER--------------------------

@app.post('/user',response_model=schema.ShowUser, tags=['User'])
def create_user(request:schema.User,db:Session=Depends(get_db)):
    # hashed_password = pwd_cxt.hash(request.password)
    new_user= prac_models.User(name=request.name, email=request.email , password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/user/{id}',response_model=schema.ShowUser, tags=['User'])
def get_user(id,db:Session=Depends(get_db)):
    user = db.query(prac_models.User).filter(prac_models.User.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User id with {id} is not available")
    return user

