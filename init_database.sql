create user todolist identified by 'todolist_db_password';
grant all privileges on todolist.* to todolist@localhost identified by 'todolist_db_password';
flush privileges;
CREATE DATABASE todolist;

use todolist;

CREATE TABLE Project (
    Projectid    int unsigned not null auto_increment,
    Userid       int unsigned not null default 1,
    title        varchar(32)  charset utf8 not null default '',
    created      timestamp not null default current_timestamp,
    primary key  (Projectid)
)ENGINE=InnoDB;

CREATE TABLE Item (
    Itemid       int unsigned not null auto_increment,
    Projectid    int unsigned not null default 0,
    content      varchar(200)  charset utf8 not null default '',
    done         boolean not null default 0,
    created      timestamp not null default current_timestamp,
    primary key  (Itemid)
)ENGINE=InnoDB;
