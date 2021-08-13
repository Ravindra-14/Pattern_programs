def pattern_1():
    print('''To generate this type of pattern
* * * * * 
  * * * * 
    * * * 
      * * 
        *''')
    n=int(input('enter the number'))
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(j>=i):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    print("end")

def pattern_2():
    print(''' To generate this type of pattern
* * * * * 
 * * * * 
  * * * 
   * * 
    * ''')
    n=int(input('enter the number'))
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(j>=i):
                print("*",end=" ")
            else:
                print("",end=" ")
        print()
    print("end")
def pattern_3():
    print('''to generat this type of pattern
* 
* * 
* * * 
* * * * 
* * * * * ''')
    n=int(input('enter the number'))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
    print("end")
    
pattern_1()
pattern_2()
pattern_3()
