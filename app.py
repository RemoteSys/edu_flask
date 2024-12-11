from flask import Flask, render_template
import pandas as pd

from src import functions as fn

app = Flask(__name__)

@app.route('/')
def index():
    path = 'data/xy1.csv'
    df = pd.read_csv(path) 
    table = fn.table_html_view(df)

    return render_template('index.html', name='first table', table=table)

if __name__ == '__main__':
   app.run(debug=True)
