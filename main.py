from lexer import Lexer
from parse import Parser
from codegen import Codegen
import sys
def write_file(code,path):
    output_file = open(path.replace('.cbd','.c'), "w")
    output_file.write(code)
    output_file.close()

def generate_code(path):
    msg = ""
    line_no = 0
    lexer = Lexer().get_lexer()
    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    with open(path) as fp:
        line_no = line_no + 1
        for line in fp:
            try:
                if((len(line.replace('\n',"")) > 0) and ('#' not in line)):
                    token = lexer.lex(line.replace('\n',""))
                    parser.parse(token)
                line_no = line_no + 1
            except:
                msg = "Syntax error in line No " + str(line_no)
                return msg
    fp.close()
    Code = Codegen()
    write_file(Code.doit(),path)
    return "Successfully generated"