#!/usr/bin/env python
# -*- coding: utf-8 -*-
import  urllib, urllib2, cookielib

class atape_http_client:
    # Передаем в конструктор класса параметры прокси и user agent для возможности манипуляций ими
    def __init__(self, proxy=None, user_agent='Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3'):      
        # Прописываем хэндлеры для http/s, redirect and cookie
        self.cookie_handler   = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
        self.redirect_handler = urllib2.HTTPRedirectHandler()
        self.http_handler     = urllib2.HTTPHandler()
        self.https_handler    = urllib2.HTTPSHandler()
   
        # Загружаем хэндлеры в opener
        self.opener = urllib2.build_opener(self.http_handler, 
                                           self.https_handler, 
                                           self.cookie_handler, 
                                           self.redirect_handler)
                
        # Проверям будем ли мы использовать прокси
        if proxy: 
            self.proxy_handler = urllib2.ProxyHandler(proxy)
            self.opener.add_handler(self.proxy_handler)
            
        # Устанавливаем заголовок User-agent    
        self.opener.addheaders = [('User-agent', user_agent)]    
        urllib2.install_opener(self.opener)
    
    # Функция, которая выполняет отправку GET/POST запросов и возвращает html код ответа
    def request(self, url, params={}, timeout=5):
        # Если переданы параметры, значит это POST запрос
        if params:
            params = urllib.urlencode(params)
            html = urllib2.urlopen(url, params, timeout)
        # Если параметров нет, значит отправляем GET запрос
        else:
            html = urllib2.urlopen(url)
            
        # Возвращаем HTML код ответа сервера
        return html.read()
        
###########################################################################

"""
# Создаем экземпляр класса
bot = atape_http_client()
# Отправка GET запроса на http://google.com
r=bot.request("http://google.com")
print r

# Установим POST-параметры login и pass
params = {'login' : 'my_login',
           'pass' : 'my_password'}
# Отправка POST запроса на http://example.com/login.php
r = bot.request("http://example.com/login.php", params)
print r

"""




