package bookstore.saas.controller;
import bookstore.saas.entities.Book;
import bookstore.saas.services.BookServices;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

@RestController
@RequestMapping( "/api/bookstore" )
public class bookController {

    @Autowired
    private BookServices bookService;

    @PostMapping("/createBook")
    public Mono<Book> createBook( @RequestBody Book book){
        return bookService.create(book);
    }

    @GetMapping("/getBooks")
    public Flux<Book> getAllBooks(){
        return bookService.getAll();
    }

    @GetMapping("/getBook")
    public Mono<Book> book(int bookId){
        return bookService.getBook(bookId);
    }

    @DeleteMapping("/delete/{book_id}")
    public Mono<ResponseEntity<String>> bookDelete(@PathVariable int book_id ){
//        return bookService.delete(book_id).map( deleteId -> deleteId ?
//                ResponseEntity.ok("Book found with ID: " + book_id ) :
//                ResponseEntity.status(HttpStatus.NOT_FOUND).body( "Book not found with ID: " + book_id )) ;
        return bookService.delete(book_id)
                .then(Mono.just(ResponseEntity.ok("Book with ID " + book_id + " deleted successfully.")))
                .onErrorResume(e ->
                        Mono.just(ResponseEntity.status(HttpStatus.NOT_FOUND)
                                .body("Book not found with ID: " + book_id))
                );
    }

}
