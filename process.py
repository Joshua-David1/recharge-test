def process_data(username,password):
	arr = []
	if username is None:
		return username,password
		
	for i in password:
		arr.append(i)
	
	for i in username:
		arr.append(i)

	username=""
	for i in range(len(arr)-1,len(arr)-4,-1):
		username+=arr[i]
	
	password=""
	for i in  range(len(arr)-4,len(arr)-14,-1):
		password+=arr[i]
	
	return username,password
