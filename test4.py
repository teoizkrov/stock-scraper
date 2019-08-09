import mysql.connector

try:
    cnx = mysql.connector.connect( host='localhost', user='root', password='123', database='wsj' )
    cursor = cnx.cursor()
    cursor.execute( 'SELECT * FROM stocks ).format('AMD')
    r = cursor.fetchone()
    print( r ) 
    cnx.close()
except mysql.connector.Error as err:
    print( err ) 

