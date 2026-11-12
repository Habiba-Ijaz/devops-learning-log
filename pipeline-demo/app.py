from logtools import count_errors

lines = ["INFO: ok", "ERROR: bad"]
print("Errors found:", count_errors(lines))
