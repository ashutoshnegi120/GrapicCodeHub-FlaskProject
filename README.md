# GraphicCodeHub Flask Project

This repository contains the source code for my personal project, GraphicCodeHub. It is a web application developed using Flask and Flask-SQLAlchemy. GraphicCodeHub is a social media platform where users can register, create posts, add comments, and interact with other users.

## Features

- User registration: Users can create an account by providing their name, email, username, and password.
- Login and authentication: Users can log in to their accounts securely using their username and password.
- Home page: Users can view a personalized home page with a feed of posts from all users.
- User profiles: Each user has a profile page where they can view and edit their personal information.
- Post creation: Users can create new posts by providing a title and a description/question.
- Commenting: Users can add comments to posts created by themselves or others.
- Post display: Users can view individual posts along with the associated comments.
- My Posts: Users can view a list of all the posts they have created.
- Sign out: Users can log out of their accounts.

## Installation

To run the GraphicCodeHub project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/GraphicCodeHub.git
   ```

2. Navigate to the project directory:

   ```bash
   cd GraphicCodeHub
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database connection:

   - If you are using XAMPP as your database, make sure XAMPP is installed and running.
   - Open the `config.json` file and provide the appropriate values for `local_host` and `public_host` based on your XAMPP configuration.

5. Run the Flask application:

   ```bash
   python app.py
   ```

6. Open your web browser and visit `http://localhost:5000` to access the GraphicCodeHub application.

## Usage

1. Register a new account by providing your name, email, username, and password.
2. Log in to your account using your username and password.
3. Explore the home page to view the posts from other users.
4. Create a new post by providing a title and a description/question.
5. View and interact with other users' posts by clicking on the post title.
6. Add comments to posts to engage in discussions.
7. Access your profile page to view and edit your personal information.
8. View your own posts on the "My Posts" page.
9. Sign out of your account when you are done.

## Contributing

As this is a personal project, I am not actively seeking contributions. However, if you find any issues or have suggestions for improvement, please feel free to open an issue or contact me directly.

## License

This project is licensed under the [MIT License].

## Contact

For any inquiries or feedback related to this personal project, please contact me at [ashutoshnegisgrr@gmail.com].
