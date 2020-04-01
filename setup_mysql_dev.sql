-- MySQL server for the project
-- dev_database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE DATABASE IF NOT EXISTS performance_schema;
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
