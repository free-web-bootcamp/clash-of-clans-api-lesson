from flask import Flask, render_template
from clash import get_user

app = Flask(__name__)


# Renders a specific template based off the URL. E.g. /player/ will render player.html
@app.route('/<string:page_name>/')
def render_static(page_name):
    if page_name == 'player':
        # get the user json blob from Clash of Clans API and render data with the html template
        user = get_user()
        return render_template('%s.html' % page_name, user=user)
    return render_template('%s.html' % page_name)


if __name__ == '__main__':
    app.run()
