# 가위 바위 보
# 1
def solution(rsp):
    answer = ''
    for i in rsp:
        if i == '2':
            answer += '0'
            
        elif i == '0':
            answer += '5'
        else:
            answer += '2'
    return answer

# 2
def solution(rsp: str) -> str:
    dict = {"2": "0", "0": "5", "5": "2"}

    return "".join(map(str, [dict[x] for x in rsp]))

if __name__ == '__main__':
    print(solution("2"))    # "0"
    print(solution("205"))  # "052"
    
# 3
def solution(rsp):
    rsp =rsp.replace('2','s')
    rsp =rsp.replace('5','p')
    rsp =rsp.replace('0','r')
    rsp =rsp.replace('r','5')
    rsp =rsp.replace('s','0')
    rsp =rsp.replace('p','2')
    return rsp

# 4
def solution(rsp):
    d = {'0':'5', '2':'0', '5':'2'}
    return ''.join(d[i] for i in rsp)