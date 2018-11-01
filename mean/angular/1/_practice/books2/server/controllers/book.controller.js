const Book = require('mongoose').model('Book');

module.exports = {
  // get all of resource
  index(request, response) {
    Book.find({})
      .then(books => response.json(books))
      .catch(console.log)
   },
  show(request, response) {
    Book.findById(request.params.book_id)
      .then(book => response.json(book))
   },
  create(request, response) {
    Book.create(request.body)
      .then(book => response.json(book))
      .catch(error => {
        const errors = Object.keys(error.errors).map(key => error.errors[key].message);
        response.status(402).json(errors);
      });
   },
  update(request, response) {
    Book.findByIdAndUpdate(request.params.book_id, request.body, { new: true })
      .then(book => response.json(book))
      .catch(console.log);
   },
  destroy(request, response) {
    Book.findByIdAndRemove(request.params.book_id)
      .then(book => response.json(book))
      .catch(console.log);
   },
};
