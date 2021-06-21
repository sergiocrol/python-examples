from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(f'{page_name}.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='')as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        # We turn the [] form data into a dictionary
        data = request.form.to_dict()
        # write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou')
    else:
        return 'Something went wrong'


# This is a dynamic path, we can use the name between <>, and aso 'int', 'string', 'uuid'... when we want to specify a type
# @app.route('/<username>/<int:user_id>')
# def dynamic(username=None, user_id=None):
#     return render_template('profile.html', username=username, user_id=user_id)


# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'This is my blog of dogs!!!'
