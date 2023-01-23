import Lex

file = open('code.txt')
lines = file.readlines()
count = 1
for line in lines:
    lexer = Lex.Lexer(line)
    tokens = lexer.get_tokens()
    print(f'\nline {count}:')
    count+=1
    for token in tokens:
        print(token)