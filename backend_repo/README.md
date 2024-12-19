## Task:

### Implement an API endpoint for the scenario below:

- Imagine that a frontend design has been drafted to present data that we already have in our DB: `Posts` and `Comments`.

  - The design is an infinite scrolling list of `Posts`.

- The list of `Posts` should be ordered by timestamp, latest first.

- Some `Posts` will have `Comments`.

- For each `Post` in this list, we want to show up to 3 `Comments` for that `Post` (`Comments` also sorted latest first).

  - For each `Post`: we will need to display a `Post`'s text, timestamp, `Comment` count, and author's username.

  - For `Comments`: we will need to display a `Comment`'s text, timestamp, and author's username.

- Include basic documentation on how to use your new endpoint.

### Follow-up Q:

- Instead of sorting comments by timestamp, how would you fetch 3 random comments associated to a given post?
  - You can leave your answer anywhere in the project codebase that you deem appropriate.

---

## To get started:

1. Set up a virtualenv for this project (The author used Python 3.10.14)

- Example: `pyenv local myvirtualenv` (or however you set up Python virtualenvs)

2. Install dependencies: `pip install -r requirements.txt`

3. Migrate database `python manage.py migrate`

4. Now head to apps/demo/views.py and complete the assignment!

- Run tests via `python manage.py test apps` or
- check server after running via `python manage.py runserver`

# API Documentation

This document outlines the available endpoints for the API, their functionality, request methods, and expected payloads.

## **Base URL**: `http://127.0.0.1:8000/`

## **User Endpoints**

### Create User

- **URL**: `/users/`
- **Method**: `POST`
- **Description**: Create a new user.

#### Request Payload:

```json
{
  "username": "string",
  "email": "string"
}
```

#### Response Example (201 Created):

```json
{
  "id": 1,
  "username": "string",
  "email": "string"
}
```

---

## **Post Endpoints**

### Fetch Posts (Infinite Scroll)

- **URL**: `/posts/`
- **Method**: `GET`
- **Description**: Retrieve a paginated list of posts.

#### Query Parameters:

- `page`: Page number.

#### Response Example:

```json
{
  "count": 50,
  "next": "http://127.0.0.1:8000/posts/?page=2",
  "previous": null,
  "results": [
    {
      "id": "uuid",
      "text": "Post content",
      "timestamp": "2023-12-18T10:00:00Z",
      "author": "username",
      "comment_count": 5,
      "comments": [
        {
          "text": "Comment content",
          "timestamp": "2023-12-18T10:05:00Z",
          "author": "username"
        }
      ]
    }
  ]
}
```

### Create Post

- **URL**: `/posts/create/`
- **Method**: `POST`
- **Description**: Create a new post.

#### Request Payload:

```json
{
  "user": 1,
  "text": "Post content"
}
```

#### Response Example (201 Created):

```json
{
  "id": "uuid",
  "text": "Post content",
  "timestamp": "2023-12-18T10:00:00Z",
  "user": 1
}
```

### Update Post

- **URL**: `/posts/<post_id>/`
- **Method**: `PUT`
- **Description**: Update an existing post.

#### Request Payload:

```json
{
  "text": "Updated post content"
}
```

#### Response Example (200 OK):

```json
{
  "id": "uuid",
  "text": "Updated post content",
  "timestamp": "2023-12-18T10:00:00Z",
  "user": 1
}
```

### Delete Post

- **URL**: `/posts/<post_id>/delete/`
- **Method**: `DELETE`
- **Description**: Delete a post.

#### Response Example (204 No Content):

```json
{
  "message": "Post deleted successfully"
}
```

---

## **Comment Endpoints**

### Create Comment

- **URL**: `/posts/<post_id>/comments/`
- **Method**: `POST`
- **Description**: Add a comment to a post.

#### Request Payload:

```json
{
  "user": 1,
  "text": "Comment content"
}
```

#### Response Example (201 Created):

```json
{
  "id": "uuid",
  "text": "Comment content",
  "timestamp": "2023-12-18T10:00:00Z",
  "post": "uuid",
  "user": 1
}
```

### Fetch All Comments for a Post

- **URL**: `/posts/<post_id>/comments/all/`
- **Method**: `GET`
- **Description**: Retrieve all comments for a specific post.

#### Response Example (200 OK):

```json
[
  {
    "text": "Comment content",
    "timestamp": "2023-12-18T10:00:00Z",
    "author": "username"
  }
]
```

### Fetch Random Comments for a Post

- **URL**: `/posts/<post_id>/comments/random/`
- **Method**: `GET`
- **Description**: Retrieve three random comments for a specific post.

#### Response Example (200 OK):

```json
[
  {
    "text": "Random comment 1",
    "timestamp": "2023-12-18T10:00:00Z",
    "author": "username"
  },
  {
    "text": "Random comment 2",
    "timestamp": "2023-12-18T10:01:00Z",
    "author": "username"
  }
]
```

---

## **Error Responses**

### Validation Errors

#### Example (400 Bad Request):

```json
{
  "error": "Validation failed",
  "details": {
    "field_name": ["Error message"]
  }
}
```

### Not Found

#### Example (404 Not Found):

```json
{
  "error": "Not found"
}
```

---

- For paginated responses, parameters such as `next` and `previous` URLs are provided to navigate through different pages.
- Error handling is consistent across all endpoints, returning meaningful error messages when appropriate.

## Error Handling

- The API includes error responses for various scenarios:
  - **400 Bad Request**: When the request body is invalid or missing required fields.
  - **404 Not Found**: When a requested resource (e.g., user, post, comment) cannot be found.
  - **500 Internal Server Error**: For unexpected server errors.

---
