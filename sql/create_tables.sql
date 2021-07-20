create table article_table(
    id varchar primary key,
    path varchar not null,
    seasons json,
    body varchar,
    author_name varchar not null,
    author_id varchar not null,
    created_date varchar not null,
    created_time varchar not null,
    updated_date varchar,
    updated_time varchar,
    counters_total int not null
);
