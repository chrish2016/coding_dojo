import { Component, OnInit } from '@angular/core';
import { Book } from '../../models/book';
import { BOOKS } from '../../data/book-data';
import { BookService } from '../../services';


@Component({
  selector: 'app-book-list',
  templateUrl: './book-list.component.html',
  styleUrls: ['./book-list.component.css'],
})
export class BookListComponent implements OnInit {
  books: Book[] = [];
  selectedBook: Book;
  constructor(private bookService: BookService) { }

  ngOnInit() {
    this.bookService.getBooks().subscribe(books => {
      this.books = books;
    });
  }

  onSelect(book: Book) {
    console.log('on select...', book);
    this.selectedBook = (this.selectedBook === book) ? null : book;
  }

  onCreate(book: Book) {
    console.log('creating book', book);
    this.bookService.createBook(book)
      .subscribe(createdBook => {
      // this.books.push(createdBook);
      this.books = [...this.books, createdBook];
    });
  }

  onRemove(id: number) {
    console.log('removed book...');

    this.bookService.removeBook(id)
      .subscribe(deletedBook => {
        this.books = this.books.filter(book => book.id !== deletedBook.id);
      });
  }

  onEvent(event: Event) {
    event.stopPropagation();
    console.log('event..');
  }
}
