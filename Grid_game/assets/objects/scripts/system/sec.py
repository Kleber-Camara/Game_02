class Sec:
    def __init__(self):
        pass

    def treat(self, st: str) -> str:
        return self.__cod(st)

    def retreat(self, st: str) -> str:
        return self.__decode(st)

    def __cod(self, st: str) -> str:
        temp = str()
        for n in range(len(st)):
            if st[n] == 'A':
                temp += '1'
            elif st[n] == 'B':
                temp += '2'
            elif st[n] == 'C':
                temp += '3'
            elif st[n] == 'D':
                temp += '4'
            elif  st[n] == 'E':
                temp += '5'
            elif st[n] == 'F':
                temp += '6'
            elif st[n] == 'G':
                temp += '7'
            elif st[n] == 'H':
                temp += '8'
            elif st[n] == 'I':
                temp += '9'
            elif st[n] == 'J':
                temp += '0'
            elif st[n] == 'K':
                temp += 'a'
            elif st[n] == 'L':
                temp += 'c'
            elif st[n] == 'M':
                temp += 'e'
            elif st[n] == 'N':
                temp += 'g'
            elif st[n] == 'O':
                temp += 'i'
            elif st[n] == 'P':
                temp += 'k'
            elif st[n] == 'Q':
                temp += 'm'
            elif st[n] == 'R':
                temp += 'o'
            elif st[n] == 'S':
                temp += 'q'
            elif st[n] == 'T':
                temp += 's'
            elif st[n] == 'U':
                temp += 'y'
            elif st[n] == 'W':
                temp += 'b'
            elif st[n] == 'Y':
                temp += 'd'
            elif st[n] == 'Z':
                temp += 'f'
            elif st[n] == 'X':
                temp += 'x'
            elif st[n] == 'a':
                temp += 'B'
            elif st[n] == 'b':
                temp += 'E'
            elif st[n] == 'c':
                temp += 'H'
            elif st[n] == 'd':
                temp += 'K'
            elif st[n] == 'e':
                temp += 'N'
            elif st[n] == 'f':
                temp += 'Q'
            elif st[n] == 'g':
                temp += 'T'
            elif st[n] == 'h':
                temp += 'Y'
            elif st[n] == 'i':
                temp += 'A'
            elif st[n] == 'j':
                temp += 'D'
            elif st[n] == 'k':
                temp += 'G'
            elif st[n] == 'l':
                temp += 'J'
            elif st[n] == 'm':
                temp += 'M'
            elif st[n] == 'n':
                temp += 'P'
            elif st[n] == 'o':
                temp += 'S'
            elif st[n] == 'p':
                temp += 'W'
            elif st[n] == 'q':
                temp += 'X'
            elif st[n] == 'r':
                temp += 'C'
            elif st[n] == 's':
                temp += 'F'
            elif st[n] == 't':
                temp += 'I'
            elif st[n] == 'u':
                temp += 'L'
            elif st[n] == 'w':
                temp += 'O'
            elif st[n] == 'x':
                temp += 'R'
            elif st[n] == 'y':
                temp += 'U'
            elif st[n] == 'z':
                temp += 'Z'
            elif st[n] == '0':
                temp += '!'
            elif st[n] == '1':
                temp += '#'
            elif st[n] == '2':
                temp += '.'
            elif st[n] == '3':
                temp += '%'
            elif st[n] == '4':
                temp += '&'
            elif st[n] == '5':
                temp += '*'
            elif st[n] == '6':
                temp += '-'
            elif st[n] == '7':
                temp += '_'
            elif st[n] == '8':
                temp += '+'
            elif st[n] == '9':
                temp += '='
            elif st[n] == '.':
                temp += '>'
            elif st[n] == '@':
                temp += ':'
            elif st[n] == '/':
                temp += ','
            elif st[n] == ' ':
                temp += '$'
            elif st[n] == ',':
                temp += '<'
            else:
                temp += st[n]

        return temp

    def __decode(self, st: str) -> str:
        temp = str()
        for n in range(len(st)):
            if st[n] == '1':
                temp += 'A'
            elif st[n] == '2':
                temp += 'B'
            elif st[n] == '3':
                temp += 'C'
            elif st[n] == '4':
                temp += 'D'
            elif  st[n] == '5':
                temp += 'E'
            elif st[n] == '6':
                temp += 'F'
            elif st[n] == '7':
                temp += 'G'
            elif st[n] == '8':
                temp += 'H'
            elif st[n] == '9':
                temp += 'I'
            elif st[n] == '0':
                temp += 'J'
            elif st[n] == 'a':
                temp += 'K'
            elif st[n] == 'c':
                temp += 'L'
            elif st[n] == 'e':
                temp += 'M'
            elif st[n] == 'g':
                temp += 'N'
            elif st[n] == 'i':
                temp += 'O'
            elif st[n] == 'k':
                temp += 'P'
            elif st[n] == 'm':
                temp += 'Q'
            elif st[n] == 'o':
                temp += 'R'
            elif st[n] == 'q':
                temp += 'S'
            elif st[n] == 's':
                temp += 'T'
            elif st[n] == 'y':
                temp += 'U'
            elif st[n] == 'b':
                temp += 'W'
            elif st[n] == 'd':
                temp += 'Y'
            elif st[n] == 'f':
                temp += 'Z'
            elif st[n] == 'x':
                temp += 'X'
            elif st[n] == 'B':
                temp += 'a'
            elif st[n] == 'E':
                temp += 'b'
            elif st[n] == 'H':
                temp += 'c'
            elif st[n] == 'K':
                temp += 'd'
            elif st[n] == 'N':
                temp += 'e'
            elif st[n] == 'Q':
                temp += 'f'
            elif st[n] == 'T':
                temp += 'g'
            elif st[n] == 'Y':
                temp += 'h'
            elif st[n] == 'A':
                temp += 'i'
            elif st[n] == 'D':
                temp += 'j'
            elif st[n] == 'G':
                temp += 'k'
            elif st[n] == 'J':
                temp += 'l'
            elif st[n] == 'M':
                temp += 'm'
            elif st[n] == 'P':
                temp += 'n'
            elif st[n] == 'S':
                temp += 'o'
            elif st[n] == 'W':
                temp += 'p'
            elif st[n] == 'X':
                temp += 'q'
            elif st[n] == 'C':
                temp += 'r'
            elif st[n] == 'F':
                temp += 's'
            elif st[n] == 'I':
                temp += 't'
            elif st[n] == 'L':
                temp += 'u'
            elif st[n] == 'O':
                temp += 'w'
            elif st[n] == 'R':
                temp += 'x'
            elif st[n] == 'U':
                temp += 'y'
            elif st[n] == 'Z':
                temp += 'z'
            elif st[n] == '!':
                temp += '0'
            elif st[n] == '#':
                temp += '1'
            elif st[n] == '.':
                temp += '2'
            elif st[n] == '%':
                temp += '3'
            elif st[n] == '&':
                temp += '4'
            elif st[n] == '*':
                temp += '5'
            elif st[n] == '-':
                temp += '6'
            elif st[n] == '_':
                temp += '7'
            elif st[n] == '+':
                temp += '8'
            elif st[n] == '=':
                temp += '9'
            elif st[n] == '>':
                temp += '.'
            elif st[n] == ':':
                temp += '@'
            elif st[n] == ',':
                temp += '/'
            elif st[n] == '$':
                temp += ' '
            elif st[n] == '<':
                temp += ','
            else:
                temp += st[n]

        return temp
