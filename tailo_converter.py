
def get_dictionary(file):
    """
    Opens a text file in the format of [character, tailo] and creates a dictionary with the characters as keys
    :param file: text file to be opened
    :return: the dictionary to be returned
    """

    #opens the text file and reads each line in a list
    #we need
    stream = open(file, encoding="utf8")
    list_of_lines = stream.readlines()
    stream.close()


    tailo_dict = {}

    for i in range(len(list_of_lines)):

        list_of_lines[i] = list_of_lines[i].split(',')
        tailo_dict[ list_of_lines[i][0].strip() ] = list_of_lines[i][  len(list_of_lines[i]) - 1 ].strip()

    return tailo_dict


def get_character(tailo):

    pass


def get_tailo(character, tailo_dict):

    return tailo_dict[ character ]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    tailo_dict = get_dictionary('short-takes-char-tailo.txt')

    print ( get_tailo('足', tailo_dict) )

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
