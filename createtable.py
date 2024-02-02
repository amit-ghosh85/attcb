import sqlite3 as s

conn=s.connect('qa_database.sqlite')
print(conn)
c=conn.cursor()

qry='''
    create table questions_answers(
    question TEXT PRIMARY KEY, answer TEXT
    )
    '''
try:
    c.execute(qry)
    print("The table hasbeen created.......")

except:
    print("The table creation was unsuccessful!!!!!!!!")

c.close()



# def create_table():
#     conn = s.connect('qa_database.sqlite')
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS questions_answers
#                  (question TEXT PRIMARY KEY, answer TEXT)''')
#     conn.commit()
#     conn.close()