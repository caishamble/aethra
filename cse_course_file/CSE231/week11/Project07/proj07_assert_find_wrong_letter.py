from crossword import Crossword,Clue


puzzle = Crossword("vowel.csv")
puzzle.board = [['■', '■', 'T', 'E', 'A'], ['■', 'T', 'O', 'G', 'A'], ['V', 'E', 'W', 'E', 'L'],
                 ['A', 'A', 'E', 'S', '■'], ['T', 'M', 'R', '■', '■']]
print(puzzle)

clue = Clue((0,2), 'A', 'TAP', 'Like some water')
student_index = puzzle.find_wrong_letter(clue)
assert student_index == 1

clue = Clue((2,0), 'D', 'VAN', 'Ride for a mover')
student_index = puzzle.find_wrong_letter(clue)
assert student_index == 2

clue = Clue((0,2), 'D', 'TOWER', 'Pisa has a noted one')
student_index = puzzle.find_wrong_letter(clue)
assert student_index == -1


