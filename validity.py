def check_validity(operation):
    operation = operation.strip()
    return operation in ("+", "-", "*")
