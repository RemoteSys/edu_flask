from flask import Flask, render_template, request
import pandas as pd

from src import functions as fn

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # path = 'data/xy1.csv'
    path = None
    table = ''
    name=''
    img=''

    if path is not None:
        df = pd.read_csv(path) 
        table = fn.table_html_view(df)
        img = fn.create_base64(df)

    return render_template('index.html',
                           name=name,
                           table=table,
                           img64base=img
                           )

if __name__ == '__main__':
   app.run(debug=True)
