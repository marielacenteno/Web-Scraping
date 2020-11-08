import requests
from bs4 import BeautifulSoup

keyword = 'chanel+earrings'
results = []

headers = {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:81.0) Gecko/20100101 Firefox/81.0'
}

#r = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + keyword, headers=headers)
for i in range(1,11):
    r = requests.get('https://www.ebay.com/sch/i.html?_&_nkw=' +keyword+ '&_pgn=' + str(i), headers=headers)

    #200 is the correct status code that you want to get
    print('r.status_code=',r.status_code)


    soup = BeautifulSoup(r.text, 'html.parser')

    #Check that selectors work

    '''
    #status
    stats = soup.select('.clearfix.srp-list.srp-results > li.s-item > .clearfix.s-item__wrapper > .clearfix.s-item__info > .s-item__subtitle > .SECONDARY_INFO')
    for stat in stats:
        print('stat=',stat.text)

    #title
    items = soup.select('.clearfix.srp-list.srp-results > li.s-item > .clearfix.s-item__wrapper > .clearfix.s-item__info > .s-item__link > .s-item__title')
    for item in items:
        print('item=',item.text)

    #price
    prices = soup.select('.s-item__price')
    for price in prices:
        print('price=',price.text)

    '''
    #create list of dictionaries by filling results list


    boxes = soup.select('.clearfix.srp-list.srp-results > li.s-item > .clearfix.s-item__wrapper')
    for box in boxes:
        #print('- - - - -')
        result = {}
        titles = box.select('.clearfix.srp-list.srp-results > li.s-item > .clearfix.s-item__wrapper > .clearfix.s-item__info > .s-item__link > .s-item__title')
        for title in titles:
            #print('title=',title.text)
            result['title'] = title.text
        prices = box.select('.s-item__price')
        for price in prices:
            #print('price=',price.text)
            result['price'] = price.text
        stats = box.select('.clearfix.srp-list.srp-results > li.s-item > .clearfix.s-item__wrapper > .clearfix.s-item__info > .s-item__subtitle > .SECONDARY_INFO')
        for stat in stats:
            #print('stat=',stat.text)
            result['status'] = stat.text
        print('result=', result)
        results.append(result)


    print('len(results)=', len(results))


import json
j = json.dumps(results)
with open ('items2.json', 'w') as f:
    f.write(j)
    

