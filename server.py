from flask import Flask, request
from flask_cors import CORS, cross_origin
from parser_server import get_info_about_user_by_url
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def hello():
    url = request.args.get('url')
    # try: 
    user_info = get_info_about_user_by_url(url)
    # except: 
    #     return {"status": 404, "message": "user wasn`t found"}
    return user_info


if __name__ == "__main__":
    app.run()