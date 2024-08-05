# Unread Books Service

## Overview

The **Unread Books Service** is a microservice implemented using Flask that provides endpoints to view unread books from a JSON file. This service allows users to view a list of unread books and filter them by author.

## Features

- **View All Unread Books**: Returns a list of books with a read status of 'N'.
- **Filter Unread Books by Author**: Returns a list of unread books filtered by a specific author's name.

## Running the Microservice

1. **Start the Flask Application:**

   ```bash
   python microservice.py
   ```

   The service will be running on `http://127.0.0.1:5000`.

## API Endpoints

### View Unread Books

- **Endpoint:** `/view-unread-books`
- **Method:** `GET`
- **Description:** Returns a list of books with the read status 'N'.
- **Example Request:**

  ```bash
  curl http://127.0.0.1:5000/view-unread-books
  ```

- **Example Response:**

  ```json
  [
    {"title": "Book Title", "author": "Author Name", "read": "N"},
    {"title": "Book Title", "author": "Author Name", "read": "N"},
    {"title": "Book Title", "author": "Author Name", "read": "N"}
  ]
  ```

### View Unread Books by Author

- **Endpoint:** `/view-unread-books-by-author`
- **Method:** `GET`
- **Query Parameter:** `author` (Required)
- **Description:** Returns a list of unread books by a specific author.
- **Request Structure:**

  ```bash
  curl "http://127.0.0.1:5000/view-unread-books-by-author?author=Author Name"
  ```

- **Example Request:**

  ```bash
  curl "http://127.0.0.1:5000/view-unread-books-by-author?author=George%20Orwell"
  ```

- **Example Response:**

  ```json
  [
    {"title": "Book Title", "author": "Author Name", "read": "N"}
  ]
  ```

## Error Handling

- **Internal Server Error (500):** Returns an error message indicating an internal error.

  ```json
  {"error": "An internal error occurred."}
  ```
