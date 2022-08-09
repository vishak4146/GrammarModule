from flask import Flask, request, jsonify
from gingerit.gingerit import GingerIt
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def getGrammarCorrections(text_input):
    parser = GingerIt()
    resultText = parser.parse(text_input)
    return resultText['result']


@app.route('/checkGrammar', methods=["POST"])
def checkGrammar():
    input_json = request.get_json(force=True)
    dictToReturn = {'text': getGrammarCorrections(input_json['text'])}
    return jsonify(dictToReturn)


if __name__ == '__main__':
    app.run(debug=True)
