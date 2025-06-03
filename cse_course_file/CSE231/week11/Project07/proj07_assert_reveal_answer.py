from crossword import Crossword,Clue

instructor_board1 = [['■', '■', 'T', 'A', 'P'], ['■', 'T', 'O', 'G', 'A'], ['V', 'E', 'W', 'E', 'L'],
                 ['I', 'A', 'E', 'S', '■'], ['N', 'M', 'R', '■', '■']]

instructor_board2 = [['■', '■', 'T', 'A', 'P'], ['■', 'T', 'O', 'G', 'A'], ['V', 'E', 'W', 'E', 'L'],
                 ['A', 'A', 'E', 'S', '■'], ['N', 'M', 'R', '■', '■']]

puzzle = Crossword("vowel.csv")
puzzle.board = [['■', '■', 'T', 'E', 'A'], ['■', 'T', 'O', 'G', 'A'], ['V', 'E', 'W', 'E', 'L'],
                 ['I', 'A', 'E', 'S', '■'], ['N', 'M', 'R', '■', '■']]
print("Puzzle before")
print(puzzle)


clue = Clue((0,2), 'A', 'TAP', 'Like some water')
student_return = puzzle.reveal_answer(clue)
print("Puzzle after clue 1:", clue)
print(puzzle)
assert puzzle.board == instructor_board1 and student_return == None

clue = Clue((2,0), 'D', 'VAN', 'Ride for a mover')
student_return = puzzle.reveal_answer(clue)
print("Puzzle after clue 2:", clue)
print(puzzle)
assert puzzle.board == instructor_board2 and student_return  == None

