# Import dependencies
from flask import Flask, jsonify
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    """List all avaialble api routes."""

    routes = "<h1>Welcome!</h1><br/>"\
        "Below are the avaialable api routes.<br/><br/>"\
        "<a href='/api/v1.0/precipitation'> /api/v1.0/precipitation <a/><br/>"\
        "<a href='/api/v1.0/stations'> /api/v1.0/stations <a/><br/>"\
        "<a href='/api/v1.0/tobs'> /api/v1.0/tobs <a/><br/>"\
        "/api/v1.0/{start}<br/>"\
        "/api/v1.0/{start}/{end}"

    return routes


@app.route("/api/v1.0/precipitation")
def precipitation():

    return "Precipitation"


@app.route("/api/v1.0/stations")
def stations():
    
    return "stations"


@app.route("/api/v1.0/tobs")
def tobs():
    
    return "tobs"


@app.route("/api/v1.0/<start>")
def start_date(start):
    
    return f"Start date: {start}"


@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    
    return f"Start date: {start}<br/>"\
            f"End date: {end}"



if __name__ == "__main__":
    app.run(debug=True)
