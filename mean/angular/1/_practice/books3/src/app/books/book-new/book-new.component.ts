import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { NgForm } from '@angular/forms';

import { Book } from '../../models/book';

import { BookService } from '../../services';

@Component({
  selector: 'app-book-new',
  templateUrl: './book-new.component.html',
  styleUrls: ['./book-new.component.css']
})
export class BookNewComponent implements OnInit {
  book = new Book();
  @Output()
  createBook = new EventEmitter<Book>();

  constructor(private readonly bookService: BookService) { }

  ngOnInit() {
  }

  onSubmit(event: Event, form: NgForm) {
    event.preventDefault();
    console.log('submitting form...', this.book);

    this.bookService.createBook(this.book)
      .subscribe(book => {
        this.createBook.emit(book);
        this.book = new Book();
        form.reset();
      });
  }
}
