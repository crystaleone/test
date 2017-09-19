from flask import Flask, render_template

app = Flask(__name__)

@app.route('/echo/<thing>/<place>')
def echo(thing, place):
	return render_template('flask3.html', thing=thing, place=place)

app.run(host='192.168.6.120', port=9999, debug=True)
