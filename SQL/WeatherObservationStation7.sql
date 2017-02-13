#Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
select distinct(CITY)
from STATION
where lower(substr(CITY,length(CITY),1)) in ('a','e','i','o','u');
