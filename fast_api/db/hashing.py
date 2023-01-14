from passlib.context import CryptContext

# openssl rand -hex 32 for secret_key
SECRET_KEY = "89c5b806c1a927ef54a89d5c6b2b6ce661ec1726c730fbbbb4cf90e07838651d"
ALGORITHM = "HS265"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)
