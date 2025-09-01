# Flask Chess Game

A web-based chess game built with Flask backend and rich UI using Tailwind CSS.

## Features

- Complete chess game implementation
- Rich, responsive UI with Tailwind CSS
- Real-time game state updates
- Move validation for all chess pieces
- Game status tracking and winner detection
- Reset game functionality

## Setup and Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to `http://localhost:5000`

## How to Play

1. Click on a piece to select it
2. Click on a valid square to move the piece
3. The game alternates between white and black players
4. Capture the opponent's king to win the game
5. Use the "Reset Game" button to start a new game

## Project Structure

- `app.py` - Flask application and API routes
- `chess_game.py` - Chess game logic and move validation
- `templates/index.html` - Frontend with Tailwind CSS styling
- `requirements.txt` - Python dependencies

## API Endpoints

- `GET /` - Main game page
- `GET /api/board` - Get current board state
- `POST /api/move` - Make a move
- `POST /api/reset` - Reset the game
- `GET /api/status` - Get game status