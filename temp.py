from lexer import Lexer

text_input = """
START a = 1 "ggwp ace" = <hello(this)> [boi] nomad high
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

for token in tokens:
    print(token)