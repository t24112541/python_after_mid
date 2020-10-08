import sqlite3

db=sqlite3.connect("sqlite/data.db")

def sh_all(db):
    cur=db.cursor()
    cur.execute("select * from data")
    return cur.fetchall()

def insertData(db,d_id,name):
    cur=db.cursor()
    cur.execute("insert into data (id,name) values(?,?)",(d_id,name,))
    db.commit()
def update(db,d_id,name):
    cur=db.cursor()
    cur.execute("update data set name=? where id=?",(name,d_id))
    db.commit()
def sh(db,d_id):
    cur=db.cursor()
    cur.execute("select * from data where id=?",(d_id,))
    return cur.fetchall()
def dele(db,d_id):
    cur=db.cursor()
    cur.execute("delete from data where id=?",(d_id,))
    db.commit()
def mk_empty(db):
    cur=db.cursor()
    cur.execute("delete from data")
    db.commit()


