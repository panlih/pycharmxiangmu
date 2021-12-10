import requests
from lxml import etree
from time import  sleep
import json
def get_response(url):
    headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Mobile Safari/537.36'}
    response=requests.get(url,headers=headers).text
    return response

def handel_html(response):
    html=etree.HTML(response)
    return html

def save_to_file(filename,data):
    data = json.dumps(data)
    with open(filename,'w') as f:
        f.write(data)

def handel_page_data(response):
    #保存该页所有图书信息
    page_books=[]
    #每个图书的信息分别保存在class="indent"的div下的table标签内
    book_table= handel_html(response).xpath('//div[@class="indent"]//table')
    for book_td in book_table:
        #保存单个图书信息
        book={}
        #图书名保存在class="p12"的div下的第一个a标签内的title属性内
        book['name']=book_td.xpath('.//div[@class="pl2"]//a[1]/@title')[0]
        other_info = book_td.xpath('.//p[@class="pl"]/text()')[0]
        other_info=other_info.split('/')
        book['data']=other_info[-2]
        book['price']=other_info[-1]
        book['press']=other_info[-3]
        book['author']=other_info[:-3]
        book['author']=' '.join(book['author'])
        page_books.append(book)
    return page_books

def get_next_url(response):
    #下一页地址保存在text()='后页>'中的a标签的href属性
    html=handel_html(response)
    next_url=html.xpath('//a[text()="后页>"]/@href')
    #如果下一页连接存在
    if len(next_url)>0:
        return next_url[0]
    else:

        return None

def run():
    # 用于保存所有图书信息
    books_info = []
    index_url="https://book.douban.com/top250?start=0"
    #1、获取首页resopnce响应
    response=get_response(index_url)
    # 2、解析网页内容，获取所需信息(使用xpath解析)
    page_books = handel_page_data(response)
    #print(page_books)
    #放入所有图书信息中
    books_info.extend(page_books)
    #3.获取下一页url
    next_url = get_next_url(response)
    #print(next_url)
    #当下一页存在
    while next_url is not None:
        #设置延时 防止封ip
        sleep(4)
        # 1、获取首页resopnce响应
        response = get_response(next_url)
        # 2、解析网页内容，获取所需信息(使用xpath解析)
        page_books = handel_page_data(response)
        #print(page_books)
        # 放入所有图书信息中
        books_info.extend(page_books)
        # 3.获取下一页url
        next_url = get_next_url(response)
    save_to_file(filename='data.json',data=books_info)


if __name__ == '__main__':
    run()
