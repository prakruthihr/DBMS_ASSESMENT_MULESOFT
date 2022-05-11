import sqlite3 as sql

connection = sql.connect("Movie.db")

pointer = connection.cursor()
pointer.execute("CREATE TABLE IF NOT EXISTS MOVIES( NAME TEXT, ACTOR TEXT, ACTRESS TEXT,DIRECTOR_NAME TEXT, YEAR INTEGER )")
pointer.execute("INSERT INTO MOVIES VALUES('KGF','YASH','ARCHANA','PRASANT',2019)")
pointer.execute("INSERT INTO MOVIES VALUES('BAHUBALI','PRABAS','ANUSHKA','RAJAMOULI',2020)")
pointer.execute("INSERT INTO MOVIES VALUES('Spider-Man: Homecoming','Tom Holland','Zendaya','Jon Watts',2017)")
pointer.execute("INSERT INTO MOVIES VALUES('KASHMIRI FILES','DARSHAN','PALLAVI','VIVEK',2022)")
pointer.execute("INSERT INTO MOVIES VALUES('Spider-Man: No Way Home','Tom Holland','Zendaya','Jon Watts',2021)")

# Printing all the elements of the database 
print("************************Everything in the database************************")
allMovies = pointer.execute("SELECT * FROM MOVIES").fetchall()
for i in allMovies:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("============================================================================================")

# In this query, we are printing only the details from the db where Tom Holland is the lead actor
print("************************Actor Query************************")
print("TO PRINT MOVIE DATA ACTED BY TOM HOLLAND" )
actorQuery = pointer.execute("SELECT * FROM MOVIES WHERE ACTOR = 'Tom Holland'").fetchall()
for i in actorQuery:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("============================================================================================")
  