#-*- coding:UTF-8 -*-
import MySQLdb

def insert():
	try:
		# conn=MySQLdb.connect(host='localhost',user='root',passwd='shadow33',db='test',port=3306)
		conn=MySQLdb.connect(host='172.27.35.11',user='root',passwd='shadow33',port=3306,db='test',charset='utf8')
		cur=conn.cursor()

		
		values=[]
		for i in range(100):
			values.append((i,'mysqlbook'+str(i),'iiiii'))
		cur.executemany('insert into books (id,name,author) values(%s,%s,%s)',values)



		conn.commit()
		cur.close()
		conn.close()
	except MySQLdb.Error,e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

if __name__ == "__main__":
	# values=[]
	# for i in range(5):
	# 	values.append((i,'mysqlbook'+str(i),'iii'))
	# print(values)
	insert()