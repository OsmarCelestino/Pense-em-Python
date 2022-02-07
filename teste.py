def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.
    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    fin = open(source, 'r')
    fout = open(dest, 'w')

    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)
    print(fout)

    fin.close()
    fout.close()


def main():
    pattern = 'livro_guttenberg.txt'
    replace = 'replace'
    source = 'arquivo_exercicios.txt'
    dest =  'arquivo_exercicios.txt'
    sed(pattern, replace, source, dest)


if __name__ == '__main__':
    main()