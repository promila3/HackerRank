#Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
select distinct(CITY)
from STATION
where lower(substr(CITY,1,1)) in ('a','e','i','o','u');
