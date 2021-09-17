import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt
# from dateutil.relativedelta import relativedelta

# Set up Database
engine = create_engine('sqlite:///hawaii.sqlite')

# Reflect existing database into a new model
Base = automap_base()

# Reflect tables
Base.prepare(engine, reflect=True)

# View all the columns in this dataframe
print(Base.classes.keys())
# # Save reference to tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# print(Base.classes.keys())

# # Set up Flask
app = Flask(__name__)

# # Flask routes
@app.route("/")
def testtest():
    """Lists all available routes."""
    return(
        f"Available Routes:<br/>"
        f"/api/V1.0/precipitation<br/>"
        f"/api/V1.0/Station<br/>"
        f"/api/V1.0/tobs<br/>"
    )


# Convert the query results to a dictionary using date as the key and prcp as the value.

@app.route("/api/v1.0/precipitation")
def precipitation():
    #Create session(link) from Python to DB
    session = Session(engine)

    #Query Measurement
    results = (session.query(Measurement.date, Measurement.prcp)
                    .order_by(Measurement.date)).all()

    #create dictionary
    d={}
    
    #put all results into the dictionary
    for result in results:
        d[result[0]]=result[1]
        #print(result[0],result[1])

    djson = jsonify(d)
   
    return(
        djson
    )



@app.route("/api/v1.0/stations")
def stations():
    #Create session(link) from Python to DB
    session = Session(engine)

    #Query Measurement
    results = (session.query(Station.station, Station.name)
                    .order_by(Station.station)).all()

    #create list
    li=[]
    
    #put all results into the dictionary
    for result in results:
        li.append(result[0])
        #print(result[0],result[1])

    lijson = jsonify(li)
   
    return(
        lijson
    )




@app.route("/api/v1.0/tobs")
def tobs():
    #Create session(link) from Python to DB
    session = Session(engine)

    #Query Measurement
    results = (session.query(Station.station, Station.name)
                    .order_by(Station.station)).all()

    #create list
    li=[]
    
    #put all results into the dictionary
    for result in results:
        li.append(result[0])
        #print(result[0],result[1])

    lijson = jsonify(li)
   
    return(
        lijson
    )

# Return the JSON representation of your dictionary.
if __name__ == '__main__':
    app.run()