from flask import Flask, request, render_template, redirect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, DATETIME, Integer, Column
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()
app = Flask(__name__)
app.secret_key = 'key'


class GuestBook(Base):
    __tablename__ = 'guestbook'
    postID = Column(Integer, primary_key=True)
    userName = Column(String(50))
    createdAt = Column(DATETIME,default=datetime.datetime.now())
    content = Column(String(1500))

# demo 24
class ToDo(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    pass


class DataBase(object):
    def __init__(self):
        self.info = {
            'user': 'root',
            'password': 'guyueyu710520',
            'ip': 'localhost',
            'port': '3306',
            'database': 'test'
        }
        self.session = self.make_connect()

    def __del__(self):
        if self.session:
            self.session.close()

    def make_connect(self):
        connect_str = 'mysql+pymysql://{user}:{password}@{ip}:{port}/{database}'.format_map(self.info)
        engine = create_engine(connect_str)
        self.create_table(self, engine)
        db_session = sessionmaker(engine)
        session = db_session()
        return session

    @staticmethod
    def create_table(self, engine):
        Base.metadata.create_all(engine)

    def query_all_post(self):
        items = self.session.query(GuestBook).order_by(GuestBook.postID).all()
        if not isinstance(items, list):
            return [items]
        return items

    def add_post(self, item):
        self.session.add(item)
        self.session.commit()


@app.route('/', methods=['GET', 'POST'])
def main():
    db = DataBase()
    if request.method == 'POST':
        data = request.values
        db.add_post(GuestBook(userName=data['userName'], content=data['content'], createdAt=datetime.datetime.now()))
        return redirect('/')
    items = db.query_all_post()
    return render_template('index.html', nums=len(items), items=items[::-1])


if __name__ == '__main__':
    app.run()
