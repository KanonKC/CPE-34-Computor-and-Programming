print("Sub#1 Credit: 3 Grade:A\nSub#2 Credit: 1 Grade:B+\nInput => 3 A 1 B+")
score = [i for i in input("Input => ").split()] # 3 A 4 B

tCredit = 0
tGrade = 0

grader = {
    "char":['A','B+','B','C+','C','D+','D','F'],
    "grade":[4,3.5,3,2.5,2,1.5,1,0]
}

for i in range(0,len(score),2):
    tCredit += float(score[i])
    for j in range(len(grader["char"])):
        if score[i+1] == grader["char"][j]:
            tGrade += grader["grade"][j]*float(score[i])

print(f"Output: Total Credit = {tCredit:.1f} ,GPA = {tGrade/tCredit:.2f}")