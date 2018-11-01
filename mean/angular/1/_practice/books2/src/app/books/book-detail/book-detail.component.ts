import { Component, OnInit, Input } from '@angular/core';
import { Book } from 'src/app/models/book';
// import { Book } from '../../models/book';
// import { BOOKS } from '../../data/book-data';

@Component({
  selector: 'app-book-detail',
  templateUrl: './book-detail.component.html',
  styleUrls: ['./book-detail.component.css']
})
export class BookDetailComponent implements OnInit {
  @Input()
  book: Book;
  // selectedBook: Book;

  constructor() { }

  ngOnInit() {
  }

}
