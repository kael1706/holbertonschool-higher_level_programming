#!/usr/bin/python3
# print all State objects that contain the letter a
# from the database hbtn_0e_6_usa

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    u = sys.argv[1]
    p = sys.argv[2]
    mydb = sys.argv[3]

    query_c = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(
        query_c.format(u, p, mydb),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    s = Session()

    records = s.query(State).order_by(State.id)
    for i, row in enumerate(records, 1):
        if 'a' in row.name:
            print('{}: '.format(i) + row.name)
    s.close()
