# this is a question I encountered on hackerrank and I liked it, which is why its here lol

# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------

def doormat(width, length):
    for i in range(1,width,2): 
        print((i * ".|.").center(length, "-"))
    print("WELCOME".center(length,"-"))
    for i in range(width-2,0,-2): 
        print((i * ".|.").center(length, "-"))

if __name__ == '__main__':
    doormat(7, 21)