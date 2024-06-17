# Write your MySQL query statement below

with cte1 as (
    select user_id, count(user_id) as cnt
    from MovieRating
    group by user_id
), 
cte2 as (
    select movie_id, avg(rating) as rating
    from MovieRating
    where created_at between '2020-02-01' and '2020-02-29'
    group by movie_id
),
cte3 as (
    select Users.name as results from cte1
    inner join Users
    on Users.user_id = cte1.user_id
    order by cte1.cnt desc, Users.name  
    limit 1),
cte4 as (
    select Movies.title as results from cte2
    inner join Movies
    on Movies.movie_id = cte2.movie_id
    order by rating desc, Movies.title
    limit 1)

select * from cte3
union all
select * from cte4
    