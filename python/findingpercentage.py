'''
Finding the percentage
'''
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    student_show = student_marks[query_name]
    value = 0
    for i in student_show:
        value+=i
    value = value/len(student_show)
    print("%.2f" % value)
