import chess

class Position:
    def __init__(self, fen: str):
        self.fen  = fen
        self.board = chess.Board(fen)
        self.pieces = [(str(self.board.piece_at(n)), chess.square_name(n)) for n in range(64) if self.board.piece_at(n) != None]
     
    def turn(self) -> str:
        if self.board.turn == True:
            return "White to move"
        return "Black to move"
    
    def en_passant(self) -> str:
        if self.board.has_legal_en_passant() == True:
            return "en passant is legal\n"
        return ''
    
    def is_pawn(self, piece) -> str:
        if piece == 'P' or piece == 'p':
            return ""
        return piece
    
    def black_pieces(self) -> list[str]:
        Black = ['p','r','n','b','q','k']
        return [self.is_pawn(piece[0].upper()) + str(piece[1]) for piece in self.pieces if (piece[0] in Black)]
    
    def white_pieces(self) -> list[str]:
        White = ['P','R','N','B','Q','K']
        return [self.is_pawn(piece[0]) + str(piece[1]) for piece in self.pieces if (piece[0] in White)]
    
    def get_position(self) -> str:
        turn = self.turn()
        enPas = self.en_passant()
        
        white_list = self.white_pieces()
        black_list = self.black_pieces()
        
        white = ""
        black = ""
        
        for piece in white_list:
            white += piece
            white += " "
   
        for piece in black_list:
            black += piece
            black += " "
        
        return f"{turn}\n{enPas}White: {white.rstrip()}\nBlack: {black.rstrip()}"
        
        

    
    
    
    
    
        

        
