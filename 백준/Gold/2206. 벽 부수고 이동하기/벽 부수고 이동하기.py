import sys
from collections import deque

def min_distance():
    que = deque([(1, 1, 1)]) # 시작위치 x = 1, y = 1, 벽을 깰 수 있는 기회 1

    while que:
        x, y, cnt = que.popleft()

        for r, c in move:
            # x+r이 1, n 사이의 값, y+c의 값이 1, m 사이의 값, 거리값이 음수면 이동가능
            if 0 < x+r <= n and 0 < y+c <= m and visited[x+r][y+c][cnt] < 0:
                
                # 다음 위치가 (n, m)이면 거리 반환
                if (x+r, y+c) == (n, m): return visited[x][y][cnt] + 1

                # 다음 위치가 이동이 가능하면 실행
                if not arr[x+r][y+c]:
                    visited[x+r][y+c][cnt] = visited[x][y][cnt] + 1
                    que.append((x+r, y+c, cnt))

                # 다음 위치가 벽이 있고 벽을 깰 수 있는 기회가 있으면 실행
                elif arr[x+r][y+c] and cnt:
                    visited[x+r][y+c][cnt-1] = visited[x][y][cnt] + 1
                    que.append((x+r, y+c, cnt-1))

    # (n, m)에 도착하지 못했다면 -1 반환
    return -1
    
n, m = map(int, sys.stdin.readline().strip().split())

arr = [[0]*(m+1)]
arr += [[0] + list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

# 0은 이동 가능, 1은 이동 불가(벽이 있는 곳)
# 상하좌우로 이동 가능 벽을 깰 수 있는 기회는 1번
# 최단 경로를 구하기
move = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우 순서로 이동배열 생성
visited = [[[-1]*2 for _ in range(m+1)] for _ in range(n+1)] # 방문배열 생성

visited[1][1][0], visited[1][1][1] = 1, 1 # (1, 1) 1로 초기화

if (1, 1) == (n, m): print(1)
else: print(min_distance())