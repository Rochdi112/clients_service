# Dépendances FastAPI (JWT, current_user, DB session)
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from config import settings
from database import get_session

# Pour l'exemple, à adapter selon votre logique

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = next(get_session())
    try:
        yield db
    finally:
        db.close()

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return {"user_id": user_id}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid credentials")
