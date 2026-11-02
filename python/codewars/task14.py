def find_short(s):
    list_of_words = s.split()
    len_list = []
    for i in list_of_words:
        len_list += str(len(i))
    return min(len_list)


print(find_short("bitcoin take over the world maybe who knows perhaps"))
