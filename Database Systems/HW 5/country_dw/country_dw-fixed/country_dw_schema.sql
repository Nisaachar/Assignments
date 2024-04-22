
drop table country_fact;
drop table region;
drop table population;
drop table area;

create table region
(cid number,
 country_name varchar2(60),
 region_name varchar2(60),
 continent6 varchar2(10), 
 continent5 varchar2(10),
 continent4 varchar2(12),
 primary key (cid));


create table population
(pid number(3),
 range varchar2(30),
 primary key (pid));


create table area
(aid number(3),
 range varchar2(30),
 primary key (aid));


create table country_fact
(cid number(3), 
 pid number(3), 
 aid number(3), 
 gdp number,
 foreign key (cid) references region(cid),
 foreign key (pid) references population(pid),
 foreign key (aid) references area(aid));


