##
# a
s = 'goodbye'
print(s[0] == 'g')
# True
##
# b
print(s[6]=='g')
# False
##
# c
print(s[0] == 'g' and s[1] == 'a')
# False
##
# d
print(s[-2] == 'x')
# False
##
# e
print(s[len(s)//2] == 'd')
# True
##
# f
print(s[0]==s[-1])
# False
##
# g
print(s[-5:-1]=='tion')
# False
