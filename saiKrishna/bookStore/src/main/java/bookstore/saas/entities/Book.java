package bookstore.saas.entities;
import org.springframework.data.annotation.Id;
import org.springframework.data.relational.core.mapping.Column;
import org.springframework.data.relational.core.mapping.Table;

@Table("book")
public class Book {

    @Id
    @Column("book_id")
    private int bookId ;

    private String name;

    @Column("book_desc")
    private String description;

    private String publisher;

    private String auther;

    //Here we are using constructor and getter setter instead of lombok because it's only one class .( Our wish we can use lombok also )
    public Book(int bookId, String name, String description, String publisher, String auther) {
        this.bookId = bookId;
        this.name = name;
        this.description = description;
        this.publisher = publisher;
        this.auther = auther;
    }

    public Book() {
    }

    public int getBookId() {
        return bookId;
    }

    public void setBookId(int bookId) {
        this.bookId = bookId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getPublisher() {
        return publisher;
    }

    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }

    public String getAuther() {
        return auther;
    }

    public void setAuther(String auther) {
        this.auther = auther;
    }
}
