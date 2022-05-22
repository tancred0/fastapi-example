from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings





# old way of connecting
# import psycopg2
# from psycopg2.extras import RealDictCursor
# from time import sleep

# while True:

#     try:
#         conn = psycopg2.connect(
#             host='localhost',
#             database='fastapi',
#             user='postgres',
#             password='ABCdef123',
#             cursor_factory=RealDictCursor
#         )

#         cursor = conn.cursor()
#         print("\nDatabase connection was sucessful!\n")
#         break

#     except Exception as error:
#         print("Connecting to database failed.")
#         print("Error: ", error)
#         sleep(5)

## old way ends

SQLALCHEMY_DATABASE_URL = '''
    postgresql://
    <username>:<password>@
    <ip-address/hostname>/<database_name>
'''

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

### copy paste this code everytime :D ###