from flask import Flask, request, render_template, Response
import pandas as pd
from fakedata import generate_fake_data

#app = Flask(__name__)

# create the application object
app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        df = pd.read_csv(request.files.get('file'))
        final_df = generate_fake_data(df)
        #return render_template('upload.html', shape=df.shape)
        return Response (
            final_df.to_csv(index = False), 
            mimetype='text/csv',
            headers={
                'Content-disposition':
                'attachment; filename=yourfakedata.csv'
            }
        )
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)