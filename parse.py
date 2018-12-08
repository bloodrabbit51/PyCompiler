from rply import ParserGenerator
from ast import Number, Sum, Sub, Print
from codegen import *


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'START', 'STOP','STRING','TAG','EQUAL','FOR','RESLT','DESCR','NOT','IS',
             'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN','IN','SBRACE','SEMI_COLON', 'SUM', 'SUB', 'COLON']
        )

    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN COLON')
        def program(p):
            return Print(p[2])

        @self.pg.production('program : START STRING')
        def program(s):
            testcase = s[1].getstr()
            testStart(testcase)

        @self.pg.production('program : STOP STRING')
        def program(s):
            testcase = s[1].getstr()
            testStop(testcase)

        @self.pg.production('program : DESCR COLON TAG')
        def program(s):
            TestDes(s[2].getstr())

        @self.pg.production('program : RESLT COLON TAG IS TAG')
        @self.pg.production('program : RESLT COLON TAG NOT TAG')
        def program(s):
            inp = s[2]
            out = s[4]
            operator = s[3]
            if operator.gettokentype() == 'IS':
                TestRes(inp.getstr(),out.getstr(), " == ")
            elif operator.gettokentype() == 'NOT':
                TestRes(inp.getstr(),out.getstr(), " != ")

        @self.pg.production('program : RESLT COLON NOT TAG')
        @self.pg.production('program : RESLT COLON IS TAG')
        def program(s):
            opr = s[2]
            api = s[3]
            if opr.gettokentype() == 'IS':
                TestResSingle(api.getstr(),"")
            elif opr.gettokentype() == 'NOT':
                TestResSingle(api.getstr(),"!")

        @self.pg.production('program : EQUAL FOR IN SBRACE SEMI_COLON SUM SUB')
        def program(s):
            print("gg")

        # @self.pg.production('expression : expression SUM expression')
        # @self.pg.production('expression : expression SUB expression')
        # def expression(p):
        #     left = p[0]
        #     right = p[2]
        #     operator = p[1]
        #     if operator.gettokentype() == 'SUM':
        #         return Sum(left, right)
        #     elif operator.gettokentype() == 'SUB':
        #         return Sub(left, right)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
