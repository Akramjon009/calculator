def ifsible(txt):
    lis = ['-', '+', '/', '*', '(']
    if not (txt[len(txt)-1] in lis):
        return True
    else:
        return False

def ifbracket(txt):
    if txt != '':
       return True
    else:
        return False

def ifbrackets(txt):
    bracket1 = 0
    bracket2 = 0
    for i in txt:
        if i == '(':
            bracket1 += 1
        elif i == ')':
            bracket2 += 1

    if bracket1 == bracket2:
        return True
    else:
        return False

def ifbrackets2(txt):
    bracket1 = 0
    bracket2 = 0
    for i in txt:
        if i == '(':
            bracket1 += 1
        elif i == ')':
            bracket2 += 1

    if bracket1-bracket2 > 0:
        return True
    else:
        return False

def ifbrakets_with_number2(txt):
    lis = ['-', '+', '/', '*', '(']
    if(len(txt)>0):
        if not (txt[len(txt)-1] in lis):
            return True
        else:
            return False
    else:
        return True

def ifbrakets_with_number(txt):
    lis = ['-', '+', '/', '*', '(']
    if(len(txt)>0):
        if txt[len(txt)-1] in lis:
            return True
        else:
            return False
    else:
        return True
