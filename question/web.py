from flask import Flask
app = Flask("Nam")

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/receive_picture")
def receivepic():
    return "Hello, Flask!"


@app.route("/nam")
def abc():

    return """<b>Hello</b>, Nam!. Very nice to meet you

<form action="/action_page.php">
  <label for="fname">First name:</label>
  <input type="text" id="fname" name="fname"><br><br>
  <label for="lname">Last name:</label>
  <input type="text" id="lname" name="lname"><br><br>
  <input type="submit" value="Submit">
</form>

<br>

<form action="/receive_picture">
  <input type="file" id="myFile" name="filename">
  <input type="submit">
</form>
	"""


app.run(host= '0.0.0.0')