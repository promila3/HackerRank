# Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

select city,length(city) 
FROM STATION 
order by length(city) asc,city asc 
LIMIT 1;
select city,length(city)
from STATION
order by length(city) desc, city asc
LIMIT 1;
