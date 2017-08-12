#一些MySQL基本操作～

hadoop@b2utyyomi-VPCEG18FG:/media/hadoop/TAEKWOON/PYTHON/Net_data/store_data$ mysql -uroot -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 5.7.19-0ubuntu0.16.04.1 (Ubuntu)

Copyright (c) 2000, 2017, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> create database test; # CREATE DATABASE test;
Query OK, 1 row affected (0.00 sec)

mysql> use test; # USE test;
Database changed
mysql> CREATE TABLE pages;
ERROR 1113 (42000): A table must have at least 1 column
mysql> CREATE TABLE pages (id BIGINT(7) NOT NULL AUTO_INCREMENT, title VARCHAR(200), content VARCHAR(10000), created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY(id));
Query OK, 0 rows affected (0.39 sec)

mysql> DESCRIBE pages;
+---------+----------------+------+-----+-------------------+----------------+
| Field   | Type           | Null | Key | Default           | Extra          |
+---------+----------------+------+-----+-------------------+----------------+
| id      | bigint(7)      | NO   | PRI | NULL              | auto_increment |
| title   | varchar(200)   | YES  |     | NULL              |                |
| content | varchar(10000) | YES  |     | NULL              |                |
| created | timestamp      | NO   |     | CURRENT_TIMESTAMP |                |
+---------+----------------+------+-----+-------------------+----------------+
4 rows in set (0.00 sec)

mysql> INSERT INTO pages (title, content) VALUES ("Test page title", "This is some test page content. It can be up to 10,000 characters long.");
Query OK, 1 row affected (0.05 sec)

mysql> SELECT * FROM pages;
+----+-----------------+-------------------------------------------------------------------------+---------------------+
| id | title           | content                                                                 | created             |
+----+-----------------+-------------------------------------------------------------------------+---------------------+
|  1 | Test page title | This is some test page content. It can be up to 10,000 characters long. | 2017-07-27 18:57:22 |
+----+-----------------+-------------------------------------------------------------------------+---------------------+
1 row in set (0.00 sec)

mysql> INSERT INTO pages (id, title, content) VALUES (2, "oppa", "DaeHyun, TaekWoon, SuperJunior, SHINee, EXO, BTS");
Query OK, 1 row affected (0.05 sec)

mysql> SELECT * FROM pages;
+----+-----------------+-------------------------------------------------------------------------+---------------------+
| id | title           | content                                                                 | created             |
+----+-----------------+-------------------------------------------------------------------------+---------------------+
|  1 | Test page title | This is some test page content. It can be up to 10,000 characters long. | 2017-07-27 18:57:22 |
|  2 | oppa            | DaeHyun, TaekWoon, SuperJunior, SHINee, EXO, BTS                        | 2017-07-27 19:00:44 |
+----+-----------------+-------------------------------------------------------------------------+---------------------+
2 rows in set (0.00 sec)

mysql> SELECT content FROM pages WHERE id = 2;
+--------------------------------------------------+
| content                                          |
+--------------------------------------------------+
| DaeHyun, TaekWoon, SuperJunior, SHINee, EXO, BTS |
+--------------------------------------------------+
1 row in set (0.00 sec)

mysql> SELECT title,id FROM pages WHERE content LIKE "%Super%";
+-------+----+
| title | id |
+-------+----+
| oppa  |  2 |
+-------+----+
1 row in set (0.01 sec)

mysql> DELETE FROM pages WHERE id = 3;
Query OK, 0 rows affected (0.00 sec)

mysql> UPDATE pages SET title="A new title", content="Some new content" WHERE id = 1;
Query OK, 1 row affected (0.06 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM pages;
+----+-------------+--------------------------------------------------+---------------------+
| id | title       | content                                          | created             |
+----+-------------+--------------------------------------------------+---------------------+
|  1 | A new title | Some new content                                 | 2017-07-27 18:57:22 |
|  2 | oppa        | DaeHyun, TaekWoon, SuperJunior, SHINee, EXO, BTS | 2017-07-27 19:00:44 |
+----+-------------+--------------------------------------------------+---------------------+
2 rows in set (0.00 sec)
mysql> USE scraping
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A
# 为了支持Unicode字符处理 必须进行下面的处理
mysql> ALTER DATABASE scraping CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
mysql> ALTER TABLE pages CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
mysql> ALTER TABLE pages CHANGE title title VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
mysql> ALTER TABLE pages CHANGE content content VARCHAR(10000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
mysql> SELECT * FROM pages;
+----+------------------+-------------------+---------------------+
| id | title            | content           | created             |
+----+------------------+-------------------+---------------------+
|  2 | 欧巴             | hahahaha hahahaha | 2017-07-27 17:38:08 |
|  4 | Test pages title | hahahaha hahahaha | 2017-07-27 17:36:24 |
+----+------------------+-------------------+---------------------+
2 rows in set (0.00 sec)





