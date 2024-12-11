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
    
    if  request.method == 'POST':
        # <input type="file" id="myfile" name="csv_file"><br><br>
        # use name from input tag to upload file
        file = request.files['csv_file']
        name = file.filename
        df = pd.read_csv(file) 
        table = fn.table_html_view(df)
        img = fn.create_base64(df)

    return render_template('index.html',
                           name=name,
                           table=table,
                           img64base=img
                           )

if __name__ == '__main__':
   app.run(debug=True)
