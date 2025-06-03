from crossword import Crossword, Clue

instructor_board1 = [['■', '■', 'T', 'E', 'A'], ['■', '_', '_', '_', '_'], ['_', '_', '_', '_', '_'],
                     ['_', '_', '_', '_', '■'], ['_', '_', '_', '■', '■']]

instructor_board2 = [['■', '■', 'T', 'E', 'A'], ['■', '_', '_', '_', '_'], ['L', '_', '_', '_', '_'],
                     ['E', '_', '_', '_', '■'], ['T', '_', '_', '■', '■']]

instructor_board3 = [['■', '■', 'T', 'E', 'A'], ['■', '_', 'E', '_', '_'], ['L', '_', 'A', '_', '_'],
                     ['E', '_', 'M', '_', '■'], ['T', '_', 'S', '■', '■']]

puzzle = Crossword("vowel.csv")
print("Puzzle before")
print(puzzle)


clue = Clue((0,2), 'A', 'TAP', 'Like some water')
new_guess = "TEA"
student_return = puzzle.change_guess(clue, new_guess)
print("Puzzle after clue 1:", clue)
print(puzzle)
assert puzzle.board == instructor_board1 and student_return == None

clue = Clue((2,0), 'D', 'VAN', 'Ride for a mover')
new_guess = "LET"
student_return = puzzle.change_guess(clue, new_guess)
print("Puzzle after clue 2:", clue)
print(puzzle)
assert puzzle.board == instructor_board2 and student_return  == None

clue = Clue((0,2), 'D', 'TOWER', 'Pisa has a noted one')
new_guess = "TEAMS"
student_return = puzzle.change_guess(clue, new_guess)
print("Puzzle after clue 3:", clue)
print(puzzle)
assert puzzle.board == instructor_board3 and student_return == None

print("Checking with a guess with incorrect length")
try:
    clue = Clue((0, 2), 'D', 'TOWER', 'Pisa has a noted one')
    new_guess = "TEAM"
    puzzle.change_guess(clue, new_guess)
    assert puzzle.board == instructor_board3
except RuntimeError as error_msg:
    assert puzzle.board == instructor_board3
    assert str(error_msg) == "Guess length does not match the length of the clue.\n"

print("Checking with a guess with invalid characters")
try:
    clue = Clue((0, 2), 'D', 'TOWER', 'Pisa has a noted one')
    new_guess = "Te,ms"
    puzzle.change_guess(clue, new_guess)
except RuntimeError as error_msg:
    assert puzzle.board == instructor_board3
    assert str(error_msg) == "Guess contains invalid characters.\n"


