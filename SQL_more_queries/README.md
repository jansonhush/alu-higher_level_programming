# SQL - More queries

These are the SQL scripts I wrote while learning users and privileges, constraints, foreign keys, subqueries and joins in MySQL.

## What's inside

- `0-privileges.sql`: lists the privileges of `user_0d_1` and `user_0d_2`
- `1-create_user.sql`: creates `user_0d_1` with all privileges
- `2-create_read_user.sql`: creates `hbtn_0d_2` and `user_0d_2` (SELECT only)
- `3-force_name.sql`: table with a `NOT NULL` name
- `4-never_empty.sql`: table with a default `id`
- `5-unique_id.sql`: table with a unique `id`
- `6-states.sql`: database `hbtn_0d_usa` and table `states`
- `7-cities.sql`: table `cities` with a foreign key to `states`
- `8-cities_of_california_subquery.sql`: cities of California using a subquery
- `9-cities_by_state_join.sql`: all cities with their state using a join
- `10-genre_id_by_show.sql`: shows with at least one genre
- `11-genre_id_all_shows.sql`: all shows, `NULL` when there is no genre
- `12-no_genre.sql`: shows without a genre
- `13-count_shows_by_genre.sql`: number of shows for each genre
- `14-my_genres.sql`: genres of the show Dexter
- `15-comedy_only.sql`: all Comedy shows
- `16-shows_by_genre.sql`: all shows with all their genres

## How to run

Pipe a script into `mysql`, passing the database name when the script needs one:

```bash
cat 1-create_user.sql | mysql -hlocalhost -uroot -p
cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
```

Tasks 10 to 16 use the `hbtn_0d_tvshows` database, which is imported from the dump given in the project.

## Author

Janson ([jansonhush](https://github.com/jansonhush))
