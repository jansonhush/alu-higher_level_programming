# SQL - Introduction

These are the SQL scripts I wrote while learning the basics of MySQL: databases, tables, and the main SQL statements (DDL and DML).

## What's inside

- `0-list_databases.sql`: lists all databases
- `1-create_database_if_missing.sql`: creates `hbtn_0c_0` if it doesn't exist
- `2-remove_database.sql`: deletes `hbtn_0c_0` if it exists
- `3-list_tables.sql`: lists the tables of a database
- `4-first_table.sql`: creates `first_table`
- `5-full_table.sql`: prints the full description of `first_table`
- `6-list_values.sql`: lists all rows of `first_table`
- `7-insert_value.sql`: inserts a row in `first_table`
- `8-count_89.sql`: counts the records with `id = 89`
- `9-full_creation.sql`: creates `second_table` and adds rows
- `10-top_score.sql`: lists the records ordered by score
- `11-best_score.sql`: lists the records with a score of 10 or more
- `12-no_cheating.sql`: updates Bob's score using his name
- `13-change_class.sql`: removes the records with a score of 5 or less
- `14-average.sql`: computes the average score
- `15-groups.sql`: counts the records for each score
- `16-no_link.sql`: lists the records that have a name

## How to run

Pipe a script into `mysql`, passing the database name as an argument when the script needs one:

```bash
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## Author

Janson ([jansonhush](https://github.com/jansonhush))
