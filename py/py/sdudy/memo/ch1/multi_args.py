# *args vs **kwargs
#   1. *args: 複数の不定数量の引数を渡せる
#   2. *kwargs: 複数の不定数量の[Key:Val]引数を渡せる
# 标准参数与*args、**kwargs在使用时的顺序 那么如果你想在函数里同时使用所有这三种参数， 顺序是这样的:
# some_func(fargs, *args, **kwargs)

#  例１：　*args   ***********************************************--Start--
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg throug *argv:", arg)


test_var_args('gudingArg', 'fushuArg1', 'fushuArg2', 'fushuArg3')


#  例１：　*args   ***********************************************--End--

print("--------------------")


#  例2：　*kwargs   **********************************************--Start--
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} ==> {1}".format(key, value))


greet_me(name="abc", age=11, add="東京都台東区上野")
#  例2：　*kwargs   **********************************************--End--


# ****************************************************************
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


args = ("one", 2, "xxx")
test_args_kwargs(*args)

kwargs = {"arg1": 5, "arg2": "six", "arg3": "yyy"}
test_args_kwargs(**kwargs)
# ****************************************************************
