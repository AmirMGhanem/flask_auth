from flask import Flask , jsonify, redirect, url_for
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = 'AmirFTW'

oauth= OAuth(app)

github = oauth.register(
    name='github',
    client_id='6afbf97d652248daa742',
    client_secret='93a31af51714a1dcb5c876abf4c240f690fd6787',
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)

@app.route('/')
def index():
    return "Hello World from Home Page"

@app.route('/login')
def login():
    github = oauth.create_client('github')
    redirect_uri = url_for('authorize', _external=True)
    return github.authorize_redirect(redirect_uri)
@app.route('/authorize')
def authorize():
    github = oauth.create_client('github')
    token = github.authorize_access_token()
    resp = github.get('user', token=token)
    profile = resp.json()
    # do something with the token and profile
    return jsonify(profile, token)


if __name__ == '__main__':
    app.run(debug=True)