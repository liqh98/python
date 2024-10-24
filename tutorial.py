# _*_ coding: utf-8 _*_
## number 
## int; float; string

int_number = 6
int_number + 36
int_number -3
int_number * 7
int_number // 4
int_number / 4

x = int(input("Please enter an integer: "))

if x < 0:
    x =0
    print("Negative changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print('More')

# like switch or case

words = ['cat', 'window', 'defenestrate']

for w in words: 
    print(w, len(w))
