from xml.dom.minidom import parse
from sys import argv
import mysql.connector
#no module named mysql.connector



def traverse( cursor ): 
    
    doc = parse( argv[1] ) 
    table = doc.getElementsByTagName( 'table' ) 
    
    #print( 'exchange,symbol,company,volume,price,change' )
    for tr in table[2].getElementsByTagName( 'tr' )[1:]:
        ara=[] # fufu~
        for td in tr.getElementsByTagName( 'td' ): 
            for a in td.getElementsByTagName( 'a' ): 
                for text in a.childNodes:
                    s = text.nodeValue 
                    s = s.replace( ')', '').strip().split('(')
                    s[0] = s[0].strip()
                    s[0] = s[0].replace("'", "\'")
                    ara.append( "Nasdaq" )
                    ara.append( s[1] )
                    ara.append( s[0] )
            for node in td.childNodes:  
                if node.nodeType == node.TEXT_NODE and node.nodeValue != '\n':
                    ara.append( node.nodeValue.strip( '$' ).replace( ',', '' ) )
        cursor.execute( "SELECT * FROM stocks " 'WHERE company="%s"' %( ara[3] ) )
        r = cursor.fetchone()
        if r is not None:
            update( cursor, ara )
            cnx.commit()
        else:
            insert( cursor, ara )
            cnx.commit()
    doc.unlink()

def insert( cursor, ara ):

        query = """
        INSERT INTO stocks
            ( exchange, symbol, company, volume, price, chang )
        VALUES
            ( %s, %s, %s, %s, %s, %s )
        """
        cursor.execute( query, ( ara[1], ara[2], ara[3], float( ara[4] ), float ( ara[5] ),float ( ara[6] ) ) )

def update( cursor, ara ):
    query = "UPDATE stocks SET volume=%s, price=%s, chang=%s WHERE company=%s"
    cursor.execute( query, ( float( ara[4] ), float( ara[5] ), float( ara[6] ), ara[3] ) )

try:
    cnx = mysql.connector.connect( host='localhost', user='root', password='123', database='wsj' )
    cursor = cnx.cursor()
    traverse( cursor )
    cnx.close()
except mysql.connector.Error as err:
    print( err )
finally:
    try:
        cnx
    except NameError:
        pass
    else:
        cnx.close()

'''

        # IF ROW COUNT == 1 THEN IT EXISTS THEN UPDATE
        # ELSE INSERT
        print( r ) 
        #cursor.execute( query, ( ara[1], ara[2], ara[3], float( ara[4] ), float( ara[5] ), float( ara[6] ) ) )
       # print( ara ) # ','.join( ara[1:4] ) 1-6


'''
