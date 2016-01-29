from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def home_page():
    """Shows the home page."""

    return render_template("index.html")
    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


@app.route('/application')
def application_page():
    """Shows the application page form."""

    return render_template("application-form.html")
    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route('/application-response',methods=["POST"])
def application_response():
    """Shows the application response page form."""

    input_fname = request.form.get("firstname")
    # print input_fname
    input_lname = request.form.get("lastname")
    input_jobreq = request.form.get("jobrequirement")
    input_salaryreq = request.form.get("salaryrequirement")

    return render_template("application-response.html",
                        firstname=input_fname,
                        lastname=input_lname,
                        jobrequirement=input_jobreq,
                        salaryrequirement=input_salaryreq)


if __name__ == "__main__":
    app.run(debug=True)
