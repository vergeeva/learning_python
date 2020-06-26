import header


def main():
    # 1
    str_ = 'I want to find "t"'
    find_s = 't'
    print(f'количество символов {find_s} в строке {str_} = {header.find_count(find_s, str_)}')
    # количество символов t в строке I want to find "t" = 3

    # 2
    print('-----------------------------------------')
    print(ord('A'), ord('Z'), ord('a'), ord('z'), ord('А'), ord('Я'), ord('а'), ord('я'), ord(' '))
    # 65 90 97 122 1040 1071 1072 1103
    print('-----------------------------------------')
    a = 'File_1.txt'
    b = 'File.txt'
    try:
        header.convert_text(a, b)
    except ValueError:
        print("file not found")
    aa = open(a)
    bb = open(b)
    print(aa.read())
    print(bb.read())
    # Hi! My name is File!
    # HHii! MMyy nnaammee iiss FFiillee!


main()
