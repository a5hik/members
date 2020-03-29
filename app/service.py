from sqlalchemy import create_engine
from db.config import DATABASE_URI
from db.members import Member
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


class MembersService:
    def __init__(self):
        self.model = Member()

    def create(self, params):
        print(params)

        member = Member(**params)
        with session_scope() as s:
            s.add(member)
            print(member)
            return member

    def list(self):
        with session_scope() as s:
            members = s.query(Member).all()
            print(members)
