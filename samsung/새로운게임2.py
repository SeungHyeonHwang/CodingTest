# In[] : https://www.acmicpc.net/problem/17837
# 새로운 게임 2 

N, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
info = [list(map(int, input().split())) for _ in range(K)]


stack = [[[] for _ in range(N)] for _ in range(N)]
for i,p in enumerate(info):
    # k 저장 
    p[0] -= 1
    p[1] -= 1
    p[2] -= 1
    stack[p[0]][p[1]].extend([i])


dx = [0,0,-1,1]
dy = [1,-1,0,0]

def reverseDirection(direction) : 
    if direction == 0 or direction == 2: 
        return direction+1
    elif direction == 1 or direction == 3: 
        return direction-1


def stackCase(case,x,y,dx,dy,nx,ny,now) :
    global over
    
    if over:
        if case == 0 : 
            # 현재 말 위치부터 스택 위까지 이동
            for j in range(now, len(stack[x][y])) : 
                
                # 기존꺼 위에 현재꺼 쌓고
                stack[nx][ny].append(stack[x][y][j])
                info[stack[x][y][j]][0] = nx
                info[stack[x][y][j]][1] = ny
                
            #비우기
            temp = stack[x][y][:now]
            stack[x][y] = []
            stack[x][y] = temp
                
        elif case == 1:     
            temp_stack = []
            for j in range(now, len(stack[x][y])):
    
                temp = stack[x][y][j]
                temp_stack.append(temp)
                info[stack[x][y][j]][0] = nx
                info[stack[x][y][j]][1] = ny
     
            stack[nx][ny].extend(list(reversed(temp_stack)))
            temp = stack[x][y][:now]
            stack[x][y] = []
            stack[x][y] = temp
            
        elif case == 2:   
            rnx = x - dx[direction]
            rny = y - dy[direction]
            info[order][2] = reverseDirection(direction)
            
            if 0<= rnx < N and 0<= rny < N :
                if maps[rnx][rny] == 2 : info[order][2] = reverseDirection(direction)
                else :
                    if maps[rnx][rny] == 0 : stackCase(0, x, y, dx,dy,rnx, rny, now)
                    elif maps[rnx][rny] == 1 : stackCase(1, x, y, dx,dy,rnx, rny, now)

    for i in range(N):
        for j in range(N):
            if len(stack[i][j]) >= 4 :
                over = False
                break

cnt = 1
over = True 
while over :

    if cnt > 1001:
        print(-1)
        over = False
        break

    for order in range(K):
        # 현재 말 정보
        x, y, direction = info[order][0], info[order][1], info[order][2]
 
        # 다음 말 위치
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 몇번째 위치
        now = 0
        for j in range(len(stack[x][y])):
            if stack[x][y][j] == order : 
                # 몇번째인지
                now = j 
                
        # # 범위를 벗어나면 (파) 
        if nx >= N or nx < 0 or ny >= N or ny < 0 : 
            stackCase(2, x, y, dx, dy, nx, ny, now)
        # 흰
        elif maps[nx][ny] == 0 : 
            stackCase(0, x, y, dx, dy, nx, ny, now)
        # 빨
        elif maps[nx][ny] == 1 : 
            stackCase(1, x, y, dx, dy, nx, ny, now)             
        # 파 
        elif maps[nx][ny] == 2 : 
            stackCase(2, x, y, dx, dy, nx, ny, now)
          
    if over == False : 
        print(cnt)  
        break
    cnt +=1
