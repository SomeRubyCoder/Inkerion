
import lexer

def main():

    # source code for Inkerion
    content = ""

    with open('test.tfl', 'r') as file:
        content = file.read()
        #
        # lexer
        #

        lex = lexer.Lexer(content)

        tokens = lex.tokenize()

main()
