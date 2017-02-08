https://www.hackerrank.com/challenges/african-cities
select c.name 
from city c, country d
where c.countrycode = d.code
and d.continent = 'Africa';
