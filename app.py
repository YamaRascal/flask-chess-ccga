from flask import Flask, render_template, request, jsonify
from chess_game import ChessGame

app = Flask(__name__)
game = ChessGame()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/board')
def get_board():
    return jsonify(game.get_board_state())

@app.route('/api/move', methods=['POST'])
def make_move():
    data = request.get_json()
    from_pos = data.get('from')
    to_pos = data.get('to')
    
    result = game.make_move(from_pos, to_pos)
    return jsonify(result)

@app.route('/api/reset', methods=['POST'])
def reset_game():
    global game
    game = ChessGame()
    return jsonify({'status': 'reset'})

@app.route('/api/status')
def get_status():
    return jsonify(game.get_game_status())

if __name__ == '__main__':
    app.run(debug=True)