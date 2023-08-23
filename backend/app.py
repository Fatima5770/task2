from flask import Flask
from coupon import get_stats
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/')
@cross_origin(supports_credentials=True)
def stats():  # put application's code here
    return get_stats()


if __name__ == '__main__':
    app.run()
