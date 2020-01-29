# -*- coding: utf-8 -*-
import scrapy
import os
import json
import uuid

METADATA_FILE = 'uk_universities.json'



class Master1UkSpider(scrapy.Spider):
    name = 'master_1_uk'
    allowed_domains = ['https://university.which.co.uk']
    # start_urls = ['http://https://university.which.co.uk/']

    def delFile(self):
        if os.path.exists('metadata/' + METADATA_FILE):
            os.remove('metadata/' + METADATA_FILE)

    def start_requests(self):

        self.delFile()
        urls =['https://university.which.co.uk/search/institution']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        university = response.css("div.institution-result--header > h3 > a::text").extract()
        course_count = response.css("div.institution-result--header--right > a::text").extract()
        crs_link = response.css("div.institution-result--header--right > a::attr(href)").extract()

        idx = 0
        uni_data = []
        with open(f'metadata/{METADATA_FILE}', 'a+') as f:
            for i in range(len(university)):
                idx += 1
                uni_obj = {}
                uni_obj['id'] = str(uuid.uuid1())
                uni_obj['type'] = 'metadata'
                uni_obj['university'] = str(university[i]).strip()
                uni_obj['course_count'] = int(str(course_count[i]).split('View all courses (')[1].split(')')[0])
                uni_obj['course_link'] = crs_link[i].strip()
                uni_data.append(uni_obj)
            f.write(json.dumps(uni_data))
        f.close()

