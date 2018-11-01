import { Component, OnInit } from '@angular/core';
import { BookService } from '../../services';

import { Book } from '../../models/book';
// import { BOOKS } from '../../data/book-data';


@Component({
  selector: 'app-book-list',
  templateUrl: './book-list.component.html',
  styleUrls: ['./book-list.component.css']
})
export class BookListComponent implements OnInit {
  books: Book[] = [];
  selectedBook: Book;

  constructor(
    private readonly bookService: BookService
  ) {}

  ngOnInit() {
   this.bookService.getBooks()
    .subscribe(books => {
      this.books = books;
    });
  }

  onSelect(book: Book) {
    console.log('on select...', book);
    this.selectedBook = (this.selectedBook === book) ? null : book;
  }
  onCreate(event: Book) {
    console.log('creating book', event);
    this.books.push(event);
  }
  onDelete(id: number){
    console.log('delete.');
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
