

from flask import Flask, render_template, request

import api

app = Flask('tinder-detective')

@app.route('/friends', methods=['GET', 'POST'])
def friends():
    stalker = api.NSASimulator(request.form['facebook_id'], request.form['facebook_token'])
    profiles = stalker.get_profiles()
    return render_template("friends.html", profiles=profiles)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("main.html")


if __name__ == '__main__':
    app.run(debug=True)
