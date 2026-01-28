marks = {"math": 80, "science": 90, "english": 75}
for subject,score in marks.items():
    print(subject,":", score)
    
    
total=0
for score in marks.values():
     total+=score

print(total)
