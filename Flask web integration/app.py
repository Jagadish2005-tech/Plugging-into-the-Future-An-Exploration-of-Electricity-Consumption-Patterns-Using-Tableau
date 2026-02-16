import os
from flask import Flask, render_template

# Explicitly tell Flask where the templates folder is
template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)