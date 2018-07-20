import os

def read_score():
    if not os.path.isfile('123.txt'):
        return 0
 
    data = []
    with open('123.txt', 'r') as f:
        for line in f: 
            data.append(line.strip())
    return int(data[0])

# write
def save_score(score):
    with open('123.txt', 'w') as f:
        f.write(str(score))
        return max_score

