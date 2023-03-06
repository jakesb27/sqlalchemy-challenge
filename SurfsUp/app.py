# Import dependencies
from flask import Flask, jsonify
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#################################################
# Database Setup
#################################################

# Create engine connection
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
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
    """List all available api routes."""

    routes = "<h1>Welcome!</h1><br/>" \
             "Below are the avaialable api routes.<br/><br/>" \
             "<a href='/api/v1.0/precipitation'> /api/v1.0/precipitation <a/><br/>" \
             "<a href='/api/v1.0/stations'> /api/v1.0/stations <a/><br/>" \
             "<a href='/api/v1.0/tobs'> /api/v1.0/tobs <a/><br/>" \
             "/api/v1.0/{start date}<br/>" \
             "/api/v1.0/{start date}/{end date}"

    return routes


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Route for handling precipitation api"""

    return "Precipitation"


@app.route("/api/v1.0/stations")
def stations():
    """Route for handling stations api"""

    return "stations"


@app.route("/api/v1.0/tobs")
def tobs():
    """Route for handling temperature api"""

    return "tobs"


@app.route("/api/v1.0/<start>")
def start_date(start):
    """Route for handling min, max, and avg for dates greater or equal to start"""

    return f"Start date: {start}"


@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    """Route for handling min, max, and avg for dates between start and end"""

    return f"Start date: {start}<br/>" \
           f"End date: {end}"


if __name__ == "__main__":
    app.run(debug=True)
