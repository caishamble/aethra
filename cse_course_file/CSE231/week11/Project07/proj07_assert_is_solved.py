from crossword import Crossword

instructor_not_win = False
instructor_win = True

puzzle1 = Crossword("vowel.csv")
puzzle1.board = [['■', '■', 'T', 'E', 'A'], ['■', '_', '_', '_', '_'], ['V', '_', '_', '_', '_'],
                      ['A', '_', '_', '_', '■'], ['N', '_', '_', '■', '■']]
print("puzzle 1: not win")
print(puzzle1)
student_not_win1 = puzzle1.is_solved()
assert instructor_not_win == student_not_win1

puzzle2 = Crossword("vowel.csv")
puzzle2.board = [['■', '■', 'T', 'E', 'A'], ['■', 'T', 'O', 'G', 'A'], ['V', 'E', 'W', 'E', 'L'],
                 ['I', 'A', 'E', 'S', '■'], ['N', 'M', 'R', '■', '■']]
print("puzzle 2: not win")
print(puzzle2)
student_not_win2 = puzzle2.is_solved()
assert instructor_not_win == student_not_win2

puzzle3 = Crossword("vowel.csv")
puzzle3.board = [['■', '■', 'T', 'A', 'P'], ['■', 'Y', 'O', 'G', 'A'], ['V', 'O', 'W', 'E', 'L'],
                 ['A', 'Y', 'E', 'S', '■'], ['N', 'O', 'R', '■', '■']]
print("puzzle 3: win")
print(puzzle3)
student_win = puzzle3.is_solved()
assert instructor_win == student_win
