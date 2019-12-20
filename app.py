import numpy as np
import os

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify

engine = create_engine(os.path.join("sqlite:///","Resources","hawaii.sqlite"))

Base = automap_base()
Base.prepare(engine, reflect = True)
Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

@app.route("/")

def Welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.9/<start>/<end><br/>"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(Measurement.date,Measurement.prcp)
    session.close()

    percp = {}
    for p in results:
        if p[0] in prcp:
            percp[p[0]].append(p[1])
        else:
            percp[p[0]]=[p[1]]
    return jsonify(prcp)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Station.station, Station.name).all()
    session.close()

    station = []
    for s in results:
        station.append(s.station)
    return jsonify(station)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    results = session.query(Measurement.tobs).filter(Measurement.date <= "2017-08-23").filter(Measurement.date >= "2016-08-23")
    temps = []
    for t in results:
        temps.append(t.tobs)
    return jsonify(temps)


if __name__ == '__main__':
    app.run(debug = True)