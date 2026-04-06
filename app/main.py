from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from . import models, schemas

# DB 테이블 생성
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Ultimate FastAPI Guide",
    description="FastAPI Backend Development Project Structure",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "FastAPI 서버가 정상적으로 실행 중입니다!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

# 예시: 유저 생성 API
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    new_user = models.User(
        username=user.username,
        email=user.email,
        # 실무에서는 비밀번호를 해싱해야 합니다!
        is_active=True
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user