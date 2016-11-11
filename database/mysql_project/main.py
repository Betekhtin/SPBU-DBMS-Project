#сделать проверку на пустоту!!!!
import csv
import mysql.connector
from mysql.connector import Error
from mysql.connector import MySQLConnection, Error
from mysql_config import connect

def insert_temperature(conn,cursor,date, city_id, T, Tn, Tx, Td, Tg):

    query = "INSERT INTO mydb.temperature(date, city_id, T, Tn, Tx, Td, Tg) " \
            "VALUES(%s,%s,%s,%s,%s,%s,%s)"
    args = (date, city_id, T, Tn, Tx, Td, Tg)

    try:

        cursor.execute(query, args)

        conn.commit()
    except Error as e:
        print('Error:', e)
def insert_weather(conn,cursor,date,city_id, WW, W1, W2):

    query = "INSERT INTO mydb.weather(date,city_id, WW, W1, W2) " \
            "VALUES(%s,%s,%s,%s,%s)"
    args = (date,city_id, WW, W1, W2)

    try:

        cursor.execute(query, args)

        conn.commit()
    except Error as e:
        print('Error:', e)
def insert_clouds(conn,cursor,date, city_id, N, Cl,Nh,H,Cm,Ch):

    query = "INSERT INTO mydb.clouds(date, city_id, N, Cl,Nh,H,Cm,Ch) " \
            "VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    args = (date, city_id, N, Cl,Nh,H,Cm,Ch)

    try:

        cursor.execute(query, args)

        conn.commit()
    except Error as e:
        print('Error:', e)
def insert_pressure(conn, cursor, date, city_id, P0,P,Pa):

        query = "INSERT INTO mydb.pressure(date, city_id, P0,P,Pa) " \
                "VALUES(%s,%s,%s,%s,%s)"
        args = (date, city_id, P0,P,Pa)

        try:

            cursor.execute(query, args)

            conn.commit()
        except Error as e:
            print('Error:', e)
def insert_wind(conn, cursor, date, city_id, DD,Ff,ff10,ff3):
    query = "INSERT INTO mydb.wind(date, city_id,DD,Ff,ff10,ff3) " \
            "VALUES(%s,%s,%s,%s,%s,%s)"
    args = (date, city_id, DD,Ff,ff10,ff3)

    try:

        cursor.execute(query, args)

        conn.commit()
    except Error as e:
        print('Error:', e)
def insert_other(conn, cursor, date, city_id, U,VV,RRR,tR,E,E_,sss):
    query = "INSERT INTO mydb.other_weather_data(date, city_id,U,VV,RRR,tR,E,E_,sss) " \
            "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    args = (date, city_id, U,VV,RRR,tR,E,E_,sss)

    try:

        cursor.execute(query, args)

        conn.commit()
    except Error as e:
        print('Error:', e)


def main():
    conn = connect()
    cursor = conn.cursor()
    csv_filename='/Users/Zharkov/Downloads/daty.csv'
    city_id=''
    with open(csv_filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for row in spamreader:
            row.pop()
            # print(', '.join(row))
            sss = row.pop()
            E_ = row.pop()
            Tg = row.pop()
            E = row.pop()
            tR = row.pop()
            RRR = row.pop()
            Td = row.pop()
            VV = row.pop()
            Ch = row.pop()
            Cm = row.pop()
            H = row.pop()
            Nh = row.pop()
            Cl = row.pop()
            Tx = row.pop()
            Tn = row.pop()
            W2 = row.pop()
            W1 = row.pop()
            WW = row.pop()
            N = row.pop()
            ff3 = row.pop()
            ff10 = row.pop()
            Ff = row.pop()
            DD = row.pop()
            U = row.pop()
            Pa = row.pop()
            P = row.pop()
            P0 = row.pop()
            T = row.pop()
            date = row.pop()
            tmp = date.split(' ')
            date = ('-'.join(tmp[0].split('.')[::-1])) + ' ' + tmp[1] + ':00'
            if (T!= Tn != Tx != Td != Tg != '') : insert_temperature(conn,cursor,date, city_id, T, Tn, Tx, Td, Tg)
            if (WW != W1 != W2 != '') : insert_weather(conn, cursor, date, city_id, WW, W1, W2)
            if ( N != Cl != Nh != H != Cm != Ch != ''): insert_clouds(conn, cursor, date, city_id, N, Cl, Nh, H, Cm, Ch)
            if (P0 != P != Pa != '') :  insert_pressure(conn, cursor, date, city_id, P0, P, Pa)
            if (DD != Ff != ff10 != ff3 != '') : insert_wind(conn, cursor, date, city_id, DD, Ff, ff10, ff3)
            if ( U != VV != RRR != tR != E != E_ != sss != '') : insert_other(conn, cursor, date, city_id, U, VV, RRR, tR, E, E_, sss)
    cursor.close()
    conn.close()
if __name__ == '__main__':
    main()