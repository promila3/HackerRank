select c.company_code, c.founder, lm.cnt_lm, sm.cnt_sm, m.cnt_m,e.cnt_e
from Company c,
(select company_code ,count(distinct lead_manager_code) cnt_lm
 from lead_manager
 group by company_code) as lm,
(select company_code ,count(distinct senior_manager_code) cnt_sm
 from senior_manager
 group by company_code) as sm,
(select company_code ,count(distinct manager_code) cnt_m
 from manager
 group by company_code) as m,
(select company_code ,count(distinct employee_code) cnt_e
 from employee
 group by company_code) as e
where c.company_code = lm.company_code
and  c.company_code = sm.company_code
and  c.company_code = m.company_code
and  c.company_code = e.company_code;
