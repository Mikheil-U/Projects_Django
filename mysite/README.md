# Django Blog Website

This is a Django-powered blog website where users with admin privileges can create, update, and delete posts. The site also supports user comments, which can be reviewed, approved, or removed by admins.

## Features

- **Post Management**: Admin users can create, update, and delete posts.
- **Commenting System**: Users can leave comments on posts. Admins can approve or remove comments.
- **Drafts**: Admins can save posts as drafts and publish them later.
- **Pagination**: Blog posts are paginated, showing 5 posts per page.
- **User Authentication**: Only authenticated users can create, update, or delete posts and comments.

![image](https://github.com/user-attachments/assets/81e7e201-53aa-490f-bdb6-b755953d3cce)
![image](https://github.com/user-attachments/assets/e98626f5-f82d-4be8-ba4b-2a9c08572ed1)
![image](https://github.com/user-attachments/assets/c94cfabf-eefe-427e-b8f2-7ba7d16992c0)
![image](https://github.com/user-attachments/assets/fd794c6e-feab-4e0b-994d-8a940caeea89)
![image](https://github.com/user-attachments/assets/49bd3ab1-bc4d-4fd8-9771-064ced743aa5)


## Models

### Post Model
- `author`: The user who authored the post.
- `title`: The title of the post.
- `text`: The content of the post.
- `create_date`: The date and time when the post was created.
- `published_date`: The date and time when the post was published.

### Comment Model
- `post`: The post to which the comment belongs.
- `author`: The name of the comment's author.
- `text`: The content of the comment.
- `create_date`: The date and time when the comment was created.
- `approved_comment`: Boolean indicating if the comment is approved.

## Views

- `AboutView`: A static page that provides information about the blog.
- `PostListView`: Displays a list of published posts with pagination.
- `PostDetailView`: Displays the details of a single post, including comments.
- `CreatePostView`: Allows admin users to create a new post.
- `UpdatePostView`: Allows admin users to update an existing post.
- `DeletePostView`: Allows admin users to delete a post.
- `DraftListView`: Displays all draft posts created by the logged-in admin user.
- `post_publish`: Publishes a draft post.
- `add_comment_to_post`: Allows users to add comments to a post.
- `comment_approve`: Allows admin users to approve a comment.
- `comment_remove`: Allows admin users to remove a comment.
- `logout_user`: Logs out the current user.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Mikheil-U/Projects_Django/mysite.git
    cd mysite
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Access the website at `http://127.0.0.1:8000`.

## Usage

- **Admin Panel**: Access the admin panel at `http://127.0.0.1:8000/admin` to manage users, posts, and comments.
- **Creating Posts**: Admin users can create new posts by navigating to `http://127.0.0.1:8000/posts/new/`.
- **Managing Comments**: Admin users can approve or remove comments from the post detail page.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

## License

This project is licensed under the MIT License.
