import pytest
import blindfold_chess as bc

x = bc.Position("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

print(x.print_position())

def test_en_passant():
    assert x.en_passant() == ""
