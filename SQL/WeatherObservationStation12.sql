#Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
select distinct city
  from station
where 
  substr(lower(city), 1, 1) not in ('a', 'e', 'i', 'o', 'u')
     and
  substr(lower(city), length(city), 1) not in ('a', 'e', 'i', 'o', 'u')
  order by city;
