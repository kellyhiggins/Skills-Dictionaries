from flask import Flask, render_template, redirect
import jinja2

app = Flask(__name__)
app.secret_key ='marshmallow'
app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

@app.route('/application-form')
def application_form():
    """Shows an application form, submits the users responses in a POST
        request."""

    return render_template('application-form.html')


@app.route('/application', methods=['POST'])
def application_response():
    """Returns a response that acknowledges their application,
    repeating back information submitted in the form."""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary = request.form.get("salary")
    job_title = request.form.get("jobtitle")

    return render_template('application.html',
                firstname=first_name, lastname=last_name,
                salary=salary, jobtitle=job_title)



if __name__ == "__main__":
    app.run(debug=True)
