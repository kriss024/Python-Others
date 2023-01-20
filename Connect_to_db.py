import pprint

__author__ = 'Superuser'


import psycopg2
import sys

def main():

    conn_string = "host='localhost' dbname='postgres' user='postgres' password='root'"

    print "Connecting to database\n	->%s" % (conn_string)

    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    print "Connected!\n"

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather")
    records = cursor.fetchall()

    print "\nShow me the databases:\n"


    print "\nRows: \n"
    for row in records:

        print row[0],row[1],row[2],row[3],row[4]

if __name__ == "__main__":
    main()