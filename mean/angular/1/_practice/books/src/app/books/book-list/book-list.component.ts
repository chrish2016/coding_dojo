import { Component, OnInit } from '@angular/core';
import { Book } from '../../models/book';
import { BOOKS } from '../../data/book-data';


@Component({
  selector: 'app-book-list',
  templateUrl: './book-list.component.html',
  styleUrls: ['./book-list.component.css']
})
export class BookListComponent implements OnInit {
  books: Book[] = BOOKS;
  selectedBook: Book;


  // constructor() { }

  ngOnInit() {
  }
  onSelect(book: Book) {
    console.log('on select...', book);
    this.selectedBook = (this.selectedBook === book) ? null : book;
  }
  onCreate(book: Book) {
    console.log('creating book', book);
    this.books.push(book);
  }
}
