# -*- coding: utf-8 -*-
import scrapy
import json
import uuid

METADATA_FILE = 'uk_universities.json'
GOLD_UNI_DATA = {
  "id": "",
  "source_type": "web",
  "source_name": "university.which.co",
  "source_domain": "https://university.which.co.uk",
  "region": "uk",
  "type": "univerity",
  "display_name": "",
  "name": "",
  "number_of_dpt": 0,
  "geo_location": {
    "lat": 0,
    "lon": 0
  },
  "address": "",
  "contact_no": ""
}
GOLD_CURS_DATA ={
  "id": "",
  "source_type": "web",
  "source_name": "university.which.co",
  "source_domain": "https://university.which.co.uk",
  "type": "cources",
  "region": "uk",
  "name": "",
  "display_name": "",
  "duration": {
    "y": 0,
    "m": 0,
    "d": 0
  },
  "fee": "0",
  "currency": "",
  "deparment": "",
  "dpt_code": "",
  "courses-code": "",
  "univeristy_id": "",
  "courses_url": "",
  "courses_type": "",
  "mode_of_study": ""
}


class Worker1UkSpider(scrapy.Spider):
    name = 'worker_1_uk'
    allowed_domains = ['https://university.which.co.uk']
    golden_course_data_arr = []

    def start_requests(self):

        for obj in self.unidata_loader():
            self.id = obj['id']
            self.url = self.allowed_domains[0] + str(obj['course_link']).strip()

            yield scrapy.Request(url=self.url,callback=self.parse)

    def parse(self, response):

        course_list = response.css("dl.result-card__heading--indented > h6 > a::text").extract()
        course_details = response.css("div.course-snippets > span::text").extract()

        for idx in range(len(course_list)):

            # Brack the course_details
            duration  = str(course_details[idx]).strip().split(' ')
            year = str(course_details[idx]).strip().split('years')[0].split(' ')[-2]
            print(duration)

            GOLD_CURS_DATA['id'] = str(uuid.uuid1())
            GOLD_CURS_DATA['name'] = str(course_list[idx]).replace(' ','_').lower()
            GOLD_CURS_DATA['display_name'] = str(course_list[idx])
            GOLD_CURS_DATA['mode_of_study'] = duration[-2]
            GOLD_CURS_DATA['duration']['y'] =float(year)
            GOLD_CURS_DATA['courses_type'] = duration[0]
            GOLD_CURS_DATA['courses_url'] = self.url
            GOLD_CURS_DATA['univeristy_id'] = self.id

            self.golden_course_data_arr.append(GOLD_CURS_DATA)

            with open('golden_rec/course.json','a+') as nwf:
                nwf.write('[')
                nwf.write(json.dumps(GOLD_CURS_DATA,indent=3))
                nwf.write(',')
                nwf.write('\n')

    def unidata_loader(self):
        golden_uni_data_arr = []
        with open(f'metadata/{METADATA_FILE}','r') as f:
            data = json.load(f)
        for univeristy in data:
            GOLD_UNI_DATA['id'] = univeristy['id']
            GOLD_UNI_DATA['display_name'] = univeristy['university']
            GOLD_UNI_DATA['name'] = str(univeristy['university']).replace(' ','_').lower()
            GOLD_UNI_DATA['number_of_dpt'] = univeristy['course_count']
            golden_uni_data_arr.append(GOLD_UNI_DATA)

        with open('golden_rec/universities.json','w') as uni:

            uni.write(json.dumps(golden_uni_data_arr))
            uni.close()


        return data



