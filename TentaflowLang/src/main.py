
import lexer

def main():

    # source code for Inkerion
    content = ""

    with open('test.ink', 'r') as file:
        content = file.read()
        #
        # lexer
        #

        lex = lexer.Lexer

main()
