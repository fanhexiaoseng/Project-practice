# _*_ coding : utf-8 _*_
# 打印这个图形
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
import sys

for i in range(1, 8):

    if i <= 4:
        print(" " * (4 - i), end="")
        print("*" * (7 - 2 * (4 - i)), end="")
        print(" " * (4 - i))
    elif i > 4:
        print(" " * (i - 4), end="")
        print("*" * (7 - 2*(i - 4)), end="")
        print(" " * (i - 4))
        
   *   
  ***  
 ***** 
*******
 ***** 
  ***  
   *   
