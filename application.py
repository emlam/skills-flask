from flask import Flask, render_template

app = Flask(__name__)


@app.route('/application')
def application_page():
    """Shows the application page form."""

    return render_template("application-form.html")
    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route('/application-response',methods=["GET"])
def application_response():
    """Shows the application response page form."""

    input_fname = request.args.get("firstname")

    return render_template("application-response.html",
                            input_fname=firstname)

#     Thank you, Jessica McHackbright, for applying to be a QA Engineer. Your
# minimum salary requirement is 89000 dollars.




if __name__ == "__main__":
    app.run(debug=True)
