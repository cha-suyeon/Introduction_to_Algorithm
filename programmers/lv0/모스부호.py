# 모스부호(1)
# 1
morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}

def solution(letter):
    answer = []
    lst = letter.split(' ')
    for i in lst:
        answer.append(morse[i])
    answer = ''.join(answer)
    return answer

print(solution(".... . .-.. .-.. ---"))

# 2
def solution(letter):
    answer = ''

    morse = { 
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }
    
    letter_ls = letter.split()
    for l in letter_ls:
        answer += morse[l]
        
    return answer

print(solution(".... . .-.. .-.. ---"))

# 3
def solution(letter):
    return "".join(map(lambda w: morse[w], letter.split())) 
