def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("no zero div")
    except ValueError:
        ("no  numba bitcha")
        

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))


