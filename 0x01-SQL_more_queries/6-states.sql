-- creates DB hbtn_0d_usa and table 'states'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states(
    id INT PRIMARY KEY,
    name VARCHAR(256)
);
