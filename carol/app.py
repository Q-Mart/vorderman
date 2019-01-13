from flask import Flask, jsonify

import lettersRound
import numbersRound

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/letters/<inputLetters>', methods=['GET'])
def solve_letters(inputLetters):
    if len(inputLetters) > 9:
        result = {'error':
                    {'status': '400',
                     'title': 'Input length greater than 9'}
                  }
    elif len(inputLetters) == 0:
        result = {'error':
                    {'status': '400',
                     'title': 'No input'}
                  }
    else:
        result = {'error': {'status': '200'},
                  'data':
                    {'solutions': [sol.decode('utf-8') for sol in lettersRound.solve(inputLetters)]}
                  }
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
