class ChessGame:
    def __init__(self):
        self.board = self.init_board()
        self.current_player = 'white'
        self.game_over = False
        self.winner = None
        
    def init_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Place pawns
        for i in range(8):
            board[1][i] = {'type': 'pawn', 'color': 'black'}
            board[6][i] = {'type': 'pawn', 'color': 'white'}
        
        # Place other pieces
        piece_order = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
        
        for i, piece in enumerate(piece_order):
            board[0][i] = {'type': piece, 'color': 'black'}
            board[7][i] = {'type': piece, 'color': 'white'}
            
        return board
    
    def get_board_state(self):
        return {
            'board': self.board,
            'current_player': self.current_player,
            'game_over': self.game_over,
            'winner': self.winner
        }
    
    def is_valid_position(self, pos):
        return 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7
    
    def get_piece_at(self, pos):
        if not self.is_valid_position(pos):
            return None
        return self.board[pos[0]][pos[1]]
    
    def is_valid_move(self, from_pos, to_pos):
        if not self.is_valid_position(from_pos) or not self.is_valid_position(to_pos):
            return False
        
        piece = self.get_piece_at(from_pos)
        if not piece or piece['color'] != self.current_player:
            return False
        
        target = self.get_piece_at(to_pos)
        if target and target['color'] == piece['color']:
            return False
        
        return self.is_valid_piece_move(piece, from_pos, to_pos)
    
    def is_valid_piece_move(self, piece, from_pos, to_pos):
        piece_type = piece['type']
        row_diff = to_pos[0] - from_pos[0]
        col_diff = to_pos[1] - from_pos[1]
        
        if piece_type == 'pawn':
            return self.is_valid_pawn_move(piece, from_pos, to_pos, row_diff, col_diff)
        elif piece_type == 'rook':
            return self.is_valid_rook_move(from_pos, to_pos, row_diff, col_diff)
        elif piece_type == 'knight':
            return abs(row_diff) == 2 and abs(col_diff) == 1 or abs(row_diff) == 1 and abs(col_diff) == 2
        elif piece_type == 'bishop':
            return self.is_valid_bishop_move(from_pos, to_pos, row_diff, col_diff)
        elif piece_type == 'queen':
            return (self.is_valid_rook_move(from_pos, to_pos, row_diff, col_diff) or 
                   self.is_valid_bishop_move(from_pos, to_pos, row_diff, col_diff))
        elif piece_type == 'king':
            return abs(row_diff) <= 1 and abs(col_diff) <= 1
        
        return False
    
    def is_valid_pawn_move(self, piece, from_pos, to_pos, row_diff, col_diff):
        direction = -1 if piece['color'] == 'white' else 1
        target = self.get_piece_at(to_pos)
        
        if col_diff == 0:
            if not target and row_diff == direction:
                return True
            if not target and row_diff == 2 * direction:
                start_row = 6 if piece['color'] == 'white' else 1
                return from_pos[0] == start_row
        elif abs(col_diff) == 1 and row_diff == direction:
            return target is not None
        
        return False
    
    def is_valid_rook_move(self, from_pos, to_pos, row_diff, col_diff):
        if row_diff != 0 and col_diff != 0:
            return False
        return self.is_path_clear(from_pos, to_pos)
    
    def is_valid_bishop_move(self, from_pos, to_pos, row_diff, col_diff):
        if abs(row_diff) != abs(col_diff):
            return False
        return self.is_path_clear(from_pos, to_pos)
    
    def is_path_clear(self, from_pos, to_pos):
        row_step = 0 if from_pos[0] == to_pos[0] else (1 if to_pos[0] > from_pos[0] else -1)
        col_step = 0 if from_pos[1] == to_pos[1] else (1 if to_pos[1] > from_pos[1] else -1)
        
        current_row, current_col = from_pos[0] + row_step, from_pos[1] + col_step
        
        while (current_row, current_col) != to_pos:
            if self.board[current_row][current_col] is not None:
                return False
            current_row += row_step
            current_col += col_step
        
        return True
    
    def make_move(self, from_pos, to_pos):
        if self.game_over:
            return {'success': False, 'error': 'Game is over'}
        
        if not self.is_valid_move(from_pos, to_pos):
            return {'success': False, 'error': 'Invalid move'}
        
        piece = self.board[from_pos[0]][from_pos[1]]
        target = self.board[to_pos[0]][to_pos[1]]
        
        self.board[to_pos[0]][to_pos[1]] = piece
        self.board[from_pos[0]][from_pos[1]] = None
        
        if target and target['type'] == 'king':
            self.game_over = True
            self.winner = self.current_player
        
        self.current_player = 'black' if self.current_player == 'white' else 'white'
        
        return {
            'success': True,
            'board': self.board,
            'current_player': self.current_player,
            'game_over': self.game_over,
            'winner': self.winner
        }
    
    def get_game_status(self):
        return {
            'current_player': self.current_player,
            'game_over': self.game_over,
            'winner': self.winner
        }