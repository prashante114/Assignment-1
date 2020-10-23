import pymysql




def connect_with_db():
	try:
		con = pymysql.connect(host='localhost', port=3306, user=root, passwd=root, db=route_data)
		if con:
			return con
		else:
			return False
	except Exception  as e:
		print (e)



def get_route_data(rout_data_list):
	try:
		con = connect_with_db()
		val = create_route_data()
		if con:
			user_query = 'INSERT INTO crud_app_routerproperties (id, sapid,hostname,loopback,macaddress) VALUES (%s,%s,%s,%s,%s)'
			cur = con.cursor(pymysql.cursors.DictCursor)
			cur.execute(user_query)
			
	
	except Exception  as e:
		print(e)

	finally:
		con.close()

def create_route_data():
	no_of_record = input("Enter no record you want INSERT")
	data_list = []
	if no_of_record:
		mac_id = "00:0a:95:9d:68:"
		sapid = 0
		host_name = "example.com"
		loopback ="69.89.31.226"
		for i in range (1,no_of_record):
			mac_id = mac_id + str(i)
			host_name = str(i) + host_name
			loopback = loopback + str(i)
			sapid = i
			data_list.append(i,sapid,host_name,loopback,mac_id)

		return data_list

