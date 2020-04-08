#!/usr/bin/python3
# print all State objects from the database hbtn_0e_6_usa

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    u = sys.argv[1]
    p = sys.argv[2]
    mydb = sys.argv[3]

    queryC = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(
        queryC.format(u, p, mydb),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    s = Session()

    for state in s.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    s.close()
