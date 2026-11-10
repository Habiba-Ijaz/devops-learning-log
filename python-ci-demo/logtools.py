def count_errors(lines):
    return len([line for line in lines if "ERROR" in line])
