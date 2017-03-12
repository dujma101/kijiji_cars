

import scrapy
import sqlite3


class QuotesSpider(scrapy.Spider):
    name = "kijiji"
    start_urls = [
        'http://www.kijiji.ca/v-cars-trucks/regina/yorkton-2001-volkswagen-passat-sedan/1245980754?enableSearchNavigationFlag=true',
    ]

    # conn = sqlite3.connect("scrapydata.db")
    # cur = conn.cursor()
    # cur.execute("select title from artical;")
    # resultsi = cur.fetchall()
    # cur.close()
    # conn.close()

    def parse(self, response):

        table_h = response.xpath('//table[@class="ad-attributes"]//tr//th//text()').extract()
        table_d = response.xpath('//table[@class="ad-attributes"]//tr//td//text()').extract()

        table_headers = []
        car_attrs = []

        for sve in table_h:
            table_headers.append(sve.strip())

        headers = [x for x in table_headers if x]
        del headers[2:6]
        # print(headers)

        for sve in table_d:
            car_attrs.append(sve.strip())
        attrs = [x for x in car_attrs if x]
        # print(attrs)

        del attrs[2:6]
        del attrs[3]
        # print(attrs)
        description = response.xpath('//*[@id="UserContent"]/table/tbody/tr/td/span/text()').extract()
        headers.append('Description')
        headers.append('Url')
        attrs.append((''.join(description).strip()))
        attrs.append('neki url')


        #dealing with empty values


        possible_header = set(['Date Listed', 'Make' ,'Model', 'Year', 'Kilometers', 'Price', 'Address','Transmission', 'Body Type' ,'Colour' ,'No. of Doors', 'Drivetrain', 'Fuel Type' , 'Description' , 'Url', 'For Sale By','Trim'])
        actual_header = set(headers)
        to_add = list(possible_header-actual_header)

        all_headers = headers + to_add

        for sve in range(len(to_add)):
            attrs.append('')



        zipano = zip(all_headers,attrs)
        print(zipano)


        #         yield {
        #      'description' : description,
        #
        # }

        return dict(zipano)


        # for quote in pth:
        #     print('qqqqqqqqqqqqqqqqqqqqqqqqqqqqqq', quote.extract())
        #     if quote.extract() == QuotesSpider.resultsi[-1][0]:
        #         print('22222222222222222222222222222222222222222222')
        #         yield {
        #     'text': quote.extract(),}
        #         return
        #
        #
        #
        # print('1111111111111111111111111111',QuotesSpider.resultsi[4])
        #
        # next_page = response.xpath('//a[@title="Next"]/@href').extract_first()
        # print(next_page)
        # nm = 0
        # while nm<3:
        #     if next_page is not None:
        #         nm +=1
        #         next_page = response.urljoin(next_page)
        #         #np = 'http://www.kijiji.ca/' + next_page
        #         yield scrapy.Request(next_page, callback=self.parse)