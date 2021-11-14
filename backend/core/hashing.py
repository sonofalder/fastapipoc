from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hasher():
    """
    Can easily test with this inline python
    from core.hashing import Hasher
    """
    @staticmethod
    def verify_pwd(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_pwd_hash(plain_password):
        return pwd_context.hash(plain_password)