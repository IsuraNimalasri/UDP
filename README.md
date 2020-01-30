# University Data Pipeline (UDP 1.0 )

![pipeline](/Pipeline.jpg)

This diagram represents the high-level architecture of University Data Pipelines. The selected sample consists of UK University information.

Starting from the Left-hand side; the diagram describes data sources or websites, which store information of universities.

The second step is scraping of data by “Scrapy Engine”. 

There are two types of spiders (“spider” is a scrapy term used to describe a web scraping module) which associate with the source; “Master Spider” and “Worker Spider”. 

##### Master Spider: Create metadata for worker spiders

##### Worker Spider: Create golden records 

#### Golden Records
This refers to the output of the pipeline, which helps to achieve business and marketing goals. There are two types of golden records introducing in this sample.
- University: describe the university for business and marketing purpose
- Courses: describe the course details for business and marketing purpose

Main reasons for introducing MongoDB as a Golden Record store are; 
	The Golden Records are semi-structured document type data.
Each record type can be evolved based on the business goal (i.e. keys can be added to the json)
These Golden Records have to be enriched, developed and transformed based on the business requirement and to achieve this, MongoDB has a sophisticated query strength.
 
<hr>

## Golden Records 

### Universites 

```
{
  "id": "UUID_1",
  "source_type": "web",
  "source_name": "example",
  "source_domain": "http://example.com/",
  "region": "uk",
  "type": "univerity",
  "display_name": "Univeristy of ABC",
  "name": "univerity_of_abc",
  "number_of_dpt": 15,
  "geo_location": {
    "lat": 7.8221380123,
    "lon": 65.238012921
  },
  "address": "",
  "contact_no": ""
}

```

### Courses

```
{
  "id": "UUID_2",
  "source_type": "web",
  "source_name": "example",
  "source_domain": "http://exsample.com/",
  "type": "cources",
  "region": "uk",
  "name": "coputer_science",
  "display_name": "Computer Science",
  "duration": {
    "y": 1,
    "m": 6,
    "d": 0
  },
  "fee": "35000",
  "currency": "eur",
  "deparment": "computing",
  "dpt_code": "",
  "courses-code": "cs12391",
  "univeristy_id": "UUID_1",
  "courses_url": "http://exsample.com/cources/cs12391",
  "courses_type": "Bsc",
  "mode_of_study": "full_time"
}

```

#### How to excute 

- Before excete UDP you should install  `pip install scrapy`

- Step 1 Excute master spider  
	`scrapy crawl master_1_uk`
	
- step 2 Excute worker spider
	`scrapy crawl worker_1_uk`





