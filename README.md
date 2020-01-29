# University Data Pipeline (UDP 1.0 )

![pipeline]()

This is very basic concept , I try to do. When we go through the diagram data flow start from sourcee where is our data scrapying form. Whe we come to scrapying area we create some logical grouping for spiders. each source has two type of spiders. 

- master spider (one per sources)
- worker spider (multiple number of worker per sources)

#### Master Spider 
Master spider can create golden recodes which are Business and markeing team looking data. And also master spider should create metadata for workers.

#### Worker Spider 
There are multiple number of woker spiders in unders the single sourse. The are doing diffrent jobs using metadata.
There are multiple websites can be source for our scraping engine.each web site has desicated master spider for crawling web data.
This master spider create metadata file for all workers. 


## Golden Records 

### Universites 

```
{
"id":UUID_1
"region":"uk",
"type":"univerity",
"display_name":"Univeristy of ABC",
"name":"univerity_of_abc",
"number_of_dpt" :15,
"geo_location":{
"lat":7.8221380123,
"lon":65.238012921
},
"address":"",
"contact_no":"
"
"
}
```

### Courcses

```{
"id":UUID_2,
"type":"cources",
"region":"uk",
"name":"coputer_science",
"display_name":"Computer Science",
"duration":{  
"y":1,
"m":6,
"d":0
},
"fee":"",
"currency":"eur",
"deparment":"computing",
"dpt_code":"",
"cources_code":"cs12391",
"univeristy_id": "UUID_1",
"courcse_url":"http://exsample.com/cources/cs12391",
"cources_type":"Bsc",
"mode_of_study":"full_time"
}```







