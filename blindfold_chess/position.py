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
    
    def black_pieces(self):
        Black = ['p','r','n','b','q','k']
        return [str(piece[0].upper()) + str(piece[1]) for piece in self.pieces if (piece in Black)]
    
    def white_pieces(self):
        White = ['P','R','N','B','Q','K']
        return [str(piece[0]) + str(piece[1]) for piece in self.pieces if (piece in White)]
    
    def print_position(self):
        print(self.turn())
        print(self.en_passant())
        
        white = self.white_pieces()
        black = self.black_pieces()
        print("White")
        for piece in white:    
            print(piece),

        print("\nBlack")    
        for piece in black:
            print(piece),
            
        print("\n")
        
        

    
    
    
    
    
        

        