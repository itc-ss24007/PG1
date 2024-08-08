#グローバルスコープ
def scope_test():
    #ネステッドスコープ(scope_testのlocal scope)
    def do_local():
        # local scope
        s1 = "local  "

    def do_nonlocal():
        # from local to nested scope
        nonlocal s2
        s2 = "nolocal"

    def do_global():
        # from local to global scope
        global s3
        # global scope
        s3 = "global"

    s0 = s1 = s2 = s3 ="test  "
    do_local()
    print("After local    :", s0, s1, s2, s3)
    do_nonlocal()
    print("After nonlocal :", s0, s1, s2, s3)
    do_global()
    print("After global   :", s0, s1, s2, s3)

s0 = s1 = s2 = s3 = "initial "
print("In the global      :", s0, s1, s2, s3)
scope_test()
print("After func call    :", s0, s1, s2, s3)


