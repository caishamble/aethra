# Laboratory Exercise #1 (Part A)

AAA = 8
BBB = 20
CCC = 1
DDD = 11
EEE = 13
FFF = 5

# Give the value displayed by each of the calls to "print" below.

A = BBB // AAA

print( "\nValue of A: ", A )     # Value of A: _____2_______

B = BBB % AAA

print( "\nValue of B: ", B )     # Value of B: ______4______

C = DDD * 3 + FFF

print( "\nValue of C: ", C )     # Value of C: ______38______

D = EEE - FFF * 4

print( "\nValue of D: ", D )     # Value of D: ______-7______

E = EEE // FFF + CCC

print( "\nValue of E: ", E )     # Value of E: ______3______

F = EEE // (FFF + CCC)

print( "\nValue of F: ", F )     # Value of F: ______2______



G = FFF // 2 * 2

print( "\nValue of G: ", G )     # Value of G: _____4_______


# Laboratory Exercise #1 (Part B)

AAA = 7
BBB = 20

# Give the value displayed by each of the calls to "print" below.

A = 5
A += 1

print( "\nValue of A: ", A )     # Value of A: ______6______

B = 8
B += AAA

print( "\nValue of B: ", B )     # Value of B: ______15______

C = 10
C *= BBB

print( "\nValue of C: ", C )     # Value of C: _______200_____

D = 10
D *= (BBB + 3)

print( "\nValue of D: ", D )     # Value of D: ____230________

E = 10
E *= BBB + 3                          # note: the parentheses doesn't matter here

print( "\nValue of E: ", E )     # Value of E: _______230_____

F = 14
F -= BBB

print( "\nValue of F: ", F )     # Value of F: ______-6______

G = 25
G -= BBB + 3                         # note: the parentheses doesn't matter here

print( "\nValue of G: ", G )     # Value of G: _____2_______

H = 25
H %= 3

print( "\nValue of H: ", H )     # Value of H: _______1_____

J = I = 36

print( "\nValue of I: ", I )     # Value of I: _______36_____

print( "\nValue of J: ", J )     # Value of J: _______36_____


# Laboratory Exercise #1 (Part C)

AAA = 9
BBB = 13

XXX = 17.9
YYY = 1.2e+3
ZZZ = 5.625e-12

# Give the value displayed by each of the calls to "print" below.

A = int( XXX )

print( "\nValue of A: ", A )     # Value of A: _____17_______

B = int( XXX + 4.8 )

print( "\nValue of B: ", B )     # Value of B: ____22________

C = int( XXX - AAA // 2 )

print( "\nValue of C: ", C )     # Value of C: ______13______

D = int( ZZZ )

print( "\nValue of D: ", D )     # Value of D: ________0____

E = int( YYY - ZZZ )              # note: be careful

print( "\nValue of E: ", E )     # Value of E: ______1199______

X = float( BBB )

print( "\nValue of X: ", X )     # Value of X: _____13.0_______

Y = float( BBB // 2 )

print( "\nValue of Y: ", Y )     # Value of Y: ____6.0________