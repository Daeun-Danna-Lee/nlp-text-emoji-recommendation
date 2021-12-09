import firebase_admin
from firebase_admin import credentials, db
from flask import Flask, request, jsonify


# Firebase database 인증 및 앱 초기화
cred = credentials.Certificate(
    './emoji-recommendation-firebase-adminsdk-9td56-544cedf58d.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://emoji-recommendation-default-rtdb.asia-southeast1.firebasedatabase.app/'
})


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/emoji')  # get emoji list with query string 'words'
def get_emoji():
    words = request.args.get('words')
    if words:
        print(words)
        return jsonify({"words": words})
    else:
        return '올바른 query string을 넣으세요.'


dir = db.reference()
dir.update({'자동차': ['기아', '현대', '벤츠']})

dir = db.reference('이동수단/기차')
dir.update({'1번': 'KTX'})
dir.update({'2번': '무궁화'})

if __name__ == "__main__":
    app.run()
