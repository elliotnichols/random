######################################
# Python Lexical Analysis            #
# By @elliotnichols                  #
#                                    #
# No Known issues:                   #
# - None                             #
######################################

######################################
#              Settings              #
######################################

filepath = "/Users/elliot/PycharmProjects/lexicalv3/test.py" # Enter your file path here.
debug_mode = False # Set to "True" for side by side comparison set to "False" to disable

######################################
#              Functions             #
######################################
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_numberprev(s):
    try:
        float(s)
        return False
    except ValueError:
        s = s[:-1]
        try:
            float(s)
            return True
        except ValueError:
            return False

def do_nothing():
    return

######################################
#              Program               #
######################################

# Defining Types
symbols = ['+','-','*','/','%','>','<','&','~','^','>>','<<','=',".","!","@",'£',"#","?",'`'] # single-char keywords
other_symbols = ['//', '**','==','!=','>=','<=','and','or','not','+=','-=','*=','/=','%=','//=','**=','&=','|=','^=','>>=','<<=','is','is not','in','not in'] # multi-char keywords
function = ['False','await','else','import','pass','None','break','except','raise','True','class','finally','return','continue','for','lambda','try','as','def','from','nonlocal','while','assert','del','global','with','async','elif','if','yield','print','range']
delimiters = [",",':',';','|']

# Initialise Variables
converted = ""
analysing = ""
brackets = False
number = False
operator = False
text = False

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
        # Print Debug Read Line:
        if debug_mode == True:
            print("Code Line {}: {}".format(cnt, line.strip()))
        # Get a raw line
        raw = line.strip()
        raw = raw.split("#", 1)[0] # Sanitises comments
        if len(raw.strip()) == 0:
            converted = ""
        else:
            # Carry on to converting
            for char in raw:
                analysing += char
                if is_number(analysing) == True and number != True:
                    converted += "<number>"
                    number = True
                if is_numberprev(analysing) == True:
                    type = ""
                    analysing = char
                    number = False
                do_nothing()
                if analysing in function:
                    converted += "<function>"
                    analysing = ""
                elif analysing in symbols or analysing in other_symbols and operator != True:
                    converted += "<operator>"
                    analysing = ""
                    operator = True
                elif analysing in delimiters:
                    converted += "<delimiter>"
                    analysing = ""
                elif analysing == " ":
                    analysing = ""
                elif analysing == "(":
                    converted += "<open_bracket>"
                    brackets = True
                    analysing = ""
                elif ")" in analysing and len(analysing) > 1 and text != True:
                    converted += "<identifier><close_bracket>"
                elif analysing == ")":
                    converted += "<close_bracket>"
                    brackets = False
                    analysing = ""
                elif analysing.endswith(" ") and text != True:
                    converted += "<identifier>"
                    analysing = ""
                elif analysing == "'" or analysing == '"' and text != True:
                    text = True
                    converted += "<string>"
                elif "'" in analysing[1:] or '"' in analysing[1:] and text == True:
                    text = False
                    analysing = ""
            # Print Result
            print("Converted Line {}: {}".format(cnt, converted))
            converted = ""
            analysing = ""
            brackets = False
            number = False
            operator = False
            text = False

        # Go to next line
        converted = ""
        line = fp.readline()
        cnt += 1
