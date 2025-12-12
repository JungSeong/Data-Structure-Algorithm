import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub("[^0-9a-z-_.]", '', new_id)
    new_id = re.sub("[.]+", ".", new_id)
    new_id = re.sub("^[.]|[.]$", '', new_id)
    if len(new_id) == 0 : new_id = 'a'
    if len(new_id) >= 16 :
        new_id = new_id[:15]
        new_id = re.sub("[.]$", "", new_id)
    if len(new_id) <= 2 :
        while len(new_id) < 3 :
            new_id += new_id[-1]
    
    answer = new_id
    return answer