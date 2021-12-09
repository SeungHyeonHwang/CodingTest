"""
1 31
2 28
3 31
4 30
5 31
6 30
7 31
8 30
9 31
10 30
11 31
12 30 
"""

def make_calander(eventMonth, eventDay, eventWeek):
	week = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
	week_dict = {i:string for i,string in enumerate(week)}
	offset_dict = {string:i for i,string in enumerate(week)}
	offset = offset_dict[eventWeek]
	calander = dict()
	if eventMonth == 2 : 
		for i in range(eventDay,29):
			calander[i] =  [week_dict[(i-eventDay+offset)%7], 0]
	elif eventMonth%2 == 1 : 
		for i in range(eventDay,32):
			calander[i] = [week_dict[(i-eventDay+offset)%7], 0]
	else : 
		for i in range(eventDay,31):
			calander[i] = [week_dict[(i-eventDay+offset)%7], 0]
	return calander

def solution(start_day, days):
	answer = 0
	eventWeek = start_day[:3]
	eventMonth = int(start_day[4:].split('/')[0])
	eventDay = int(start_day[4:].split('/')[1])

	calander = make_calander(eventMonth, eventDay, eventWeek)

	for info in days:
		mon = int(info.split('/')[0])
		day = int(info.split('/')[1])
		#week = [eventDay+day%7]
		if day in calander :
			calander[day][1] = 1
	temp = 0
	print(calander)
	for i in range(eventDay, len(calander)):
		if calander[i][1] :
			if calander[i][0] not in ["SAT","SUN"] : 
				temp+=1
			answer = max(answer, temp)
		else :
			if calander[i][0] not in ["SAT","SUN"] : 
				temp = 0
	return answer
		
# 이벤트 시작일 
start_day = "MON 05/04"
# 접속일
temp = "05/06 05/02 05/10 05/07 05/08 05/13 05/12 05/20 06/01 05/30"
days = list(temp.split())
print(solution(start_day, days))
# output = 3 

start_day = "THU 05/06"
# 접속일
temp = "05/06 05/02 05/10 05/07 05/08 05/13 05/16 05/20 06/01 05/30 05/11"
days = list(temp.split())
print(solution(start_day, days))

# 5->6월 넘어가는 시점 추가해야함