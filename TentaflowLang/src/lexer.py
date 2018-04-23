

class Lexer(object):

    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):
        print('test')


        tokens = []


        source_code = self.source.code.split()

        source_index = 0

        while source_index < len(source_code):
