# -*- coding: utf-8 -*-
import csv
import sqlite3
from sqlite3 import Error

def insert_temperature(conn,cursor,date, city_id, T, Tn, Tx, Td, Tg):

    query = "INSERT INTO temperature(date, city_id, T, Tn, Tx, Td, Tg) " \
            "VALUES(?,?,?,?,?,?,?)"
    args = (date, city_id, T, Tn, Tx, Td, Tg)

    try:

        cursor.execute(query, args)

        conn.commit()
    except Error as e:
        print('Error:', e)
        print(args)
def insert_weather(conn,cursor,date,city_id, WW, W1, W2):

    query = "INSERT INTO weather(date,city_id, WW, W1, W2) " \
            "VALUES(?,?,?,?,?)"
    args = (date,city_id, WW, W1, W2)

    try:

        cursor.execute(query, args)

        conn.commit()
    except Error as e:
        print('Error:', e)
        print(args)
def insert_clouds(conn,cursor,date, city_id, N, Cl,Nh,H,Cm,Ch):

    query = "INSERT INTO clouds(date, city_id, N, Cl,Nh,H,Cm,Ch) " \
            "VALUES(?,?,?,?,?,?,?,?)"
    args = (date, city_id, N, Cl,Nh,H,Cm,Ch)

    try:

        cursor.execute(query, args)

        conn.commit()
    except Error as e:
        print('Error:', e)
        print(args)
def insert_pressure(conn, cursor, date, city_id, P0,P,Pa):

        query = "INSERT INTO pressure(date, city_id, P0,P,Pa) " \
                "VALUES(?,?,?,?,?)"
        args = (date, city_id, P0,P,Pa)

        try:

            cursor.execute(query, args)

            conn.commit()
        except Error as e:
            print('Error:', e)
            print(args)
def insert_wind(conn, cursor, date, city_id, DD,Ff,ff10,ff3):
    query = "INSERT INTO wind(date, city_id,DD,Ff,ff10,ff3) " \
            "VALUES(?,?,?,?,?,?)"
    args = (date, city_id, DD,Ff,ff10,ff3)

    try:

        cursor.execute(query, args)

        conn.commit()
    except Error as e:
        print('Error:', e)
        print(args)
def insert_other(conn, cursor, date, city_id, U,VV,RRR,tR,E,E_,sss):
    query = "INSERT INTO other_weather_data(date, city_id,U,VV,RRR,tR,E,E1,sss) " \
            "VALUES(?,?,?,?,?,?,?,?,?)"
    args = (date, city_id, U,VV,RRR,tR,E,E_,sss)

    try:

        cursor.execute(query, args)

        conn.commit()
    except Error as e:
        print('Error:', e)
        print(args)
def insert_country(conn, cursor,country_id, country_name):
    query = "INSERT INTO country(country_id,country_name) " \
            "VALUES(?,?)"
    args =(country_id, country_name)

    try:

        cursor.execute(query,args)

        conn.commit()
    except Error as e:
        print('Error:', e)
def insert_city(conn, cursor,city_id, country_id, city_name):
    query = "INSERT INTO city(city_id, country_id, city_name) " \
            "VALUES(?,?,?)"
    args =(city_id,country_id, city_name)

    try:

        cursor.execute(query,args)

        conn.commit()
    except Error as e:
        print('Error:', e)

def main():
    conn = sqlite3.connect('mydb.sqlite3')
    cursor = conn.cursor()
    insert_country(conn,cursor,'1','Россия');
    insert_city(conn,cursor,'1','1', 'Санкт-Петербург');
    insert_city(conn,cursor,'2','1', 'Москва');
    insert_country(conn,cursor,'2','США');
    insert_city(conn,cursor,'3','2', 'Нью-Йорк');
    insert_city(conn,cursor,'4','2', 'Сан-Франциско');
    insert_country(conn,cursor,'3','Китай');
    insert_city(conn,cursor,'5','3', 'Пекин');
    insert_city(conn,cursor,'6','3', 'Шанхай');
    csv_filename = []
    csv_filename.append('csv-data/russia_spb.csv');
    csv_filename.append('csv-data/russia_moscow.csv');
    csv_filename.append('csv-data/usa_new_york.csv');
    csv_filename.append('csv-data/usa_san_francisco.csv');
    csv_filename.append('csv-data/china_beijing.csv');
    csv_filename.append('csv-data/china_shanghai.csv');
    i=1
    while i <= 6:
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
                # if not(T== Tn == Tx == Td == Tg == "") :
                insert_temperature(conn,cursor,date, city_id, T, Tn, Tx, Td, Tg)
                # if not(WW == W1 == W2 == "") :
                insert_weather(conn, cursor, date, city_id, WW, W1, W2)
                # if not( N == Cl == Nh == H == Cm == Ch == ""):
                insert_clouds(conn, cursor, date, city_id, N, Cl, Nh, H, Cm, Ch)
                # if not(P0 == P == Pa == "") :
                insert_pressure(conn, cursor, date, city_id, P0, P, Pa)
                # if not(DD == Ff == ff10 == ff3 == "") :
                insert_wind(conn, cursor, date, city_id, DD, Ff, ff10, ff3)
                # if not( U == VV == RRR == tR == E == E_ == sss == "") :
                insert_other(conn, cursor, date, city_id, U, VV, RRR, tR, E, E_, sss)
        i = i + 1
    cursor.close()
    conn.close()
if __name__ == '__main__':
    main()