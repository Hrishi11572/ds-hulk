# problem on AZ 101 

integer, floatnum , string, boolean , none  = input().split()

none = None

floatnum =  float(floatnum)

boolean = (boolean == "True")   # converts correctly

op1 = (f"{int(integer) + floatnum:.2f}")
op2 = (string + "Python")
op3 = (f"{int(bool(boolean)) * floatnum:.2f}")
op4 = (str(none) + "Value")

print(op1)
print(op2)
print(op3)
print(op4)
