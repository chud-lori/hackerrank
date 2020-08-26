if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # save arr value to score
    score = list(arr)
    # poping if input(arr) more than expected(n)
    while len(score) > n:
        score.pop()
    print('\n')
    for i in score:
        print(i)
    # remove max or winner to get the max which the runner up
    score = list(filter(lambda a: a!=max(score), score))
    print('-'*15)
    for i in score:
        print(i)

    print('-'*15,'\n',max(score))
