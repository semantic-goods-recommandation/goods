def get_tuple(filename, three_tuple):
    three_tuple_file = open(filename, 'r')
    for line in three_tuple_file:
        line_list = [int(line.split(' ')[0]), int(line.split(' ')[1]), int(line.split(' ')[2].replace('\n', ''))]
        three_tuple.append(line_list)
    three_tuple_file.close()