import MySQLdb
 
try:
	# conn=MySQLdb.connect(host='localhost',user='root',passwd='xx',db='test',port=3306)
	conn=MySQLdb.connect(host='localhost',user='root',passwd='xx',port=3306)
	cur=conn.cursor()

	cur.execute('create database if not exists py_MYSQLTest')
	conn.select_db('py_MYSQLTest')
	cur.execute('create table test(id int,info varchar(20))')
	print('11111111111111111111')

	value=[1,'hi rollen']
	cur.execute('insert into test values(%s,%s)',value)
	
	values=[]
	for i in range(20):
		values.append((i,'hi rollen'+str(i)))
	cur.executemany('insert into test values(%s,%s)',values)

	cur.execute('update test set info="I am rollen" where id=3')

	conn.commit()
	cur.close()
	conn.close()
except MySQLdb.Error,e:
	print "Mysql Error %d: %s" % (e.args[0], e.args[1])

