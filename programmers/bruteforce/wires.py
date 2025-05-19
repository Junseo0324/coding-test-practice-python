'''
n 개의 송전탑이 전선을 통해 하나의 트리 형태로 연결
이 전선들 중 하나를 끊어 현재의 전력망 네트워크를 2개로 분할
두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추고자 함.
n = 송전탑 개수 /  전선 정보 = wires

가장 비슷할 때 두 전력망이 가지고 있는 송전탑 개수의 차이(절댓값)를 return
wires 는 길이가 n-1 / [v1,v2] -> 1 <= v1 < v2 <= n
1 -> 3이랑 연결 , 2 -> 3이랑 연결 이런식?
dfs 이용(?)
for 문 n번
    count를 세서 그 count 끼리의 차이값 저장
for문이 끝날 때 min(count,answer)해서
최솟값을 return
'''

def solution(n, wires):
    answer = -1
    return answer


def dfs(x,visited):

