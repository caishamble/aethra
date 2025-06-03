#################################
## CSE 231
## Debug exercise for Lab 3
## print() not allowed
#################################

string1 = "String manipulation"  # set a breakpoint at this line
string1 = string1[::-1]          # then progress one statement at a time
string2 = string1.upper()
string3 = string2[-3:]
string4 = string3[4:7]

for i,ch in enumerate(string3):
    ## check 'variable explorer'
    ## to see how 'i' and 'ch'
    ## change with every iteration
    ## of the 'for' loop
    ## use  F8 to progress
    ## one iteration at a time
    pass

