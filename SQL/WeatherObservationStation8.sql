#Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.
select CITY 
from STATION 
where lower(substr(CITY,1,1) in ('a','e','i','o','u')) and lower(substr(CITY,length(CITY),1) in ('a','e','i','o','u'));
