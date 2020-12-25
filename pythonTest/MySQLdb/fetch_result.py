import MySQLdb
 
try:
    '''
    conn=MySQLdb.connect(host='localhost',user='root',passwd='shadow33',port=3306)
    cur=conn.cursor()
    conn.select_db('py_MYSQLTest')
    '''

    # charset='gb2312'
    conn = MySQLdb.Connect(host='localhost', user='root', passwd='shadow33', db='py_MYSQLTest',charset='utf8') 
    cur=conn.cursor()

    # count=cur.execute('select * from test')
    # print 'there has %s rows record' % count

    id="1"
    name ="hi rollen"
    count=cur.execute("select * from test where id ='%s' and info = '%s'"%(id,name))
    # count=cur.execute("select * from test where id ='1' and info = 'hi rollen'")
    
    
    result=cur.fetchone()
    print result
    print 'ID: %s info: %s' % result
    print('----------------------------')
 
    results=cur.fetchmany(5)
    print(results)
    for r in results:
        print r
    print('----------------------------')
    '''
    print '=='*10
    # cur.scroll(0,mode='absolute')
    cur.scroll(18,mode='absolute')
 
    results=cur.fetchall()
    print(results)
    for r in results:
        print r[1]
    '''

    conn.commit()
    cur.close()
    conn.close()
 
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])