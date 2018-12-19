# -*- encoding:utf-8 -*-
from pyquery import PyQuery as pq
import os
import random
import requests
import urllib.request
import sys
type=sys.getfilesystemencoding()


class Crawler(object):

    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"}
    def request(self,url):

        rt = requests.get(url,headers =self.headers)
        return rt
    def gethtml(self,url):
        try:
            quest = self.request(url)
            html=quest.text
            return html
        except Exception as ex:
            print (u'打开页面超时')
     
     
    def getUrL(self,html):
        pgurl,num=self.getPageNum(html)
        for j in range(1,int(num)+1):
            try:
                imageurl=pgurl+str(j)
               # print imageurl.decode('utf-8').encode(type)
                print(imageurl)
                requ = self.request(imageurl)
                #pag= requests.urlopen(request).read()
                pag=requ.text
                urlslist=pq(pag)
                urls=urlslist('.postlist #pins>li>a').items()
                for url in urls:
                    imgurl=url('a').attr('href')
                    #print ur 
                    #title=url.find('.lazy').attr('alt')
                    title=url('img').attr('alt')
                    pathname = title.replace("?", '_')
                    fliename=pathname.strip()
                    #print fliename.decode('utf-8').encode(type)
                    print (fliename)
                    self.mkFile(fliename)

                    req = self.request(imgurl)
                    self.headers['referer'] = imgurl
                    #pagehtml= requests.urlopen(req).read()
                    pagehtml = req.text
                    max_span= pq(pagehtml)
                    spans= max_span('.pagenavi').items()
                    for spantext in spans:
                        panum=spantext.find('span').eq(-2).html()
                        for i in range(1,int(panum)+1):
                            pageurl=imgurl+'/'+str(i)
                            images=pq(pageurl)
                            image= images('img').attr('src')
                            print(image)
                            self.save(image)
                            i+=1
            except Exception as e:
                print(u'文件下载失败')
                print(str(e))
            finally:
                j=j+1

    def save(self, img_url):  ##这个函数保存图片
        name = img_url[-9:-4]
        img = self.request(img_url)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    def getTitleAndUrl(self,imageurl):
        pag= requests.get(imageurl).text
        urlslist=pq(pag)
        urls=urlslist('.postlist #pins>li>a').items()
        for url in urls:
            imgurl=url('a').attr('href')
                    #print ur 
                    #title=url.find('.lazy').attr('alt')
            title=url('img').attr('alt')
            pathname = title.replace("?", '_')
            fliename=pathname.strip()
            print(fliename)
            return imgurl,fliename
    
    
    def getPageNum(self,html):
        urlspage=pq(html)
        urlpages=urlspage('.nav-links').items()
        for pagenum in urlpages:
            pageurl=pagenum('a').attr('href')
            url=pageurl[0:-1]
            print (url)
            num=pagenum.find('.page-numbers').eq(-2).text()
            return url,num
     
    def mkFile(self,fliename):
        path = fliename.strip()
        isExists = os.path.exists(os.path.join("D:\images", path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("D:\images", path))
            os.chdir(os.path.join("D:\images", path))
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False
    def getPages(self,url):
            pagehtml= requests.get(url).text
            max_span= pq(pagehtml)
            spans= max_span('.pagenavi').items()
            for spantext in spans:
                panum=spantext.find('span').eq(-2).html()
                return panum  

if  __name__=='__main__':        
    cw=Crawler()
    html=cw.gethtml('http://www.mzitu.com/')               
    cw.getUrL(html)