const mongoose = require('mongoose');

const { Schema } = mongoose;

const BookSchema = new Schema({
  title: {
    type: String,
    required: [true, 'Provide a title.'],
    trim: true,
    minlength: [3, 'Provide at least 3 characters.']
  },
  author: {
    type: String,
    required: [true, 'Provide a title.'],
    trim: true
  },
  pages: {
    type: Number,
    min: 1,
    required: true
  },
  year: Number,
  publisher: String
},
  {
    timestamps: true,
  }
);

module.exports = mongoose.model('Book', BookSchema);
