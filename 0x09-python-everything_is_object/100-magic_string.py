def magic_string():
    magic_string.counter += 1
    return ("BestSchool, " * magic_string.counter + "BestSchool")
magic_string.counter = 0
