# student score checker 
def check_score():
    students = ["nick", "allen", "steve", "cortez", "zaman"]
    scores = [78, 45, 90, 49, 50]

    for i in range(len(students)):
        name = students[i]
        score = scores[i]
        
        if score >=80:
            print(name, "passed with flying colors", score)
        elif score >=50:
            print(name, "passed with", score)
        else:
            print(name, "failed with", score)

check_score()