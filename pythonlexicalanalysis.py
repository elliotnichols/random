######################################
# Python Lexical Analysis            #
# By @elliotnichols                  #
# Licence: MIT License               #
#                                    #
# No Known issues:                   #
# - None                             #
######################################

######################################
#              Licence               #
######################################
"""

MIT License

Copyright (c) 2020 Elliot Nichols

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
######################################
#             Code Input             #
######################################

inputstr = '''

run = 0
while True:
    print ("Hello World!")
    run += 1
    for i in range(5):
        print ("Hello World",i)
    if run == 4:
        break
print ("Good Bye!")

'''

######################################
#              Program               #
######################################

# Defining Types
symbols = ['+','-','*','/','%','>','<','&','|','~','^','>>','<<','=','"',"'",",",".","!","@",'£',"#","?",'`',':',';'] # single-char keywords
other_symbols = ['//', '**','==','!=','>=','<=','and','or','not','+=','-=','*=','/=','%=','//=','**=','&=','|=','^=','>>=','<<=','is','is not','in','not in'] # multi-char keywords
brackets = ['(',')']
keywords = ['False','await','else','import','pass','None','break','except','raise','True','class','finally','return','continue','for','lambda','try','as','def','from','nonlocal','while','assert','del','global','with','async','elif','if','yield','print','range']
KEYWORDS = symbols + other_symbols + keywords

# Defining tools used in program
intext = False
number = False
printed = False
white_space = ' '
lexeme = ''
toprint = ''

# Actual Program
for i,char in enumerate(inputstr):
    if char == '*':
        if inputstr[i-1] == '/':
            lexeme += '<operator>'
        elif inputstr[i+1] == '/':
            lexeme += '<operator>'
        else:
            lexeme += '<operator>'
    elif char == '/':
        if inputstr[i+1] != '*' and inputstr[i-1] != '*':
            lexeme += '<operator>'
        else:
            continue
    elif char == '=':
        if inputstr[i+1] != '=':
            lexeme += '<operator>'
        else:
            continue
    else:
        if char != white_space:
            lexeme += char # adding a char each time
    if (i+1 < len(inputstr)): # prevents error
        if inputstr[i+1] == white_space or inputstr[i+1] in KEYWORDS or lexeme in KEYWORDS or lexeme in keywords or inputstr[i+1] in keywords or lexeme in brackets: # if next char == ' '
            if lexeme != '':
                if lexeme in KEYWORDS:
                    print("<keyword>")
                elif lexeme in keywords:
                    print("<operator><keyword><operator>")
                elif lexeme in symbols:
                    print("<operator>")
                    if lexeme == "'" or lexeme == '"':
                        if intext == False:
                            intext = True
                        elif intext == True:
                            intext = False
                            printed = False
                elif lexeme in other_symbols:
                    print("<operator>")
                elif "\n" in lexeme:
                    print(toprint)
                    toprint = ""
                elif lexeme == "(":
                    print("<open_bracket>")
                elif lexeme == ")":
                    print("<close_bracket>")
                else:
                    try:
                        val = int(lexeme)
                        number = True
                    except ValueError:
                        pass
                    if intext == True:
                        print("<string>")
                    elif number == True:
                        print("<number>")
                    elif lexeme[:-2] == ")":
                        print("<string><close_bracket>")
                    elif "print" in lexeme:
                        print("<keyword>")
                    else:
                        if ")" in lexeme:
                            print("<string><close_bracket>")
                        elif number != True:
                            print("<string>")
                    if number == True:
                        number = False
                lexeme = ''