def createReverseIndex(lines):
    print('Use these constants: {}, {}, {}'.format(FileConstants.TableNamePrefix, FileConstants.UserPrefix,
                                                   FileConstants.ColumnPrefix))

    raise Exception('boo')


def getLines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]


class FileConstants:
    TableNamePrefix = '$'
    UserPrefix = '#'
    ColumnPrefix = '-'


if __name__ == '__main__':
    filename = 'dictionary/sample.txt'
    lines = getLines(filename)

    reverseIndex = createReverseIndex(lines)
