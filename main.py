from lexer import Lexer
from parse import Parser
from codegen import Codegen

def write_file(code):
    output_file = open("test.c", "w")
    output_file.write(code)
    output_file.close()

def generate_code():
    line_no = 0
    lexer = Lexer().get_lexer()
    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    with open("test.cbd") as fp:
        line_no = line_no + 1
        for line in fp:
            try:
                if((len(line.replace('\n',"")) > 0) and ('#' not in line)):
                    token = lexer.lex(line.replace('\n',""))
                    parser.parse(token)
                line_no = line_no + 1
            except:
                print("Syntax error in line No " + str(line_no))
    fp.close()
    Code = Codegen()
    write_file(Code.doit())

generate_code()


# #print(4 + 4 - 2);
# text_a = """
# START "shamim"
# """
#
# testcase = """
# RESLT : <bswm_init()> IS <TRUE>
# """
#
# text_b = """
# STOP "shamim"
# """
#
# testdes = """
# DESCR : <BswM_fuckme(&hotchicks)>
# """
#
# lexer = Lexer().get_lexer()
# token_d = lexer.lex("DESCR : <BswM_fuckme(&hotchicks)>")
# token_a = lexer.lex(text_a)
# token_c = lexer.lex(testcase)
# token_b = lexer.lex(text_b)
#
# pg = Parser()
# pg.parse()
# parser = pg.get_parser()
# parser.parse(token_a)
# parser.parse(token_d)
# parser.parse(token_c)
# parser.parse(token_b)
#
# Code = Codegen()
# write_file(Code.doit())
