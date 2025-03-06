from flask import Flask, render_template

app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Dynamic user route
@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
