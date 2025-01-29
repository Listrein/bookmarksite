from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/catalog')
def catalog():
    return render_template('catalog.html')


@app.route('/provider')
def provider():
    return render_template('provider.html')


@app.route('/recommendations')
def recommendations():
    return render_template('recommendations.html')


@app.route('/nailbook')
def nailbook():
    return render_template('nailbook.html')


@app.route('/shrussonata')
def shrussonata():
    return render_template('shrussonata.html')


@app.route('/engine_rollers_1VDFTV')
def engine_rollers_1VDFTV():
    return render_template('engine_rollers_1VDFTV.html')


@app.route('/g4kd')
def g4kd():
    return render_template('g4kd.html')


@app.route('/akb')
def akb():
    return render_template('akb.html')
    
    
@app.route('/calc')
def calc():
    return render_template('calc.html')


@app.route('/sitemap.xml')
def sitemap():
    return render_template('sitemap.xml')


@app.route('/robots.txt')
def robots():
    return render_template('robots.txt')


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port = '5000')
