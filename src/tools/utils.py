def parse_input_data(path):
    with open(path) as f:
        employees = f.readlines()
        return employees
