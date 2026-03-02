#loop1
#i = 3
#while i != 0:
#   print("meow")
#   i = i - 1



#loop2

#for i in[0,1,2]:
 #   print("meow")


#loop3
#for i in range(3):
#   print("meow")

#loop4
#print("meow\n"* 2,"meow")



#მაგალთები
#n = int(input("whats n?"))
#for _ in range(n):
#    print("meow")



#while True:
#    n = int(input("whats n?"))
#    if n <= 0:
#        continue
#    else:
#        break
#for _ in range(n):
#    print("meow")



def main():
    n = int(input("whats n?"))
    meow(n)


def meow(n):
    for _ in range(n):
        print("meow")


main()