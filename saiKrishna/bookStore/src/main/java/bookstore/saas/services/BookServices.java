package bookstore.saas.services;
import bookstore.saas.entities.Book;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

public interface BookServices {

    public Mono<Book> create(Book book );

    public Flux<Book>   getAll();

    public Mono<Book> update( int bookId , Book book );

    public Mono<Book> getBook( int bookId );

    public Mono<Void> delete( int bookId );

    public Flux<Book> search( String query );
}
