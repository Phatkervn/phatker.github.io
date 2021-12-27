import requests
from bs4 import BeautifulSoup
from datetime import datetime
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import ParseMode

title_tin_the_gioi = []
link_tin_the_gioi = []
title_trong_nuoc = []
link_trong_nuoc =[]
title_hang_hoa = []
link_hang_hoa = []
title_batdongsan = []
link_batdongsan = []
title_chungkhoang = []
link_chungkhoang = []
add_title = []

def get_news_thegioi():
    global add_title
    url_ndh = requests.get("https://ndh.vn/quoc-te/")
    soup_ndh = BeautifulSoup(url_ndh.text, 'html.parser')
    mydivs_ndh = soup_ndh.find_all("h1", {"class": "title-news"})
    for new in mydivs_ndh:
        if new.a.get('title') not in add_title:     
        	link_tin_the_gioi.append( 'https://ndh.vn' + new.a.get("href"))
        	title_tin_the_gioi.append( new.a.get("title"))
        	add_title.append(new.a.get('title'))




def get_news_thegioi_1():
    global add_title
    url_cafe = requests.get("https://cafef.vn/")
    soup_cafe = BeautifulSoup(url_cafe.text, 'html.parser')
    mydivs_cafe = soup_cafe.find_all("h2", {"class": ""})
    for new in mydivs_cafe[0:3]:
        if new.a.get('title') not in add_title:
            link_tin_the_gioi.append( 'https://cafef.vn' +new.a.get('href'))
            title_tin_the_gioi.append(new.a.get("title"))
            add_title.append(new.a.get('title'))



def get_news_thegioi_2():
    global add_title
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.46 Safari/537.36'}
    response = requests.get("https://vietstock.vn/the-gioi.htm", headers = header)
    soup = BeautifulSoup(response.content, "html.parser")
    abstract = soup.find_all("h2", class_="channel-title")
    for i in abstract[0:2]:
        if i.a.text not in add_title:
        	link_tin_the_gioi.append('https://vietstock.vn' + i.a.get("href"))
        	title_tin_the_gioi.append(i.a.text)
        	add_title.append( i.a.text)



def get_news_trongnuoc():
    global add_title
    url_ndh = requests.get("https://cafef.vn/thoi-su.chn")
    soup_ndh = BeautifulSoup(url_ndh.text, 'html.parser')
    mydivs_ndh = soup_ndh.find_all("h3", {"class": ""})
    for new in mydivs_ndh[0:3]:
        if new.a.get('title') not in add_title:
        	link_trong_nuoc.append('https://cafef.vn' + new.a.get("href"))
        	title_trong_nuoc.append(new.a.get("title"))
        	add_title.append(new.a.get('title'))



def get_news_chungkhoang3():
    global add_title
    url_ndh = requests.get("https://cafef.vn/thi-truong-chung-khoan.chn")
    soup_ndh = BeautifulSoup(url_ndh.text, 'html.parser')
    mydivs_ndh = soup_ndh.find_all("h3", {"class": ""})
    for new in mydivs_ndh[0:2]:
        if new.a.get('title') not in add_title:
        	link_chungkhoang.append('https://cafef.vn' + new.a.get("href"))
        	title_chungkhoang.append(new.a.get("title"))
        	add_title.append(new.a.get('title'))



def get_news_chungkhoang1():
    global add_title
    url_ndh = requests.get("https://ndh.vn/chung-khoan/co-phieu")
    soup_ndh = BeautifulSoup(url_ndh.text, 'html.parser')
    mydivs_ndh = soup_ndh.find_all("h3", {"class": "title-news"})
    for new in mydivs_ndh[0:2]:
        if new.a.get('title') not in add_title:
        	link_chungkhoang.append('https://ndh.vn' + new.a.get("href"))
        	title_chungkhoang.append(new.a.get("title"))
        	add_title.append(new.a.get('title'))



def get_news_chungkhoang2():
    global add_title
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'}
    response = requests.get("https://vietstock.vn/chung-khoan/giao-dich-noi-bo.htm", headers = header)
    soup = BeautifulSoup(response.content, "html.parser")
    abstract = soup.find_all("h2", class_='channel-title')
    for i in abstract[0:5]:
        if i.a.text not in add_title:
        	link_chungkhoang.append('https://vietstock.vn' + i.a.get("href"))
        	title_chungkhoang.append(i.a.text)
        	add_title.append(i.a.text)



def get_news_hanghoa():
    global add_title
    url_ndh = requests.get("https://ndh.vn/hang-hoa/")
    soup_ndh = BeautifulSoup(url_ndh.text, 'html.parser')
    mydivs_ndh = soup_ndh.find_all("h3", {"class": "title-news"})
    for new in mydivs_ndh[0:3]:
        if new.a.get('title') not in add_title:
        	link_hang_hoa.append('https://ndh.vn' + new.a.get("href"))
        	title_hang_hoa.append(new.a.get("title"))
        	add_title.append(new.a.get('title'))



def get_news_batdongsan():
    global add_title
    url_ndh = requests.get("https://ndh.vn/bat-dong-san/")
    soup_ndh = BeautifulSoup(url_ndh.text, 'html.parser')
    mydivs_ndh = soup_ndh.find_all("h3", {"class": "title-news"})
    for new in mydivs_ndh[0:3]:
        if new.a.get('title') not in add_title:
        	link_batdongsan.append('https://ndh.vn' + new.a.get("href"))
        	title_batdongsan.append(new.a.get("title"))
        	add_title.append(new.a.get('title'))



def get_news_chungkhoan():
    global add_title
    url_ndh = requests.get("https://ndh.vn/chung-khoan/")
    soup_ndh = BeautifulSoup(url_ndh.text, 'html.parser')
    mydivs_ndh = soup_ndh.find_all("h3", {"class": "title-news"})
    for new in mydivs_ndh[0:3]:
        if new.a.get('title') not in add_title:
        	link_chungkhoang.append('https://ndh.vn' + new.a.get("href"))
        	title_chungkhoang.append(new.a.get("title"))
        	add_title.append(new.a.get('title'))        	



def news(update: Update, context: CallbackContext) -> None:
	admin = "<a href='@Nguyenxu1984'>@Nguyenxu1984</a>"
	text =''
	text_tg = "🌏"
	text_tg_like = "👉"

	text_hh = "🏨"
	text_bds = "🏛"
	text_ck = "💵"
	tim = '❤️'
	cham = '.'*57
    
	d1 = datetime.now().strftime('%H:%M:%S ngày %d-%m-%Y')
	strthegioi = ''
	strhanghoa = ''
	strbatdongsan = ''
	strchungkhoan = ''
	strtrongnuoc = ''
	
	for i in range(0,len(title_tin_the_gioi)):
		if title_tin_the_gioi[i] != '':
			strthegioi += text_tg_like +"  " + title_tin_the_gioi[i]+ ". " +  "<a href='" + link_tin_the_gioi[i]+"'>Xem thêm...</a>" + "\n\n"
	for i in range(0,len(title_trong_nuoc)):
		if title_trong_nuoc[i] != '':
			strtrongnuoc += text_tg_like +"  " + title_trong_nuoc[i]+ ". " +  "<a href='" + link_trong_nuoc[i] +"'>Xem thêm...</a>" + "\n\n"
	for i in range(0,len(title_hang_hoa)):
		if title_hang_hoa[i] != '':
			strhanghoa += text_tg_like +"  " + title_hang_hoa[i] + ". " +  "<a href='" + link_hang_hoa[i]+"'>Xem thêm...</a>" + "\n\n"
	for i in range(0,len(title_batdongsan)):
		if title_batdongsan != '':
			strbatdongsan += text_tg_like +"  " + title_batdongsan[i] + ". " +  "<a href='" + link_batdongsan[i]+"'>Xem thêm...</a>" + "\n\n"
	for i in range(0,len(title_chungkhoang)):
		if title_chungkhoang[i] != '':
			strchungkhoan += text_tg_like +"  " + title_chungkhoang[i] + ". " +  "<a href='" + link_chungkhoang[i]+"'>Xem thêm...</a>" + "\n\n"
	ttg = "<b><i>Tin thế giới</i></b>"
	tintrongnuoc = "<b><i>Tin trong nước</i></b>"
	hh = "<b><i>Hàng hóa</i></b>"
	ck = "<b><i>Chứng khoán</i></b>"
	bds = "<b><i>Bất động sản</i></b>"

	update.message.reply_text(f'<b>Bản tin cập nhập lúc: {d1}</b>\n {text}\n{text_tg}  {ttg}\n{strthegioi}\n{text_tg}  {tintrongnuoc}\n{strtrongnuoc}\n{text_hh}  {hh}\n{strhanghoa}\n{text_bds}  {bds}\n{strbatdongsan}\n{text_ck}  {ck}\n{strchungkhoan}\n\n<b style="font-size: 4px;">Liên Hệ Mở Tài Khoản Chứng Khoán SSI, VPS: Ad</b> {admin}\n{cham}\n{tim}#ITP #chungkhoan #ichimoku',parse_mode=ParseMode.HTML)

get_news_thegioi()
get_news_thegioi_1()
get_news_thegioi_2()
get_news_trongnuoc()


get_news_hanghoa()
get_news_batdongsan()
get_news_chungkhoan()
#get_news_chungkhoang1()
get_news_chungkhoang2()
get_news_chungkhoang3()


updater = Updater('5002113106:AAE4pREE_5-W8XgEy1calCUk4RZnOBu0NHc')


# Lệnh
updater.dispatcher.add_handler(CommandHandler('news', news))

updater.start_polling()
updater.idle()
