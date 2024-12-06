import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from dotenv import load_dotenv
import os

load_dotenv()
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_TIME_DAYS = 60

class JWTService:
    @staticmethod
    def generate_token(username: str) -> str:
        expiration = datetime.utcnow() + timedelta(days=JWT_EXPIRATION_TIME_DAYS)
        payload = {
            "sub": username,
            "exp": expiration
        }
        return jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

    @staticmethod
    def verify_token(token: str) -> str:
        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
            return payload.get("sub")  # Retorna el username si el token es válido
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expirado")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
