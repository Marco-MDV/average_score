def home():
    arr=[]
    votesList=open("votes.txt","r")
    for line in votesList:
        arr.append(line.strip())
    votesList.close()
    sum=0
    for vote in arr:
        sum+=float(vote)
    med = sum/len(arr)
    print("The average vote is:", med)
home()