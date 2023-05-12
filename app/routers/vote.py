from fastapi import Response,status,HTTPException,Depends,APIRouter
from app.database import get_db
from .. import models,auth2,schemas
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/vote',
    tags=["LIKE"]
)

@router.post('/',status_code=status.HTTP_201_CREATED)
def vote(vote:schemas.Vote,db:Session = Depends(get_db),current_user:int = Depends(auth2.get_current_user)):
    post = db. query (models.Post).filter (models.Post.id == vote.post_id) .first ()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {vote.post_id} does not exist")


    check = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,models.Vote.user_id == current_user.id)

    check_found = check.first()

    if vote.dir ==1:
        if check_found:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)
        new_vote = models.Vote(post_id=vote.post_id,user_id=current_user.id)
        db.add(new_vote)
        db.commit()

        return {"message":"successfully liked"}
    
    # remove like

    else:
        if not check_found:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not liked yet")
        check.delete(synchronize_session=False)
        db.commit()

        return {"message":"successfully unliked"}
    

@router.get('/{id}')
def likes(id:int,db:Session= Depends(get_db)):
    likes = db.query(models.Vote).filter(models.Vote.post_id==id).all()
    x = len(likes)
    return {"likes":x}