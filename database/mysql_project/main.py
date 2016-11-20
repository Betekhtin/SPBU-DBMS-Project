# -*- coding: utf-8 -*-
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
def insert_country(conn, cursor,country_id, country_name):
    query = "INSERT INTO mydb.country(country_id,country_name) " \
            "VALUES(%s,%s)"
    args = (country_id,country_name)

    try:

        cursor.execute(query, args)

        conn.commit()
    except Error as e:
        print('Error:', e)
def insert_city(conn, cursor, country_id, city_name):
    query = "INSERT INTO mydb.city(country_id, city_name) " \
            "VALUES(%s,%s)"
    args = (country_id, city_name)

    try:

        cursor.execute(query, args)

        conn.commit()
    except Error as e:
        print('Error:', e)

def main():
    conn = connect()
    cursor = conn.cursor()
    insert_country(conn,cursor,'1','Россия');
    insert_city(conn,cursor,'1', 'Санкт-Петербург');
    insert_city(conn,cursor,'1', 'Москва');
    insert_country(conn,cursor,'2','США');
    insert_city(conn,cursor,'2', 'Нью-Йорк');
    insert_city(conn,cursor,'2', 'Сан-Франциско');
    insert_country(conn,cursor,'3','Китай');
    insert_city(conn,cursor,'3', 'Пекин');
    insert_city(conn,cursor,'3', 'Шанхай');
    csv_filename = []
    csv_filename.append('csv-data/russia_spb.csv');
    csv_filename.append('csv-data/russia_moscow.csv');
    csv_filename.append('csv-data/usa_new_york.csv');
    csv_filename.append('csv-data/usa_san_francisco.csv');
    csv_filename.append('csv-data/china_beijing.csv');
    csv_filename.append('csv-data/china_shanghai.csv');
    i=1
    while i < 6:
        city_id=str(i)
        with open(csv_filename[i-1], newline='', encoding='utf-8') as csvfile:
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
                if not(T== Tn == Tx == Td == Tg == "") : insert_temperature(conn,cursor,date, city_id, T, Tn, Tx, Td, Tg)
                if not(WW == W1 == W2 == "") : insert_weather(conn, cursor, date, city_id, WW, W1, W2)
                if not( N == Cl == Nh == H == Cm == Ch == ""): insert_clouds(conn, cursor, date, city_id, N, Cl, Nh, H, Cm, Ch)
                if not(P0 == P == Pa == "") :  insert_pressure(conn, cursor, date, city_id, P0, P, Pa)
                if not(DD == Ff == ff10 == ff3 == "") : insert_wind(conn, cursor, date, city_id, DD, Ff, ff10, ff3)
                if not( U == VV == RRR == tR == E == E_ == sss == "") : insert_other(conn, cursor, date, city_id, U, VV, RRR, tR, E, E_, sss)
        i = i + 1
    cursor.close()
    conn.close()
if __name__ == '__main__':
    main()