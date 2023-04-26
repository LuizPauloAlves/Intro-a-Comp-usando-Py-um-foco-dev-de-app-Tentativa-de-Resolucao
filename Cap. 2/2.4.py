##
# a
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
print(s1 +' '+ s2 +' '+ s3)
#ant bat cod
##
# b
print(10 * (s1+' '))
#ant ant ant ant ant ant ant ant ant ant
##
# c
print(s1 +' '+ 2* (s2+' ') + 2 * (s3 +' ')+ s3)
#ant bat bat cod cod cod
##
# d
print(7 * (s1 +' '+ s2 +' '))
#ant bat ant bat ant bat ant bat ant bat ant bat ant bat
##
# e
print(3 * (2 * s2 + s3 + ' '))
#batbatcod batbatcod batbatcod
