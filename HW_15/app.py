from flask import Flask, render_template, jsonify
import pandas as pd
from biodiversity import fetch_data
app = Flask(__name__)

subject_df, subjects, sample_df, desc_df, new_df = fetch_data()

@app.route("/")
def index():
    """Return the dashboard homepage."""
    return render_template("index.html")

@app.route('/names')
def names():
    name = subject_df["SAMPLEID"].tolist()
    return jsonify(name)

@app.route('/otu')
def descriptions():
    otu = new_df["lowest_taxonomic_unit_found"].tolist()
    return jsonify(otu)

@app.route('/metadata/<sample_id>')
def meta_data(sample_id):
   if any(subject_df.loc[subject_df['SAMPLEID'] == str(sample_id)]):
       metadata = subject_df.loc[subject_df['SAMPLEID'] == str(sample_id)]
   return jsonify(metadata.to_dict('records'))

@app.route('/samples/<sample>')
def top_ten(sample):
    sample = 'BB_940'
    sample_data = [{
        'otu_ids': new_df[sample].tolist(),
        'sample_values': new_df["otu_id"].tolist(),
    }]
    return jsonify(sample_data)


if __name__=="__main__":
    app.run(debug=True)    