import { Book } from '../models/book';

export const BOOKS: Book[] = [
  {
    id: randomId(),
    title: 'stranger in a strange land',
    author: 'robert heinlein',
    publisher: 'G.P. Punam',
    year: 1977,
    pages: 408
  },
  {
    id: randomId(),
    title: 'Pigland',
    author: 'bert hein',
    publisher: 'G.P. Punam',
    year: 1977,
    pages: 408
  },
  {
    id: randomId(),
    title: 'land',
    author: 'ert lein',
    publisher: 'G.P. Punam',
    year: 1977,
    pages: 408
  },
];

function randomId(): number {
  return Math.floor(Math.random() * 1000);
}
