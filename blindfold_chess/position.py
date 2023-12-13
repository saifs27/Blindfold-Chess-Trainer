import chess

class Position:
    def __init__(self, fen):
        self.fen  = fen
        self.board = chess.Board(fen)
        self.pieces = [(str(self.board.piece_at(n)), chess.square_name(n)) for n in range(64) if self.board.piece_at(n) != None]
     
    def turn(self):
        if self.board.turn == True:
            return "White to move"
        return "Black to move"
    
    def en_passant(self):
        if self.board.has_legal_en_passant() == True:
            return "en passant is legal\n"
        return ''
    
    def is_pawn(self, str):
        if str == 'P' or str == 'p':
            return ""
        return str
    
    def black_pieces(self):
        Black = ['p','r','n','b','q','k']
        return [self.is_pawn(piece[0].upper()) + str(piece[1]) for piece in self.pieces if (piece[0] in Black)]
    
    def white_pieces(self):
        White = ['P','R','N','B','Q','K']
        return [self.is_pawn(piece[0]) + str(piece[1]) for piece in self.pieces if (piece[0] in White)]
    
    def print_position(self):
        print(self.turn())
        print(self.en_passant())
        
        white = self.white_pieces()
        black = self.black_pieces()
        print("White: ")
        for piece in white:    
            print(piece, end=" ")
        
        print("")

        print("\nBlack: ")    
        for piece in black:
            print(piece, end=" ")
        
        return ""
        
        

    
    
    
    
    
        

        
