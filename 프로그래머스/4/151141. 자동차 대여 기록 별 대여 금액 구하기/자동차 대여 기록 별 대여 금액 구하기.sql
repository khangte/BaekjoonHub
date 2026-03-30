with a as (
    select 
        h.history_id
        , h.car_id
        , c.car_type
        , datediff(h.end_date, h.start_date)+1 as rental_duration
        , case
            when datediff(h.end_date, h.start_date)+1 >=90 then '90일 이상'
            when datediff(h.end_date, h.start_date)+1 >=30 then '30일 이상'
            when datediff(h.end_date, h.start_date)+1 >=7 then '7일 이상'
        end as duration_type
        , c.daily_fee * (datediff(h.end_date, h.start_date)+1) as og_fee
    from car_rental_company_rental_history as h
    join car_rental_company_car as c
    on h.car_id = c.car_id
    where c.car_type = '트럭'
)

select a.history_id
    , case
        when a.duration_type is not null then round(a.og_fee*(100-p.discount_rate)/100, 0)
        else a.og_fee
    end as fee
from a as a
left join car_rental_company_discount_plan as p
on a.car_type = p.car_type and a.duration_type = p.duration_type
order by fee desc, a.history_id desc
;