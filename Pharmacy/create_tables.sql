-- create_tables.sql

-- Users Table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL
);

-- Drugs Table
CREATE TABLE drugs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    drug_name VARCHAR(255) NOT NULL,
    manufacturer VARCHAR(255),
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Sales Table
CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    drug_id INT,
    quantity INT NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    sale_date DATE,
    FOREIGN KEY (drug_id) REFERENCES drugs(id)
);

-- History Sales Table
CREATE TABLE history_sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    drug_id INT,
    quantity_sold INT NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    sale_date DATE,
    FOREIGN KEY (drug_id) REFERENCES drugs(id)
);

-- Company Table (assuming this was one of your entities)
CREATE TABLE company (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    industry VARCHAR(255)
);
