import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/unchrdemo.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
# Samples_Metadata = Base.classes.demogroups
Samples = Base.classes.demogroups


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


# @app.route("/names")
# def names():
#     """Return a list of sample names."""

#     # Use Pandas to perform the sql query
#     stmt = db.session.query(Samples).statement
#     df = pd.read_sql_query(stmt, db.session.bind)

#     # Return a list of the column names (sample names)
#     return jsonify(list(df.columns)[2:])



# @app.route("/samples/<sample>")
# def samples(sample):
#     """Return `otu_ids`, `otu_labels`,and `sample_values`."""
#     stmt = db.session.query(Samples).statement
#     sample_data = pd.read_sql_query(stmt, db.session.bind)
#     sample_data = sample_data.loc[sample_data[sample] > 1, ["Year", sample]]
#     # Format the data to send as json
#     data = {
#         "Year": sample_data.Year.values.tolist(),
#         "sample_values": sample_data[sample].values.tolist(),
#         }
#     return jsonify(data)


if __name__ == "__main__":
    app.run()
