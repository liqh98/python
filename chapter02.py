Python 3.13.0 (main, Oct  7 2024, 21:58:50) [GCC 14.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
number_int = 6
number_float = 7
# add
number_int + 36
42
number_int - 5
1
>>> number_int * 7
42
>>> number_int / 2
3.0
>>> number_int // 2
3
>>> number_int % 4
2
>>> number_int ** 2
36
>>> number_int // 4 * 4 + (number_int % 4)
6
>>> word = "Python"
>>> # string length
>>> len(word)
6
>>> # split string
>>> word[0]
'P'
>>> word[:3]
'Pyt'
>>> word[-1]
'n'
>>> word[:3] + word[3:]
'Python'
>>> word.title()
'Python'
>>> word[42]
Traceback (most recent call last):
  File [35m"/usr/lib/python3.13/idlelib/run.py"[0m, line [35m590[0m, in [35mruncode[0m
    [31mexec[0m[1;31m(code, self.locals)[0m
    [31m~~~~[0m[1;31m^^^^^^^^^^^^^^^^^^^[0m
  File [35m"<pyshell#20>"[0m, line [35m1[0m, in [35m<module>[0m
[1;35mIndexError[0m: [35mstring index out of range[0m
