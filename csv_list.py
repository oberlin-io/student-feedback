def csv_2_rows(csv_file):
    """
    Inputs csv file and returns a list, with each item being a row.
    """

    with open(csv_file,"r") as f:
        csv = f.read()

    return csv.splitlines() #row list


def row_2_list(row_list):
    """
    Inputs csv row list, counts the 'columns' (ie commas) in each item,
    and resturns each row as a list (a sub list),
    with each list item being a column.
    """

    col_cnt = 1
    for i in range(len(row_list)):
        if row_list[i] == ",":
            col_cnt += 1

    sub_lst = []
    for i in range(col_cnt):
        if "," not in row_list:
            sub_lst.append(row_list)
        else:
            for i in range(len(row_list)):
                if row_list[i] == ",":
                    sub_lst.append(row_list[:i])
                    row_list = row_list[i+1:]
                    break

    return sub_lst


def iter_r2l(row_list):
    """
    Iterates row_2_list module through the row list,
    and appends each sub list to the main list,
    which is a nested list representing rows and columns of the csv file.
    """

    list = []
    for i in row_list:
        list.append(row_2_list(i))

    return list


def make_list(csv_file):
    """
    Runs the program. Type the csv file with extension and in quotes.
    """

    return iter_r2l(csv_2_rows(csv_file))


def list_to_table(list):
    table = '<table>\n'
    for r in list:
        if list.index(r) == 0:
            table += '  <tr>\n'
            for c in r:
                table += '    <th>%s</th>\n' % c
            table += '  </tr>\n'
        else:
            table += '  <tr>\n'
            for c in r:
                table += '    <td>%s</td>\n' % c
            table += '  </tr>\n'
    table += '</table>'
    return table