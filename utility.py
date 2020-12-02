def get_data(source) -> list:
    """Returns a list of data from the sourced document"""
    data = [int(val) for val in open(source, "r").readlines()]
    return data

def get_data_string(source) -> list:
    data = [val for val in open(source, "r").readlines()]
    return data