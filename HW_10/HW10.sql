SET SQL_SAFE_UPDATES = 0;

use sakila;

SELECT 
    first_name, last_name
FROM
    actor;

alter table actor
add Actor_Name varchar(255);

UPDATE actor 
SET 
    Actor_Name = CONCAT(UPPER(first_name), ' ', UPPER(last_name));
 
SELECT 
    *
FROM
    actor
WHERE
    first_name LIKE 'Joe';

SELECT 
    *
FROM
    actor
WHERE
    last_name LIKE '%gen%';

SELECT 
    *
FROM
    actor
WHERE
    last_name LIKE '%li%'
ORDER BY last_name , first_name ASC;

SELECT 
    *
FROM
    country
WHERE
    country IN ('Afghanistan' , 'China', 'Bangladesh');

alter table actor
add middle_name varchar(50);

ALTER TABLE actor CHANGE COLUMN middle_name  middle_name VARCHAR(50) AFTER first_name;

ALTER TABLE actor MODIFY middle_name blob;

alter table actor
drop middle_name;

select* from actor;

select  last_name, count(last_name)
from actor
group by last_name;

select  last_name, count(last_name) as cnt
from actor
group by last_name
having cnt >1
order by cnt asc;

UPDATE actor
SET first_name = 'HARPO' AND Actor_Name = 'HARPO WILLIAMS'
where Actor_Name = 'GROUCHO WILLIAMS';

select * from actor
where first_name = 'HARPO';

-- 4d? 
-- 5a

select s.first_name, s.last_name, a.address
from staff s 
join address a using(address_id);



select s.first_name, s.last_name, sum(p.amount ), p.staff_id
from staff s
join payment p using(staff_id)
where payment_date between '2005-08-01 00:00:00.00' and '2005-08-31 00:00:00.00'
group by staff_id;

select f.title, count(fa.film_id) as number_of_actors
from film f
join film_actor fa using(film_id)
group by film_id;

select count(f.film_id) as copies_of_hunchback
from film f
join inventory using(film_id)
where f.title='Hunchback Impossible'; 

select  c.first_name, c.last_name, sum(p.amount ) as total_paid
from customer c
join payment p using(customer_id)
group by customer_id
order by c.last_name asc;

select  f.title, l.name
from film f
join language l using(language_id)
where title like 'K%'  or title like 'Q%' and l.name = 'English';

select a.Actor_Name as Alone_Trip_Cast
from film f
join film_actor using(film_id)
join actor a using(actor_id)
where title = 'Alone Trip';

select c.first_name, c.last_name, c.email
from customer c
join address using(address_id)
join city using(city_id)
join country using(country_id)
where country.country = 'Canada';

select film.title, film.description
from film
join film_category using(film_id)
join category using(category_id)
where category.name = 'Family';

select f.title, count(r.inventory_id) as times_rented
from film f 
join inventory i using(film_id)
join rental r using(inventory_id)
group by title
order by times_rented desc;

select s.store_id, sum(p.amount) as 'amount earned'
from staff s
join payment p using(staff_id)
group by store_id;

select s.store_id, ci.city, co.country
from store s
join address using (address_id)
join city ci using (city_id)
join country co using (country_id);

select * from rental;