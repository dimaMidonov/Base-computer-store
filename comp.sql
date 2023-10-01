CREATE TABLE client (
    ID_client INT PRIMARY KEY,
    FIO VARCHAR(255),
    city VARCHAR(255),
    street VARCHAR(255),
    house VARCHAR(255),
    telephone VARCHAR(20),
    email VARCHAR(255)
);
CREATE TABLE manager (
    ID_manager INT PRIMARY KEY,
    FIO VARCHAR(255),
    telephone VARCHAR(20),
    email VARCHAR(255)
);
CREATE TABLE administrator (
    ID_administrator INT PRIMARY KEY,
    FIO VARCHAR(255),
    email VARCHAR(255)
);
CREATE TABLE product_category (
    ID_category INT PRIMARY KEY,
    title VARCHAR(255)
);
CREATE TABLE product (
    ID_product INT PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    cost DECIMAL(10, 2),
    ID_category INT,
    FOREIGN KEY (ID_category) REFERENCES product_category(ID_category)
);
CREATE TABLE warehouse (
    ID_warehouse INT PRIMARY KEY,
    city VARCHAR(255),
    street VARCHAR(255),
    house VARCHAR(255),
    quantity_of_goods INT,
    ID_product INT,
    FOREIGN KEY (ID_product) REFERENCES product(ID_product)
);
CREATE TABLE orders (
    ID_order INT PRIMARY KEY,
    order_date DATE,
    ID_client INT,
    ID_manager INT,
    ID_administrator INT,
    FOREIGN KEY (ID_client) REFERENCES client(ID_client),
    FOREIGN KEY (ID_manager) REFERENCES manager(ID_manager),
    FOREIGN KEY (ID_administrator) REFERENCES administrator(ID_administrator)
);
CREATE TABLE order_history (
    ID_history INT PRIMARY KEY,
    ID_order INT,
    ID_client INT,
    FOREIGN KEY (ID_order) REFERENCES orders(ID_order),
    FOREIGN KEY (ID_client) REFERENCES client(ID_client)
);
CREATE TABLE order_details (
    ID_order_details INT PRIMARY KEY,
    ID_order INT,
    ID_product INT,
    quantity INT,
    interim_result DECIMAL(10, 2),
    FOREIGN KEY (ID_order) REFERENCES orders(ID_order),
    FOREIGN KEY (ID_product) REFERENCES product(ID_product)
);
CREATE TABLE remains_product (
    ID_remains INT PRIMARY KEY,
    ID_warehouse INT,
    ID_product INT,
    FOREIGN KEY (ID_warehouse) REFERENCES warehouse(ID_warehouse),
    FOREIGN KEY (ID_product) REFERENCES product(ID_product)
);