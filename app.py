import io
from flask import Flask, render_template, request, session
import pandas as pd

from src import functions as fn

app = Flask(__name__)
app.secret_key = "secure key"


@app.route('/', methods=['GET', 'POST'])
def index():
    # path = 'data/xy1.csv'
    table = ''
    name = ''
    img = ''

    if request.method == 'POST':
        print(f"\n\n{request.form}\n\n")
        if 'csv_file' in request.files:
            # <input type="file" id="myfile" name="csv_file"><br><br>
            # use name from input tag to upload file
            file = request.files['csv_file']
            name = file.filename
            df = pd.read_csv(file)
            table = fn.table_html_view(df)
            # make df 'global' between sessions
            session['df'] = df.to_json()
            session['name'] = name
            session['table'] = table
        elif 'chart' in request.form:
            tmp = io.StringIO(session['df'])
            df = pd.read_json(tmp)
            name = session['name']
            table = session['table']
            img = fn.create_base64(df)

    return render_template('index.html',
                           name=name,
                           table=table,
                           img64base=img
                           )


if __name__ == '__main__':
    app.run(debug=True)
