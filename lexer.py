from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'print')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # START
        self.lexer.add('START',r'start')
        # STOP
        self.lexer.add('STOP', r'stop')
        # STRING
        self.lexer.add('STRING', r'"(.*?)"')
        # Parenthesis
        self.lexer.add('TAG', r'<(.*?)>')
        # EQUALS
        self.lexer.add('EQUAL', r'\=')
        # Semi Colon
        self.lexer.add('COLON', r'\:')
        # FOR
        self.lexer.add('FOR', r'for')
        # IN
        self.lexer.add('IN', r'in')
        # braces
        self.lexer.add('SBRACE', r'\[(.*?)\]')
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # Ignore spaces
        self.lexer.ignore('\s+')
        # Test description
        self.lexer.add('DESCR', r'descr')
        # Test result
        self.lexer.add('RESLT', r'reslt')
        # IS
        self.lexer.add('IS', r'is')
        # NOT
        self.lexer.add('NOT', r'not')
        # word
        self.lexer.add('WORD', r'[a-zA-Z_][a-zA-Z0-9_]*')


    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()