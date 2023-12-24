path = "welcome.txt"
wel = open(path, "r")
qs1 = open("questions.txt", "r")
#ans=open("Q2","r")
questions=qs1.read().split(",")
cscore=0
def score(decide, qcount,cans='none'):
    global cscore
    if decide=="true":
        print("\nCorrect Answer yaayyy!")
        cscore+=1
        print(f"\nYour Score={cscore}/{qcount}")
    else:
        print("\nWrong Answer ")
        print(f"Correct answer is={cans}")
        print(f"\nYour Score={cscore}/{qcount}")

def verify(ans,qcount):
    if ans.lower() not in ["a","b","c","d"]:
      print("\nChoose only A,B,C,D")
    if qcount==1:
        if ans.upper()=="C":
            score("true",qcount)
        else:
            score("false",qcount,"Paris")
    elif qcount==2:
        if ans.upper()=="B":
            score("true",qcount)
        else:
            score("false",qcount,"Mars")
    elif qcount==3:
        if ans.upper()=="C":
            score("true",qcount)
        else:
            score("false",qcount,"Nitrogen")
    elif qcount==4:
        if ans.upper()=="A":
            score("true",qcount)
        else:
            score("false",qcount,"William Shakespeare")
    elif qcount==5:
        if ans.upper()=="B":
            score("true",qcount)
        else:
            score("false",qcount,"Nile river")
class quiz:
    def __init__(self):
        pass
    def welcome(self):
        print("\n"+wel.read())
    def quizz(self):
        self.k=True
        self.qcount = 0
        while self.k:
            print(questions[self.qcount])
            self.qcount += 1
            self.ans=input("Choose Correct option(A,B,C,D)=")
            verify(self.ans,self.qcount)
            if self.qcount==len(questions):
                self.k=False
obj=quiz()
obj.welcome()
obj.quizz()
