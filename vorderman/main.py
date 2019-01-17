from flask import Flask, jsonify, request
from flask_cors import CORS

import lettersRound
import numbersRound

app = Flask(__name__)
CORS(app)

@app.route('/letters', methods=['GET'])
def solve_letters():
    inputLetters = request.args.get('input')

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

@app.route('/numbers', methods=['GET'])
def solve_numbers():
    numbers = request.args.get('numbers')
    target = request.args.get('target')

    try:
        numbers = list(map(int, numbers.split(',')))
        target = int(target)
        answer = numbersRound.solve(target, numbers)
        result = {'error': {'status': '200'},
                  'data':
                    {'solutionPath': answer}
                  }
        return jsonify(result)

    except Exception:
        result = {'error':
                    {'status': '400',
                     'title': 'Bad Request. Request should be in the formate of numbers?=x,x,x,x,x,x&target=x'}
                  }
        return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
