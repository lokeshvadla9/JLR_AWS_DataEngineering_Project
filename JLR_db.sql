CREATE TABLE tblCar (
    Id INT PRIMARY KEY,
    make VARCHAR(50),
    model VARCHAR(50),
    year INT,
    color VARCHAR(20),
    engine_type VARCHAR(50),
    price DECIMAL(10, 2)
);

CREATE TABLE tblCustomer (
    Id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone_number VARCHAR(20),
    address VARCHAR(200)
);

CREATE TABLE tblOrder (
    Id INT PRIMARY KEY,
    car_id INT FOREIGN KEY REFERENCES tblCar(Id),
    customer_id INT FOREIGN KEY REFERENCES tblCustomer(Id),
    order_date DATETIME,
    delivery_date DATETIME,
    total_price DECIMAL(10, 2)
);

CREATE TABLE tblEmployee (
    Id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    job_title VARCHAR(100),
    hire_date DATETIME
);

CREATE TABLE tblServiceRecord (
    Id INT PRIMARY KEY,
    car_id INT FOREIGN KEY REFERENCES tblCar(Id),
    service_date DATETIME,
    description VARCHAR(200),
    cost DECIMAL(10, 2)
);

CREATE TABLE tblSupplier (
    Id INT PRIMARY KEY,
    company_name VARCHAR(100),
    contact_name VARCHAR(100),
    contact_email VARCHAR(100),
    phone_number VARCHAR(20)
);

CREATE TABLE tblPart (
    Id INT PRIMARY KEY,vi
    part_name VARCHAR(100),
    description VARCHAR(200),
    price DECIMAL(10, 2),
    supplier_id INT FOREIGN KEY REFERENCES tblSupplier(Id)
);

CREATE TABLE tblInventory (
    Id INT PRIMARY KEY,
    part_id INT FOREIGN KEY REFERENCES tblPart(Id),
    quantity_in_stock INT,
    reorder_threshold INT
);

CREATE TABLE tblSalesTransaction (
    Id INT PRIMARY KEY,
    order_id INT FOREIGN KEY REFERENCES tblOrder(Id),
    employee_id INT FOREIGN KEY REFERENCES tblEmployee(Id),
    transaction_date DATETIME,
    payment_method VARCHAR(50),
    amount_paid DECIMAL(10, 2)
);

CREATE TABLE tblMaintenanceRecord (
    Id INT PRIMARY KEY,
    car_id INT FOREIGN KEY REFERENCES tblCar(Id),
    employee_id INT FOREIGN KEY REFERENCES tblEmployee(Id),
    maintenance_date DATETIME,
    description VARCHAR(200),
    cost DECIMAL(10, 2)
);

CREATE TABLE tblWarranty (
    Id INT PRIMARY KEY,
    car_id INT FOREIGN KEY REFERENCES tblCar(Id),
    start_date DATETIME,
    end_date DATETIME,
    coverage_details VARCHAR(200)
);
