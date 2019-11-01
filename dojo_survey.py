from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def page_with_form():
    print("*"*30, "LOVE", "*"*30)
    print("Index Page with Form On It")
    return render_template("index.html")

@app.route('/result', methods=["POST"])
def form_answers():
    print("*"*30, "LOVE", "*"*30)
    print("Form Results")
    name_from_form = request.form["your-name"]
    dojo_location_from_form = request.form["dojo-location"]
    favorite_language_from_form = request.form["favorite-language"]
    comment_from_form = request.form["comment"]
    return render_template("results.html", your_name=name_from_form, dojo_location=dojo_location_from_form, favorite_language=favorite_language_from_form,
    comment=comment_from_form)











if __name__=="__main__":
    app.run(debug=True)


