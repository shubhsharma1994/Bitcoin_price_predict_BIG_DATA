CREATE DATABASE IF NOT EXISTS bitcoin_data;


USE bitcoin_data;


CREATE TABLE Pred (
        date String,
        act_price Float,
        pred_code float
        )
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE;


LOAD DATA INPATH '/user/cloudera/Output/pred_values/part-00000' OVERWRITE INTO TABLE pred;

create table price_comp as
select 	pred.date as time,exp(pred.act_price) as orig_price,exp(pred.pred_code) as pred_price
from pred
;


create table Final_data as 
select price_comp.time,price_comp.orig_price,price_comp.pred_price, price_comp.orig_price-price_comp.pred_price as error 
from price_comp;