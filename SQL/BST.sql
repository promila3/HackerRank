select N,
IF ( P IS NULL, 'Root',if((select count(*) from BST where P=B.N)>0, 'Inner','Leaf'))
FROM BST as B
order by N;
