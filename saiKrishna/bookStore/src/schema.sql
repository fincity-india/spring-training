CREATE table bookstore.book (
    book_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(250),
    book_desc TEXT,
    publisher VARCHAR(250),
    auther VARCHAR(250),
)