def concatenate(*args, **kwargs):
    string = "".join(args)

    for key, value in kwargs.items():
        if key in string:
            string = string.replace(key, value)
    return string

print(concatenate("Soft", "UNI", "Is", "Grate", "!",UNI="Uni", Grate="Great"))