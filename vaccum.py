import sys
class room:
    def _int_ (self):
        self.dirty = False
    def suck(self):
        self.dirty = False

A = room()
B = room()
cost = 0
count = 2
A.dirty = input("Is room A dirty? Enter True/False: ").lower()=="true"
B.dirty = input("Is room B dirty? Enter True/False: ").lower()=="true"
vaccumpos= input("Is vaccum cleaner present in room A or B :")

if not A.dirty and not B.dirty:
    print("Both rooms are already clean Total cost = 0")
    sys.exit()
print("vaccum cleaner present in room ",vaccumpos)
while count>0:
    if vaccumpos == "A" and A.dirty:
        A.suck()
        print("cleaning room A")
        cost +=1
        count -=1
    if vaccumpos == "A" and B.dirty:
        print("vaccum cleaner moving to room B")
        cost +=1
        vaccumpos = "B"
    if vaccumpos == "B" and B.dirty:
        B.suck()
        print("cleaning room B")
        cost +=1
        count -=1
    if vaccumpos =="B" and B.dirty:
        print("Vaccum cleaner moving to room A")
        cost +=1
        vaccumpos = "A"
print("Both rooms cleaned")
print("Total cost = ",cost)


'''
Is room A dirty? Enter True/False: true
Is room B dirty? Enter True/False: true
Is vaccum cleaner present in room A or B :A
vaccum cleaner present in room  A
cleaning room A
vaccum cleaner moving to room B
cleaning room B
Both rooms cleaned
Total cost =  3
'''
