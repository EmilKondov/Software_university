x = "global"

def outer():
    x = "local"

    def inner():
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    x = "nonlocal"
    print("outer:", x)
    change_global()

print(x)
outer()
print(x)
