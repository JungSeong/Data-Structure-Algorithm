def solution(new_id):
    answer = ''
    first = new_id.lower()
    available_ch = ['-','_','.']
    
    second = ''
    for ch in first :
        if not ch.isalpha() and ch in available_ch :
            second += ch
        elif ch.isalpha() or ch.isdigit() :
            second += ch
            
    print(second)
            
    third = ''
    for i in range(len(second)) :
        if len(third) != 0 and third[-1] == '.' and second[i] == '.' :
            continue
        else :
            third += second[i]
    
    print(third)

    fourth = ''
    for i in range(len(third)) :
        if i == 0 or i == len(third)-1 :
            if third[i] == '.' :
                continue
            else :
                fourth += third[i]
        else :
            fourth += third[i]
            
    print(fourth)
            
    fifth = ''
    if fourth == '' :
        fifth = fourth + 'a'
    else :
        fifth = fourth
        
    print(fifth)
    
    sixth = fifth
    if len(fifth) >= 16 :
        sixth = fifth[:15]
        if sixth[-1] == '.' :
            sixth = sixth[:-1]
    
    seventh = sixth
    if len(seventh) <= 2 :
        while len(seventh) < 3 :
            seventh += seventh[-1]
            
    answer = seventh
    
    return answer