from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/echo/')
def echo():
	kwargs = {}
	kwargs['thing'] = request.args.get('thing')
	kwargs['place'] = request.args.get('place')
	return render_template('flask3.html', **kwargs)

app.run(host='192.168.6.120', port=9999, debug=True)
