package bookstore.saas.services.imple;
import bookstore.saas.entities.Book;
import bookstore.saas.repositories.BookRepository;
import bookstore.saas.services.BookServices;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;


@Service
public class serviceImplement implements BookServices {

    @Autowired
    private BookRepository bookRepository ;

    @Override
    public Mono<Book> create(Book book) {
        Mono<Book> save = bookRepository.save(book);
        return save;
    }

    @Override
    public Flux<Book> getAll() {
        return bookRepository.findAll();
    }

    @Override
    public Mono<Book> update(int bookId, Book book) {
        return bookRepository.findById(bookId).flatMap( book1 -> {
            book1.setName(book.getName());
            book1.setDescription(book.getDescription());
            book1.setPublisher(book.getPublisher());
            book1.setAuther(book.getAuther());
            return bookRepository.save(book1);
        } );
    }

    @Override
    public Mono<Book> getBook(int bookId) {
        return bookRepository.findById(bookId);
    }

    @Override
    public Mono<Void> delete(int bookId) {
        return bookRepository.findById(bookId).flatMap( book -> bookRepository.delete(book));
    }

    @Override
    public Flux<Book> search(String query) {
//        return bookRepository.findByTitleContainingIgnoreCase(query);
        return null;
    }
}
