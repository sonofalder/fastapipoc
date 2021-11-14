from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    """
    Anything that inherits this class will automatically create a table based on the class name
    We don't have to keep worrying about creating table names, this method does it for us
    """
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()