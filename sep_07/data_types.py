pie = "apple"
sentence = "My pie has "+pie

print(sentence)

integer = 1 # 32 bytes 2 billion => 64 byte
floating = 3.1409823408274834270894798024379
string = "hello" 
boolean = True # or False

var1 = 1
var2 = 2
result = var1+var2
# 1 + 2 = 3
# print(var1+" + " + var2+" = " + result)
var1_str = str(var1)
print("var1:", type(var1), "var1_str:", type(var1_str))

print(str(var1)+" + " + str(var2)+" = " + str(result))
print(f"{var1} + {var2} = {var1+var2}")
