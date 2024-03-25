from types import NoneType
from openpyxl import load_workbook
import requests
from bs4 import BeautifulSoup as BS
from bs4 import BeautifulSoup
from IPython.display import Image, display
import pandas as pd
from tqdm import tqdm
import time
import json

#page = requests.get(url2)

#soup = BeautifulSoup(page.text, 'html.parser')
#news_items = soup.find_all(class_='ArtV2Default_wrapper__ENxvA ArtV2Default_wrapper__adaptive__2tegx ArtV2Default_v4__bVeTN')
url_link = 'https://kenwood.ru'
url = 'https://kenwood.ru/shop'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
news_items = soup.find_all(class_='shop-cart')
c = 0


for item in news_items:
    title = item.find(class_='shop-cart__title').text
    print('\n' +'Вкладка: ' + title.strip())

    if c == 0:
        c = 1
        for i in range(1, 4):                                                                   #Чекаем каждую станицу раздела kuhonnye-mashiny
            url_km = 'https://kenwood.ru/category/kuhonnye-mashiny/' + str(i)
            response_km = requests.get(url_km).text
            soup_km = BeautifulSoup(response_km, 'html.parser')
            km_items = soup_km.find_all(class_='product-card--shop')

            for item in km_items:                                                               #Бегаем по i странице
        
                if item.find(class_='card-item__display-title') != None:                        # "Если карточка товара была обнаружена", т.к там есть рекламные контейнеры с таким классом


                    img = item.find(class_='card-item__img')
                    image_tag = img.find('img')
                    image = image_tag['src']
                    display(Image(url=image))                                                   #не получается вывести картинку
            

                    title_km = item.find(class_='card-item__display-title').text                
                    full_title_km = item.find(class_='card-item__title').text
                    link = url_link + item.select_one('.card-item > a')['href']
                    print(link)
                    print('Наименование: ' + title_km.strip() + '\n' +
                  'Полное наименование: ' + full_title_km.strip())
                    
                    if item.find(class_='prev') != None:                                        #"Если есть 2 цены выводим по отдельности" 
                        full_cost_km = item.find(class_='prev').text
                        print('Полная стоимость: ' + full_cost_km.strip())
                        lower_price_km = item.find(class_='curr').text
                        print('Сниженная стоимость: ' + lower_price_km.strip())

                    else:                                                                       # Иначе выводим одну цену
                        cost_km = item.find(class_='curr').text
                        print('Полная стоимость: ' + cost_km.strip())

                    if item.find(class_='label label-orange') != None:                          # "Если есть дополнительная информация в карточке"
                        additional_km = item.find(class_='label label-orange').text
                        if additional_km == 'Хит продаж':
                            print(additional_km)
                        elif additional_km == 'New':
                            print('Новинка')
                        else:
                            pass
                        
                    if item.find(class_='label label-orange label-gift') != None: print('При покупке предусмотрен подарок')
                    else: pass

                    if item.find(class_='label label-purple') != None:                         #Предзаказ\скидка - указываются в одном классе
                        percent_km = item.find(class_='label label-purple').text
                        if percent_km == 'Предзаказ':
                            print('Только по предзаказу')
                        else: 
                            print('Cкидка ' + percent_km.strip())


                    if item.find(class_='not-available') != None:                              #"Указано ли отсутствие товара ?" Если нет, значит в наличии
                        not_available_km = item.find(class_='not-available').text
                        if not_available_km == 'Нет в наличии':
                            print('Нет в наличии' + '\n')
                    else:
                        print('В наличии' + '\n')
                else:
                    pass


            
    elif c == 1:                                                                              #Это для того чтобы в каждой станице выполнялся только соответствующий elif, можно было делать swich case, но это для умных
        c = 2
        url_kk = 'https://kenwood.ru/category/kuhonnye-kombainy'
        response_kk = requests.get(url_kk).text
        soup_kk = BeautifulSoup(response_kk, 'html.parser')
        kk_items = soup_kk.find_all(class_='product-card--shop')

        for item in kk_items:

            if item.find(class_='card-item__display-title') != None:
                    title_kk = item.find(class_='card-item__display-title').text
                    full_title_kk = item.find(class_='card-item__title').text
                    link = url_link + item.select_one('.card-item > a')['href']
                    print(link)
                    print('Наименование: ' + title_kk.strip() + '\n'
                          'Полное наименование: ' + full_title_kk.strip())


                    if item.find(class_='prev') != None:
                        full_cost_kk = item.find(class_='prev').text.strip()
                        print('Полная стоимость: ' + full_cost_kk.strip())
                        lower_price_kk = item.find(class_='curr').text.strip()
                        print('Сниженная стоимость: ' + lower_price_kk.strip())


                    else: 
                        cost_kk = item.find(class_='curr').text
                        print('Полная стоимость: ' + cost_kk.strip())

                    if item.find(class_='label label-orange') != None:                          # "Если есть дополнительная информация в карточке"
                        additional_kk = item.find(class_='label label-orange').text
                        if additional_kk == 'Хит продаж':
                            print(additional_kk)
                        elif additional_kk == 'New':
                            print('Новинка')
                        else:
                            pass
                    
                    if item.find(class_='label label-orange label-gift') != None: print('При покупке предусмотрен подарок')
                    else: pass

                    if item.find(class_='label label-purple') != None:
                        percent_kk = item.find(class_='label label-purple').text
                        if percent_kk == 'Предзаказ':
                            print('Только по предзаказу')
                        else: 
                            print('Cкидка ' + percent_kk.strip())
                
                    else:
                        pass
                    
                    if item.find(class_='not-available') != None:
                        not_available_kk = item.find(class_='not-available').text
                        if not_available_kk == 'Нет в наличии':
                            print(not_available_kk + '\n')
                    else:
                        print('В наличии' + '\n')
                    
                    
            else:
                pass
            


    elif c == 2:
        c = 3
        for i in range(1, 7):
            url_a = 'https://kenwood.ru/category/nasadki-i-aksessuary/' + str(i)
            response_a = requests.get(url_a).text
            soup_a = BeautifulSoup(response_a, 'html.parser')
            a_items = soup_a.find_all(class_='product-card--shop')

            for item in a_items:
               
                if item.find(class_='card-item__display-title') != None:
                    title_a = item.find(class_='card-item__display-title').text
                    full_title_a = item.find(class_='card-item__title').text
                    link = url_link + item.select_one('.card-item > a')['href']
                    print(link)
                    print('Наименование: ' + title_a.strip() + '\n'
                          'Полное наименование: ' + full_title_a.strip())

                    if item.find(class_='prev') != None:
                        full_cost_a = item.find(class_='prev').text
                        print('Полная стоимость: ' + full_cost_a.strip())
                        lower_price_a = item.find(class_='curr').text
                        print('Сниженная стоимость: ' + lower_price_a.strip())
                    else: 
                        cost_a = item.find(class_='curr').text
                        print('Полная стоимость: ' + cost_a.strip())

                    if item.find(class_='label label-orange') != None:                          # "Если есть дополнительная информация в карточке"
                        additional_a = item.find(class_='label label-orange').text
                        if additional_a == 'Хит продаж':
                            print(additional_a)
                        elif additional_a == 'New':
                            print('Новинка')
                        else:
                            pass
                    
                    if item.find(class_='label label-orange label-gift') != None: print('При покупке предусмотрен подарок')
                    else: pass

                    if item.find(class_='label label-purple') != None:
                        percent_a = item.find(class_='label label-purple').text
                        if percent_a == 'Предзаказ':
                            print('Только по предзаказу')
                        else: 
                            print('Cкидка ' + percent_a.strip())

                    if item.find(class_='not-available') != None:
                        not_available_km = item.find(class_='not-available').text
                        if not_available_km == 'Нет в наличии':
                            print('Нет в наличии' + '\n')
                    else:
                        print('В наличии' + '\n')
                    
                else:
                    pass
                


    elif c == 3:
        c = 4
        url_m = 'https://kenwood.ru/category/myasorubki'
        response_m = requests.get(url_m).text
        soup_m = BeautifulSoup(response_m, 'html.parser')
        m_items = soup_m.find_all(class_='product-card--shop')

        for item in m_items:
            title_m = item.find(class_='card-item__display-title').text
            full_title_m = item.find(class_='card-item__title').text
            link = url_link + item.select_one('.card-item > a')['href']
            print(link)
            print('Наименование: ' + title_m .strip() + '\n' +
                  'Полное наименование: ' + full_title_m.strip())
            
            if item.find(class_='prev') != None:
                full_cost_m = item.find(class_='prev').text
                print('Полная стоимость: ' + full_cost_m.strip())
                lower_price_m = item.find(class_='curr').text
                print('Сниженная стоимость: ' + lower_price_m.strip())
            else: 
                cost_m = item.find(class_='curr').text
                print('Полная стоимость: ' + cost_m.strip())
            
            if item.find(class_='label label-orange') != None:                          # "Если есть дополнительная информация в карточке"
                additional_m = item.find(class_='label label-orange').text
                if additional_m == 'Хит продаж':
                    print(additional_m)
                elif additional_m == 'New':
                    print('Новинка')
                else:
                    pass
            
            if item.find(class_='label label-orange label-gift') != None: print('При покупке предусмотрен подарок')
            else: pass

            if item.find(class_='label label-purple') != None:
                percent_m = item.find(class_='label label-purple').text
                if percent_m == 'Предзаказ':
                    print('Только по предзаказу')
                else: 
                    print('Cкидка ' + percent_m.strip())

            if item.find(class_='not-available') != None:
                not_available_m = item.find(class_='not-available').text
                if not_available_m == 'Нет в наличии':
                    print('Нет в наличии' + '\n')
                else:
                    print('В наличии' + '\n')


    elif c == 4:
        c = 5
        url_s = 'https://kenwood.ru/category/sokovyzhimalki'
        response_s = requests.get(url_s).text
        soup_s = BeautifulSoup(response_s, 'html.parser')
        s_items = soup_s.find_all(class_='product-card--shop')
        
        for item in s_items:
            title_s = item.find(class_='card-item__display-title').text
            full_title_s = item.find(class_='card-item__title').text
            link = url_link + item.select_one('.card-item > a')['href']
            print(link)
            print('Наименование: ' + title_s.strip() + '\n' +
                  'Полное наименование: ' + full_title_s.strip())
            
            if item.find(class_='prev') != None:
                full_cost_s = item.find(class_='prev').text
                print('Полная стоимость: ' + full_cost_s.strip())
                lower_price_s = item.find(class_='curr').text
                print('Сниженная стоимость: ' + lower_price_s.strip())
            else: 
                cost_s = item.find(class_='curr').text
                print('Полная стоимость: ' + cost_s.strip())

            if item.find(class_='label label-orange') != None:                          # "Если есть дополнительная информация в карточке"
                additional_s = item.find(class_='label label-orange').text
                if additional_s == 'Хит продаж':
                    print(additional_s)
                elif additional_s == 'New':
                    print('Новинка')
                else:
                    pass

            if item.find(class_='label label-orange label-gift') != None: print('При покупке предусмотрен подарок')
            else: pass

            if item.find(class_='label label-purple') != None:
                percent_s = item.find(class_='label label-purple').text
                if percent_s == 'Предзаказ':
                    print('Только по предзаказу')
                else: 
                    print('Cкидка ' + percent_s.strip())

            if item.find(class_='not-available') != None:
                not_available_s = item.find(class_='not-available').text
                if not_available_s == 'Нет в наличии':
                    print('Нет в наличии' + '\n')
            else:
                print('В наличии' + '\n')
            
    
    elif c == 5:
        c = 6
        url_sb = 'https://kenwood.ru/category/stacionarnye-blendery'
        response_sb = requests.get(url_sb).text
        soup_sb = BeautifulSoup(response_sb, 'html.parser')
        sb_items = soup_sb.find_all(class_='product-card--shop')

        for item in sb_items:
            title_sb = item.find(class_='card-item__display-title').text
            full_title_sb = item.find(class_='card-item__title').text
            link = url_link + item.select_one('.card-item > a')['href']
            print(link)
            print('Наименование: ' + title_sb.strip() + '\n' +
                  'Полное наименование: ' + full_title_sb.strip())
            
            if item.find(class_='prev') != None:
                full_cost_sb= item.find(class_='prev').text
                print('Полная стоимость: ' + full_cost_sb.strip())
                lower_price_sb = item.find(class_='curr').text
                print('Сниженная стоимость: ' + lower_price_sb.strip())
            else:
                cost_sb = item.find(class_='curr').text
                print('Полная стоимость: ' + cost_sb.strip())

            if item.find(class_='label label-orange') != None:                          # "Если есть дополнительная информация в карточке"
                additional_sb = item.find(class_='label label-orange').text
                if additional_sb == 'Хит продаж':
                    print(additional_sb)
                elif additional_sb == 'New':
                    print('Новинка')
                else:
                    pass

            if item.find(class_='label label-orange label-gift') != None: print('При покупке предусмотрен подарок')
            else: pass
            
            if item.find(class_='label label-purple') != None:
                percent_sb = item.find(class_='label label-purple').text
                if percent_sb == 'Предзаказ':
                    print('Только по предзаказу')
                else: 
                    print('Cкидка ' + percent_sb.strip())

            if item.find(class_='not-available') != None:
                not_available_sb = item.find(class_='not-available').text
                if not_available_sb == 'Нет в наличии':
                    print('Нет в наличии' + '\n')
            else:
                print('В наличии' + '\n')


    elif c == 6:
        c = 7
        url_rb = 'https://kenwood.ru/category/ruchnye-blendery'
        response_rb = requests.get(url_rb).text
        soup_rb = BeautifulSoup(response_rb, 'html.parser')
        rb_items = soup_rb.find_all(class_='product-card--shop')

        for item in rb_items:

            title_rb = item.find(class_='card-item__display-title').text
            full_title_rb = item.find(class_='card-item__title').text
            link = url_link + item.select_one('.card-item > a')['href']
            print(link)
            print('Наименование: ' + title_rb.strip() + '\n' +
                  'Полное наименование: ' + full_title_rb.strip())
            
            if item.find(class_='prev') != None:
                full_cost_rb= item.find(class_='prev').text
                print('Полная стоимость: ' + full_cost_rb.strip())
                lower_price_rb = item.find(class_='curr').text
                print('Сниженная стоимость: ' + lower_price_rb.strip())
            else: 
                cost_rb = item.find(class_='curr').text
                print('Полная стоимость: ' + cost_rb.strip())

            if item.find(class_='label label-orange') != None:                          # "Если есть дополнительная информация в карточке"
                additional_rb = item.find(class_='label label-orange').text
                if additional_rb == 'Хит продаж':
                    print(additional_rb)
                elif additional_rb == 'New':
                    print('Новинка')
                else:
                    pass
            
            if item.find(class_='label label-orange label-gift') != None: print('При покупке предусмотрен подарок')
            else: pass
            
            if item.find(class_='label label-purple') != None:
                percent_rb = item.find(class_='label label-purple').text
                if percent_rb == 'Предзаказ':
                    print('Только по предзаказу')
                else: 
                    print('Cкидка ' + percent_rb.strip())
    
            if item.find(class_='not-available') != None:
                not_available_rb = item.find(class_='not-available').text
                if not_available_rb == 'Нет в наличии':
                    print('Нет в наличии' + '\n')
            else:
                print('В наличии' + '\n')


        


    elif c == 7:
        c = 8
        url_ch = 'https://kenwood.ru/category/elektricheskie-chajniki'
        response_ch = requests.get(url_ch).text
        soup_ch = BeautifulSoup(response_ch, 'html.parser')
        ch_items = soup_ch.find_all(class_='product-card--shop')

        for item in ch_items:
            title_ch = item.find(class_='card-item__display-title').text
            full_title_ch = item.find(class_='card-item__title').text
            link = url_link + item.select_one('.card-item > a')['href']
            print(link)
            print('Наименование: ' + title_ch.strip() + '\n' +
                  'Полное наименование: ' + full_title_ch.strip())
            
            if item.find(class_='prev') != None:
                full_cost_ch= item.find(class_='prev').text
                print('Полная стоимость: ' + full_cost_ch.strip())
                lower_price_ch = item.find(class_='curr').text
                print('Сниженная стоимость: ' + lower_price_ch.strip())

            else: 
                cost_ch = item.find(class_='curr').text
                print('Полная стоимость: ' + cost_ch.strip())

            if item.find(class_='label label-orange') != None:                          # "Если есть дополнительная информация в карточке"
                additional_ch = item.find(class_='label label-orange').text
                if additional_ch == 'Хит продаж':
                    print(additional_s)
                elif additional_ch == 'New':
                    print('Новинка')
                else:
                    pass

            if item.find(class_='label label-orange label-gift') != None: print('При покупке предусмотрен подарок')
            else: pass
            
            if item.find(class_='label label-purple') != None:
                percent_ch = item.find(class_='label label-purple').text
                if percent_ch == 'Предзаказ':
                    print('Только по предзаказу')
                else: 
                    print('Cкидка ' + percent_ch.strip())
           
            if item.find(class_='not-available') != None:
                not_available_ch = item.find(class_='not-available').text
                if not_available_ch == 'Нет в наличии':
                    print('Нет в наличии' + '\n')
            else:
                print('В наличии' + '\n') 



    elif c == 8:
        c = 9
        url_mi = 'https://kenwood.ru/category/miksery'
        response_mi = requests.get(url_mi).text
        soup_mi = BeautifulSoup(response_mi, 'html.parser')
        mi_items = soup_mi.find_all(class_='product-card--shop')

        for item in mi_items:
            title_mi = item.find(class_='card-item__display-title').text
            full_title_mi = item.find(class_='card-item__title').text
            link = url_link + item.select_one('.card-item > a')['href']
            print(link)
            print('Наименование: ' + title_mi.strip() + '\n' +
                  'Полное наименование: ' + full_title_mi.strip())
            
            if item.find(class_='prev') != None:
                full_cost_mi = item.find(class_='prev').text
                print('Полная стоимость: ' + full_cost_mi.strip())
                lower_price_mi = item.find(class_='curr').text
                print('Сниженная стоимость: ' + lower_price_mi.strip())
            else: 
                cost_mi = item.find(class_='curr').text
                print('Полная стоимость: ' + cost_mi.strip())

            if item.find(class_='label label-orange') != None:                          # "Если есть дополнительная информация в карточке"
                additional_mi = item.find(class_='label label-orange').text
                if additional_mi == 'Хит продаж':
                    print(additional_mi)
                elif additional_mi == 'New':
                    print('Новинка')
                else:
                    pass

            if item.find(class_='label label-orange label-gift') != None: print('При покупке предусмотрен подарок')
            else: pass
            
            if item.find(class_='label label-purple') != None:
                percent_mi = item.find(class_='label label-purple').text
                if percent_mi == 'Предзаказ':
                    print('Только по предзаказу')
                else: 
                    print('Cкидка ' + percent_mi.strip())

            if item.find(class_='not-available') != None:
                not_available_mi = item.find(class_='not-available').text
                if not_available_mi == 'Нет в наличии':
                    print('Нет в наличии' + '\n')
            else:
                print('В наличии' + '\n')



    elif c == 9:
        c = 10
        url_hleb = 'https://kenwood.ru/category/hlebopech'
        response_hleb = requests.get(url_hleb).text
        soup_hleb = BeautifulSoup(response_hleb, 'html.parser')
        hleb_items = soup_hleb.find_all(class_='product-card--shop')

        for item in hleb_items:
            title_hleb = item.find(class_='card-item__display-title').text
            full_title_hleb = item.find(class_='card-item__title').text
            link = url_link + item.select_one('.card-item > a')['href']
            print(link)
            print('Наименование: ' + title_hleb.strip() + '\n' +
                  'Полное наименование: ' + full_title_hleb.strip())
            
            if item.find(class_='prev') != None:
                full_cost_hleb = item.find(class_='prev').text
                print('Полная стоимость: ' + full_cost_hleb.strip())
                lower_price_hleb = item.find(class_='curr').text
                print('Сниженная стоимость: ' + lower_price_hleb.strip())
            else: 
                cost_hleb = item.find(class_='curr').text
                print('Полная стоимость: ' + cost_hleb.strip())

            if item.find(class_='label label-orange') != None:                          # "Если есть дополнительная информация в карточке"
                additional_hleb = item.find(class_='label label-orange').text
                if additional_hleb == 'Хит продаж':
                    print(additional_hleb)
                elif additional_hleb == 'New':
                    print('Новинка')
                else:
                    pass

            if item.find(class_='label label-orange label-gift') != None: print('При покупке предусмотрен подарок')
            else: pass
            
            if item.find(class_='label label-purple') != None:
                percent_hleb = item.find(class_='label label-purple').text
                if percent_hleb == 'Предзаказ':
                    print('Только по предзаказу')
                else: 
                    print('Cкидка ' + percent_hleb.strip())

            if item.find(class_='not-available') != None:
                not_available_hleb = item.find(class_='not-available').text
                if not_available_hleb == 'Нет в наличии':
                    print('Нет в наличии' + '\n')
            else:
                print('В наличии' +'\n')




    elif c == 10:
        url_mix = ' https://kenwood.ru/category/kmix-kollekciya'
        response_mix = requests.get(url_mix).text
        soup_mix = BeautifulSoup(response_mix, 'html.parser')
        mix_items = soup_mix.find_all(class_='product-card--shop')

        for item in mix_items:
            title_mix = item.find(class_='card-item__display-title').text
            full_title_mix = item.find(class_='card-item__title').text
            link = url_link + item.select_one('.card-item > a')['href']
            print(link)
            print('Наименование: ' + title_mix.strip() + '\n' +
                  'Полное наименование: ' + full_title_mix.strip())
            
            if item.find(class_='prev') != None:
                full_cost_mix = item.find(class_='prev').text
                print('Полная стоимость: ' + full_cost_mix.strip())
                lower_price_mix = item.find(class_='curr').text
                print('Сниженная стоимость: ' + lower_price_mix.strip())
            else: 
                cost_mix = item.find(class_='curr').text
                print('Полная стоимость: ' + cost_mix.strip())

            if item.find(class_='label label-orange') != None:                          # "Если есть дополнительная информация в карточке"
                additional_mix = item.find(class_='label label-orange').text
                if additional_mix == 'Хит продаж':
                    print(additional_mix)
                elif additional_mix == 'New':
                    print('Новинка')
                else:
                    pass

            if item.find(class_='label label-orange label-gift') != None: print('При покупке предусмотрен подарок')
            else: pass

            if item.find(class_='label label-purple') != None:
                percent_mix = item.find(class_='label label-purple').text
                if percent_mix == 'Предзаказ':
                    print('Только по предзаказу')
                else: 
                    print('Cкидка ' + percent_mix.strip())
        
            if item.find(class_='not-available') != None:
                not_available_mix= item.find(class_='not-available').text
                if not_available_mix == 'Нет в наличии':
                    print('Нет в наличии' + '\n')
            else:
                print('В наличии' + '\n')