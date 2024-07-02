# select
#     a.project_id,
#     b.employee_id,
#     b.name,
#     b.experience_years
# from Project as a
# inner join Employee b
#     on a.employee_id = b.employee_id


# select
#     a.project_id,
#     b.employee_id,
#     b.name,
#     b.experience_years
# from Project as a
# inner join Employee b
#     on a.employee_id = b.employee_id
# group by project_id

# select
#     a.project_id,
#     b.employee_id,
#     b.name,
#     avg(b.experience_years)
# from Project as a
# inner join Employee b
#     on a.employee_id = b.employee_id
# group by project_id


# select
#     a.project_id,
#     b.employee_id,
#     b.name,
#     round(avg(b.experience_years),2)
# from Project as a
# inner join Employee b
#     on a.employee_id = b.employee_id
# group by project_id

select
    a.project_id,
    round(avg(b.experience_years),2) as average_years
from Project as a
inner join Employee b
    on a.employee_id = b.employee_id
group by project_id
    
    