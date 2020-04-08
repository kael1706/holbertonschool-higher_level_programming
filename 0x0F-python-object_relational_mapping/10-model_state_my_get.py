#!/usr/bin/python3
# print the id of State object with
# the name passed as argument

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    u = sys.argv[1]
    p = sys.argv[2]
    mydb = sys.argv[3]
    name = sys.argv[4]

    query_c = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(
        query_c.format(u, p, mydb),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    s = Session()

    record = s.query(State).filter_by(name=name).first()
    print('{}'.format(record.id) if record else 'Not Found')
    s.close()
