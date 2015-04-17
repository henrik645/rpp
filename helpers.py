def tokenize(program, expressions):
    pos = 0
    tokens = []
    match = None
    while pos < len(program):
        for expression in expressions:
            pattern, tag = expression
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    if text.isdigit():
                        text = int(text)
                    token = (text, tag)
                    tokens.append(token)
                break
        if match:
            pos = match.end(0)
        else:
            error("Unknown character sequence '" + characters[pos] + "'")
    return tokens
    
def usage():
    print("Usage: {0} file".format(sys.argv[0]))
    sys.exit(1)
    
def expected(message, received=None):
    if received:
        error("expected '" + message + "' but received '" + received + "'")
    else:
        error("expected '" + message + "'")
    sys.exit(1)
    
def error(message):
    print("Error: " + message + ".")
    sys.exit(1)
    
def advance():
    global symbol, symbol_type
    if len(tokens) == 0:
        error("Unexpected end of file")
    token = tokens.pop(0)
    symbol = token[0]
    symbol_type = token[1]
    
def match(token):
    if symbol == token:
        advance()
    else:
        expected(token, symbol)
        
def peek(token):
    if symbol == token:
        advance()
        return True
    else:
        return False
