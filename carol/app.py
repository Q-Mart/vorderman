from flask import Flask, jsonify, json

import lettersRound
import numbersRound

app = Flask(__name__)

# class SolveLetters(Resource):
#     def get(self, inputLetters):
#         if len(inputLetters) > 9:
#             result = {'error':
#                         {'status': '400',
#                          'title': 'Input length greater than 9'}
#                       }
#         elif len(inputLetters) == 0:
#             result = {'error':
#                         {'status': '400',
#                          'title': 'No input'}
#                       }
#         else:
#             result = {'error': {'status': '200'},
#                       'data':
#                         {'solutions': [sol for sol in lettersround.solve(inputLetters)]}
#                       }

#         return jsonify(result)

# class Hello(Resource):
#     def get(self):
#         return jsonify({'data': 'Hello world!'})

@app.route('/')
def index():
    return "Hello world"

@app.route('/letters/<inputLetters>', methods=['GET'])
def solve_letters(inputLetters):
    if len(inputLetters) > 9:
        # result = {'error':
        #             {'status': '400',
        #              'title': 'Input length greater than 9'}
        #           }
        errorData = json.dumps({'status': '400', 'title': 'Input length greater than 9'})
        return jsonify(error=errorData)
    elif len(inputLetters) == 0:
        # result = {'error':
        #             {'status': '400',
        #              'title': 'No input'}
        #           }
        errorData = json.dumps({'status': '400', 'title': 'No input'})
        return jsonify(error=errorData)
    else:
        # result = {'error': {'status': '200'},
        #           'data':
        #             {'solutions': [sol for sol in lettersround.solve(inputLetters)]}
        #           }
        errorData = json.dumps({'status': '200'})
        payloadData = json.dumps({'solutions': [sol for sol in lettersRound.solve(inputLetters)]})
        return jsonify(error=errorData, data=payloadData)

# api.add_resource(Hello, '/')
# api.add_resource(SolveLetters, '/letters/<inputLetters>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
