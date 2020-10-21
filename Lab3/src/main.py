from scanner import Scanner


def main():
    problem_file = open('p1.txt', 'r')
    token_file = open('token.in', 'r')
    separators_file = open('separators.in', 'r')

    tokens = [x for x in token_file.read().splitlines()]
    separators = [x for x in separators_file.read().splitlines()]

    scanner = Scanner(problem_file, tokens, separators)
    scanner.scan()

    st_out = open('st.out', 'w')
    st_out.write(str(scanner.get_st()))

    pif_out = open('pif.out', 'w')
    pif_out.write(str(scanner.get_pif()))


main()
