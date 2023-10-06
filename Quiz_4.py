a = input()
b = int(a)

def print_gugudan(n):
    for x in range(1, n+1):
        print("------[ {x} 단 ] ------")
        for y in range(1, n+1):
            print(x,"x", y,"=",x*y)

example = print_gugudan(b)

