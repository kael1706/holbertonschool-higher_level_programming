#!/usr/bin/python3
# prints all City objects with their states

import sys
from model_state import Base, State
from model_city import City
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

    for state, city in s.query(State, City).\
            filter(State.id == City.state_id):
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    s.close()
