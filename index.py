from flask import Flask, render_template, send_file
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template("index.html")


@app.route('/about')
def about():
	return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/return-files/')
def return_files_tut():
	try:
		return send_file('download/curriculum-vitae-SG-2020.pdf', attachment_filename='curriculum-vitae-SG-2019.pdf')
	except Exception as e:
		return str(e)
