



def move(x,y,d):
    while True : 
        nx,ny = x+dx[d],y+dy[d]
        if 0>=nx or 0>=ny or nx>=n-1 or ny>=m-1 or maps[nx][ny]!='.': 
            x,y = nx-dx[d],ny-dy[d]
            break
    return [x,y,d]

def bmove(r,b,d,cnt,flag):
    [nx,ny,d] = move(b[0],b[1],d)
    if 0<nx<n-1 and 0<ny<m-1 :
        if maps[nx][ny]=='O':
            flag[0]=1
            return [r,b,d,cnt,flag]
        elif maps[nx][ny]=='.' :
            return [r,b,d,cnt,flag]
        elif nx==r[0] and ny==r[1]:
            [r,b,d,cnt,flag] = bmove(r,b,d,cnt,flag)
            return [r,b,d,cnt,flag]
    else :
        for i in range(4):
            if i!= d :
                pass

def rmove(r,b,d,cnt,flag):
    [nx,ny,d] = move(r[0],r[1],d)
    if r[0]==nx and r[1]==ny :
        return [r,b,d,cnt,flag]
    if maps[nx][ny]=='O':
        flag[1]=1
        return bmove([nx,ny],b,d,cnt,flag)

    else :
        for i in range(4):
            if i!= d : 
                nx, ny = r[0]+dx[i], r[1]+dy[i]
                if maps[nx][ny]=='O':
                    flag[1]=1
                    return bmove([nx,ny],b,d,cnt+1,flag)
                elif maps[nx][ny]=='.' :
                    return bmove([nx,ny],b,d,cnt+1,flag)
                elif nx==b[0] and ny==b[1]:
                    return bmove(r,b,d,cnt+1,flag)

def solution(n,m):
    cnt = 1
    d=0
    while True : 
        r = rmove(R,B,O,d,cnt,flag)
        if r[0][0] == R[0] and r[0][1] == R[1]:
            d=(d+1)%4
        R,B,O,d,cnt,flag = r[0],r[1],r[2],r[3],r[4]
        b = bmove(R,B,O,d,cnt,flag)
        R,B,O,d,cnt,flag = b[0],b[1],b[2],b[3],b[4]
        if flag == [1,0] :
            answer = min(answer, cnt)
            break
        if flag == [0,1] or flag == [1,1]:
            break
    return answer if answer!=int(1e9) else -1

R,B,O = [],[],[]
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'R': R = [i,j]
        elif maps[i][j] == 'B': B = [i,j]
        elif maps[i][j] == 'O': O = [i,j]
flag = [0,0]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
answer = int(1e9)
n,m = map(int, input().split())
maps = [list(map(str, input().split()))]

print(solution(n,m))