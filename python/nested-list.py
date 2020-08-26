if __name__ == '__main__':
    student=[]
    allScore=[]
    for _ in range(int(input("Total: "))):
        name = input("Name: ")
        score = float(input("Score: "))
        student.append([name, score])
    for i in student:
        allScore.append(i[1])
    # remove max or winner to get the max which the runner up
    s = list(filter(lambda a: a[1]!=min(allScore), student))
    mini=min(s, key=lambda a: a[1]) 
    print("S: ",s)
    print("Mini: ",mini)
    final=[]
    for i in s:
        if i[1]==mini[1]:
            final.append(i)
    final.sort(key=lambda a: a[0])
    for name in final:
        print(name[0])
