from flask import Flask, request, jsonify
import os

import morph


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/emoji')  # get emoji list with query string 'words'
def get_emoji():
    words = request.args.get('words')
    if words:
        # response = jsonify([{"keyword": words,
        #                      "emoji": [{"imageUrl": "", "rawText": "( ღ'ᴗ'ღ )"},
        #                                {"imageUrl": "", "rawText": "(❁´▽`❁)"},
        #                                {"imageUrl": "", "rawText": "๑•‿•๑"}]},
        #                     {"keyword": words,
        #                      "emoji": [{"imageUrl": "", "rawText": "( ღ'ᴗ'ღ )"},
        #                                {"imageUrl": "", "rawText": "(❁´▽`❁)"},
        #                                {"imageUrl": "", "rawText": "๑•‿•๑"}]},
        #                     {"keyword": words,
        #                      "emoji": [{"imageUrl": "", "rawText": "( ღ'ᴗ'ღ )"},
        #                                {"imageUrl": "", "rawText": "(❁´▽`❁)"},
        #                                {"imageUrl": "", "rawText": "๑•‿•๑"}]}])
        response = (', ').join(morph.splitByMorphs(words))
        # response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'
        return response

    else:
        return '올바른 query string을 넣으세요.'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
