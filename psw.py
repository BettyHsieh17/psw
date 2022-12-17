#密碼重試程式
#password = 'a123456'
#讓使用者重複輸入密碼
#最多輸入3次
#如果正確 就印出"登入成功!"
#如果不正確 就印出 "密碼錯誤還有_次機會!"
password = 'a123456'
x = 1
while True:
	psd = input('請輸入密碼:')
	if psd == password:
		print ('登入成功')
		break #逃出迴圈
	else:
		print ('密碼錯誤! 還剩下', 3-x,'次機會')
		x = x + 1
		if x == 4:
			print('無法登入')
			break






