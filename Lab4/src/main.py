from models.scanner import Scanner


def main():
    reserved_words = []
    separators = []
    operators = []

    problem_file = open('p1.txt', 'r')
    token_file = open('token.in', 'r')

    token_file.readline()
    for i in range(10):
        separator = token_file.readline().strip()
        if separator == "space":
            separator = " "
        separators.append(separator)
    for i in range(10):
        operators.append(token_file.readline().strip())
    for i in range(19):
        reserved_words.append(token_file.readline().strip())

    scanner = Scanner(problem_file, reserved_words, separators, operators)
    scanner.scan()

    st_out = open('st.out', 'w')
    st_out.write(str(scanner.get_st()))

    pif_out = open('pif.out', 'w')
    pif_out.write(str(scanner.get_pif()))


main()
