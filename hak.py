from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqlamodel import ModelView

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main_page.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/addit')
def addit():
    return render_template('addit.html')

@app.route('/social')
def soc():
    return render_template('soc.html')

@app.route('/for_older')
def for_older():
    return render_template('for_older.html')


#app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
#строчка выше придает лазурный цвет панели, строчку можно не использовать

admin = Admin(app)

if __name__ == '__main__':
    app.run(debug=False)