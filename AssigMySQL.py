#1) Count the number of Salesperson whose name begin with ‘a’/’A’.
select
    Count(*)
from
    SalesPeople
where
    Sname like 'a%'
    or Sname like 'A%';

#2) Display all the Salesperson whose all orders worth is more than Rs. 2000.
select
sp.Sname,
o.Amt
from
    Orders as o
    inner join SalesPeople as sp on o.Snum = sp.Snum
where
    o.Amt > 2000;

#3) Count the number of Salesperson belonging to Newyork.
select
    count(*)
from
    SalesPeople
where
    City = 'Newyork';

#4) Display the number of Salespeople belonging to London and belonging to Paris.
select
    City,
    count(*)
from
    SalesPeople
where
    city = 'London'
    or city = 'Paris'
group by
    City;

#5) Display the number of orders taken by each Salesperson and their date of orders.
select
    sp.Sname,
    count(*),
    o.Odate
from
    SalesPeople as sp
    inner join Orders as o on sp.Snum = o.Snum
group by
    sp.Sname,
    o.Odate;