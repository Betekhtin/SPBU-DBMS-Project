import lxml.html as html
from pandas import DataFrame

output_d=open('wr_spb.html','wb')
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


#
# main_domain_stat='file:///Users/Zharkov/Downloads/test2.htm'
#
# page=html.parse(main_domain_stat)
#
# e = page.getroot().\
#         find_class('cl_hr').\
#         pop()
#
# t=e.getchildren().pop()
#
# print(e, t)
source_date = '03-12-2016'
page = html.parse("http://rp5.ru/%D0%90%D1%80%D1%85%D0%B8%D0%B2_%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D1%8B_%D0%B2_%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D0%B5")

form=page.getroot().forms[3]
form.fields['ArchDate'] = source_date.encode('utf-8')
#form.fields['pe'] = '1'.encode('utf-8')
result = html.parse(html.submit_form(form, open_http=myopen_http))
#test = result.getroot().get_element_by_id('archiveTable')[2].getchildren()[3].text_content()
#-------------
tr_blocks = result.getroot().get_element_by_id('archiveTable')[1:9]
i=0
tmp = source_date.split('-')
date = tmp[2] + '-' + tmp[1] + '-' + tmp[0] + ' ' + tr_blocks[i].getchildren()[1].text_content() + ':00'
T = (tr_blocks[i].getchildren()[2].text_content()).split(' ')[0].rstrip()
P0 = (tr_blocks[i].getchildren()[3].text_content()).split(' ')[0].rstrip()
P = (tr_blocks[i].getchildren()[4].text_content()).split(' ')[0].rstrip()
Pa = (tr_blocks[i].getchildren()[5].text_content()).split(' ')[0].rstrip()
U = (tr_blocks[i].getchildren()[6].text_content()).split(' ')[0].rstrip()
DD = (tr_blocks[i].getchildren()[7].text_content())
Ff = (tr_blocks[i].getchildren()[8].text_content()).split(')')[0] + ')'
ff10 = (tr_blocks[i].getchildren()[9].text_content()).split(' ')[0].rstrip()
ff3 = (tr_blocks[i].getchildren()[10].text_content()).split(' ')[0].rstrip()
N = (tr_blocks[i].getchildren()[11].text_content()).split('%')[0] + '%'  # важно что это не проценты а варчар
WW = (tr_blocks[i].getchildren()[12].text_content())
W1 = (tr_blocks[i].getchildren()[13].text_content())
W2 = (tr_blocks[i].getchildren()[14].text_content())
Tn = (tr_blocks[i].getchildren()[15].text_content()).split(' ')[0].rstrip()
Tx = (tr_blocks[i].getchildren()[16].text_content()).split(' ')[0].rstrip()
Cl = (tr_blocks[i].getchildren()[17].text_content())
Nh = (tr_blocks[i].getchildren()[18].text_content()).split('%')[0] + '%'
H = (tr_blocks[i].getchildren()[19].text_content()).split(' ')[0].rstrip()
Cm = (tr_blocks[i].getchildren()[20].text_content())
Ch = (tr_blocks[i].getchildren()[21].text_content())
VV = (tr_blocks[i].getchildren()[22].text_content()).split(' ')[0].rstrip()
Td = (tr_blocks[i].getchildren()[23].text_content()).split(' ')[0].rstrip()
RRR = (tr_blocks[i].getchildren()[24].text_content()).split(' ')[0].rstrip()
tR = (tr_blocks[i].getchildren()[25].text_content())
E = (tr_blocks[i].getchildren()[26].text_content())
Tg = (tr_blocks[i].getchildren()[27].text_content()).split(' ')[0].rstrip()
E1 = (tr_blocks[i].getchildren()[28].text_content())
sss = (tr_blocks[i].getchildren()[29].text_content()).split(' ')[0].rstrip()
print(W2)
i=1
while i<8:
    tmp=source_date.split('-')
    date = tmp[2] + '-'+ tmp[1] + '-' + tmp[0]+' '+tr_blocks[i].getchildren()[0].text_content() + ':00'
    T=(tr_blocks[i].getchildren()[1].text_content()).split(' ')[0].rstrip()
    P0=(tr_blocks[i].getchildren()[2].text_content()).split(' ')[0].rstrip()
    P=(tr_blocks[i].getchildren()[3].text_content()).split(' ')[0].rstrip()
    Pa=(tr_blocks[i].getchildren()[4].text_content()).split(' ')[0].rstrip()
    U=(tr_blocks[i].getchildren()[5].text_content()).split(' ')[0].rstrip()
    DD=(tr_blocks[i].getchildren()[6].text_content())
    Ff=(tr_blocks[i].getchildren()[7].text_content()).split(')')[0]+')'
    ff10=(tr_blocks[i].getchildren()[8].text_content()).split(' ')[0].rstrip()
    ff3=(tr_blocks[i].getchildren()[9].text_content()).split(' ')[0].rstrip()
    N=(tr_blocks[i].getchildren()[10].text_content()).split('%')[0]+'%' #важно что это не проценты а варчар
    WW=(tr_blocks[i].getchildren()[11].text_content())
    W1=(tr_blocks[i].getchildren()[12].text_content())
    W2=(tr_blocks[i].getchildren()[13].text_content())
    Tn=(tr_blocks[i].getchildren()[14].text_content()).split(' ')[0].rstrip()
    Tx=(tr_blocks[i].getchildren()[15].text_content()).split(' ')[0].rstrip()
    Cl=(tr_blocks[i].getchildren()[16].text_content())
    Nh=(tr_blocks[i].getchildren()[17].text_content()).split('%')[0]+'%'
    H=(tr_blocks[i].getchildren()[18].text_content()).split(' ')[0].rstrip()
    Cm=(tr_blocks[i].getchildren()[19].text_content())
    Ch=(tr_blocks[i].getchildren()[20].text_content())
    VV=(tr_blocks[i].getchildren()[21].text_content()).split(' ')[0].rstrip()
    Td=(tr_blocks[i].getchildren()[22].text_content()).split(' ')[0].rstrip()
    RRR=(tr_blocks[i].getchildren()[23].text_content()).split(' ')[0].rstrip()
    tR=(tr_blocks[i].getchildren()[24].text_content())
    E=(tr_blocks[i].getchildren()[25].text_content())
    Tg=(tr_blocks[i].getchildren()[26].text_content()).split(' ')[0].rstrip()
    E1=(tr_blocks[i].getchildren()[27].text_content())
    sss=(tr_blocks[i].getchildren()[28].text_content()).split(' ')[0].rstrip()
    i=i+1
#-----------------------------
# test = tr_blocks[0].getchildren()[2].text_content()
# print(test)
# t_0_p = result.getroot().find_class('t_0 dfs')
# t_0_p.pop()
# t_0_p.pop()
# t_0_p.pop()
# Td=t_0_p.pop().text_content()
# print(Td)
#pr = (html.tostring(result,pretty_print=True, method="html", encoding='utf8'))
#test  = (html.tostring(Td,pretty_print=True, method="html", encoding='utf8'))
#print(test)
#output_d.write(pr)

#output_d.close()