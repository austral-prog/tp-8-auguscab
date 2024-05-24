def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):
    return tuple(coordinate)


def create_record(azara_record, rui_record):
    if (convert_coordinate(azara_record[1])) == rui_record[1]:
        return azara_record + rui_record
    else:
        return "not a match"
