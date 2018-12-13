from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    select = request.form.get('input_select', '')
    select = request.form.get('input_select', '')
    freeform = request.form.get('input_freeform', '')
    outputstring = name + " , " + select + " , " +  select


    return render_template("main_page.html",
                           output="You entered these: %s." % outputstring)
