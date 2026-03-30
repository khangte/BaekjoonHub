with rental_base as (
    select 
        h.history_id
        , h.car_id
        , c.car_type
        , c.daily_fee
        , datediff(h.end_date, h.start_date)+1 as rental_duration
    from car_rental_company_rental_history as h
    join car_rental_company_car as c
    on h.car_id = c.car_id
    where c.car_type = '트럭'
)
select rb.history_id
    , round(
        rb.daily_fee * rb.rental_duration * (100-coalesce(p.discount_rate, 0))/100
        , 0
    ) as fee
from rental_base as rb
left join car_rental_company_discount_plan as p
on rb.car_type = p.car_type 
    and p.duration_type = case
        when rb.rental_duration>=90 then '90일 이상'
        when rb.rental_duration>=30 then '30일 이상'
        when rb.rental_duration>=7 then '7일 이상'
    end
order by fee desc, rb.history_id desc
;