percent = input("enter the percentage marks of students:").split()
percent = [int(i) for i in percent]
print("Initial percentage tuple", str(percent))
passmark = []
failmark = []
for i in percent:
    if i >= 50:
        passmark.append(i)
    else:
        failmark.append(i)
print("Tuple of pass marks:", str(passmark))
print("Tuple of fail marks:", str(failmark))
