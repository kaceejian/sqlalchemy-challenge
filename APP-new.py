import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt
from dateutil.relativedelta import relativedelta

# Set up Database
engine = create_engine('sqlite:///hawaii.sqlite')

# Reflect existing database into a new model
Base = automap_base()

# Reflect tables
Base.prepare(engine, reflect=True)

# Save reference to tables
Measurement = Base.classes.measurement
Station = Base.classes.station

print(Base.classes.keys())

# Set up Flask
app = Flask(__name__)

# Flask routes
@app.route("/")
def testtest():
    """Lists all available routes."""
    return(
        f"Available Routes:<br/>"
        f"/api/V1.0/precipitation<br/>"
        f"/api/V1.0/Station<br/>"
        f"/api/V1.0/tobs<br/>"
    )
