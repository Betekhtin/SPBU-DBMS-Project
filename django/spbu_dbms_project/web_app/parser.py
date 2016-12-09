import lxml.html as html
import sqlite3
from sqlite3 import Error

from web_app import models
import datetime
def myopen_http(method, url, values):
   if not url:
      raise ValueError("cannot submit, no URL provided")
   ## FIXME: should test that it's not a relative URL or something
   try:
      from urllib import urlencode, urlopen
   except ImportError: # Python 3
      from urllib.request import urlopen
      from urllib.parse import urlencode
   if method == 'GET':
      if '?' in url:
         url += '&'
      else:
         url += '?'
         url += urlencode(values)
         data = None
   else:
      data = urlencode(values).encode('utf-8')

   return urlopen(url, data)
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

#source_date = '03-12-2016'
#source_page='http://rp5.ru/%D0%90%D1%80%D1%85%D0%B8%D0%B2_%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D1%8B_%D0%B2_%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D0%B5'
def parser(source_date, source_page, city_id):
    conn = sqlite3.connect('mydb.sqlite3')
    cursor = conn.cursor()
    page = html.parse(source_page)
    form=page.getroot().forms[3]
    form.fields['ArchDate'] = source_date.encode('utf-8')
    result = html.parse(html.submit_form(form, open_http=myopen_http))
    if (int(city_id)==4):
        costili=4
    # elif (int(city_id)==5):
    #     costili=9
    else: costili=8
    tr_blocks = result.getroot().get_element_by_id('archiveTable')[1:(costili+1)]
    i=0
    tmp = source_date.split('-')
    date = tmp[2] + '-' + tmp[1] + '-' + tmp[0] + ' ' + tr_blocks[i].getchildren()[1].text_content() + ':00:00'
    try: T = (tr_blocks[i].getchildren()[2][0].text_content())
    except IndexError: T=''
    try: P0 = (tr_blocks[i].getchildren()[3][0].text_content())
    except IndexError: P0=''
    try: P = (tr_blocks[i].getchildren()[4][0].text_content())
    except IndexError: P=''
    try: Pa = (tr_blocks[i].getchildren()[5][0].text_content())
    except IndexError: Pa=''
    try: U = (tr_blocks[i].getchildren()[6][0].text_content())
    except IndexError: U=''
    try: DD = (tr_blocks[i].getchildren()[7].text_content())
    except IndexError: DD=''
    try: Ff = (tr_blocks[i].getchildren()[8][0].text_content()).replace('(', '').replace(')', '').lstrip().split(' ')[0]
    except IndexError: Ff=''
    try: ff10 = (tr_blocks[i].getchildren()[9].text_content()).split(' ')[0].rstrip()
    except IndexError: ff10=''
    try: ff3 = (tr_blocks[i].getchildren()[10].text_content()).split(' ')[0].rstrip()
    except IndexError: ff3=''
    try: N = (tr_blocks[i].getchildren()[11][0].text_content())  # важно что это не проценты а варчар
    except IndexError: N=''
    try: WW = (tr_blocks[i].getchildren()[12].text_content())
    except IndexError: WW=''
    try: W1 = (tr_blocks[i].getchildren()[13].text_content())
    except IndexError: W1=''
    try: W2 = (tr_blocks[i].getchildren()[14].text_content())
    except IndexError: W2=''
    try: Tn = (tr_blocks[i].getchildren()[15].text_content()).split(' ')[0].rstrip()
    except IndexError: Tn=''
    try: Tx = (tr_blocks[i].getchildren()[16].text_content()).split(' ')[0].rstrip()
    except IndexError: Tx=''
    try: Cl = (tr_blocks[i].getchildren()[17].text_content())
    except IndexError: Cl=''
    try: Nh = (tr_blocks[i].getchildren()[18][0].text_content())
    except IndexError: Nh=''
    try: H = (tr_blocks[i].getchildren()[19][0].text_content())
    except IndexError: H=''
    try: Cm = (tr_blocks[i].getchildren()[20].text_content())
    except IndexError: Cm=''
    try: Ch = (tr_blocks[i].getchildren()[21].text_content())
    except IndexError: Ch=''
    try: VV = (tr_blocks[i].getchildren()[22][0].text_content())
    except IndexError: VV=''
    try: Td = (tr_blocks[i].getchildren()[23][0].text_content())
    except IndexError: Td=''
    try: RRR = (tr_blocks[i].getchildren()[24][0].text_content())
    except IndexError: RRR=''
    try: tR = (tr_blocks[i].getchildren()[25].text_content())
    except IndexError: tR=''
    try: E = (tr_blocks[i].getchildren()[26].text_content())
    except IndexError: E=''
    try: Tg = (tr_blocks[i].getchildren()[27].text_content()).split(' ')[0].rstrip()
    except IndexError: Tg=''
    try: E1 = (tr_blocks[i].getchildren()[28].text_content())
    except IndexError: E1=''
    try: sss = (tr_blocks[i].getchildren()[29].text_content())
    except IndexError: sss=''
    #print(date, T)
    #data = models.temperature(date=(date), city_id=1, T=float(T), Tn=float(Tn), Tx=float(Tx), Td=float(Td), Tg=float(Tg))
    #data.save()
    #print(float(T))
    insert_temperature(conn, cursor, date, city_id, T, Tn, Tx, Td, Tg)
    insert_weather(conn, cursor, date, city_id, WW, W1, W2)
    insert_clouds(conn, cursor, date, city_id, N, Cl, Nh, H, Cm, Ch)
    insert_pressure(conn, cursor, date, city_id, P0, P, Pa)
    insert_wind(conn, cursor, date, city_id, DD, Ff, ff10, ff3)
    insert_other(conn, cursor, date, city_id, U, VV, RRR, tR, E, E1, sss)
    i=1

    while i<costili:
        tmp=source_date.split('-')
        date = tmp[2] + '-'+ tmp[1] + '-' + tmp[0]+' '+tr_blocks[i].getchildren()[0].text_content() + ':00:00'
        try:
            T = (tr_blocks[i].getchildren()[1][0].text_content())
        except IndexError:
            T = ''
        try:
            P0 = (tr_blocks[i].getchildren()[2][0].text_content())
        except IndexError:
            P0 = ''
        try:
            P = (tr_blocks[i].getchildren()[3][0].text_content())
        except IndexError:
            P = ''
        try:
            Pa = (tr_blocks[i].getchildren()[4][0].text_content())
        except IndexError:
            Pa = ''
        try:
            U = (tr_blocks[i].getchildren()[5][0].text_content())
        except IndexError:
            U = ''
        try:
            DD = (tr_blocks[i].getchildren()[6].text_content())
        except IndexError:
            DD = ''
        try:
            Ff = (tr_blocks[i].getchildren()[7][0].text_content()).replace('(', '').replace(')', '').lstrip().split(' ')[0]
        except IndexError:
            Ff = ''
        try:
            ff10 = (tr_blocks[i].getchildren()[8].text_content()).split(' ')[0].rstrip()
        except IndexError:
            ff10 = ''
        try:
            ff3 = (tr_blocks[i].getchildren()[9].text_content()).split(' ')[0].rstrip()
        except IndexError:
            ff3 = ''
        try:
            N = (tr_blocks[i].getchildren()[10][0].text_content())  # важно что это не проценты а варчар
        except IndexError:
            N = ''
        try:
            WW = (tr_blocks[i].getchildren()[11].text_content())
        except IndexError:
            WW = ''
        try:
            W1 = (tr_blocks[i].getchildren()[12].text_content())
        except IndexError:
            W1 = ''
        try:
            W2 = (tr_blocks[i].getchildren()[13].text_content())
        except IndexError:
            W2 = ''
        try:
            Tn = (tr_blocks[i].getchildren()[14].text_content()).split(' ')[0].rstrip()
        except IndexError:
            Tn = ''
        try:
            Tx = (tr_blocks[i].getchildren()[15].text_content()).split(' ')[0].rstrip()
        except IndexError:
            Tx = ''
        try:
            Cl = (tr_blocks[i].getchildren()[16].text_content())
        except IndexError:
            Cl = ''
        try:
            Nh = (tr_blocks[i].getchildren()[17][0].text_content())
        except IndexError:
            Nh = ''
        try:
            H = (tr_blocks[i].getchildren()[18][0].text_content())
        except IndexError:
            H = ''
        try:
            Cm = (tr_blocks[i].getchildren()[19].text_content())
        except IndexError:
            Cm = ''
        try:
            Ch = (tr_blocks[i].getchildren()[20].text_content())
        except IndexError:
            Ch = ''
        try:
            VV = (tr_blocks[i].getchildren()[21][0].text_content())
        except IndexError:
            VV = ''
        try:
            Td = (tr_blocks[i].getchildren()[22][0].text_content())
        except IndexError:
            Td = ''
        try:
            RRR = (tr_blocks[i].getchildren()[23][0].text_content())
        except IndexError:
            RRR = ''
        try:
            tR = (tr_blocks[i].getchildren()[24].text_content())
        except IndexError:
            tR = ''
        try:
            E = (tr_blocks[i].getchildren()[25].text_content())
        except IndexError:
            E = ''
        try:
            Tg = (tr_blocks[i].getchildren()[26].text_content()).split(' ')[0].rstrip()
        except IndexError:
            Tg = ''
        try:
            E1 = (tr_blocks[i].getchildren()[27].text_content())
        except IndexError:
            E1 = ''
        try:
            sss = (tr_blocks[i].getchildren()[28].text_content())
        except IndexError:
            sss = ''
        #print(date, T)
        insert_temperature(conn, cursor, date, city_id, T, Tn, Tx, Td, Tg)
        insert_weather(conn, cursor, date, city_id, WW, W1, W2)
        insert_clouds(conn, cursor, date, city_id, N, Cl, Nh, H, Cm, Ch)
        insert_pressure(conn, cursor, date, city_id, P0, P, Pa)
        insert_wind(conn, cursor, date, city_id, DD, Ff, ff10, ff3)
        insert_other(conn, cursor, date, city_id, U, VV, RRR, tR, E, E1, sss)
        i=i+1
    cursor.close()
    conn.close()