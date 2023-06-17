# Movie Ticket Booking System

This is a movie ticket booking system built using Django, Jinja templates, HTML, and CSS.

## Features

- User registration and authentication: Users can create accounts and log in to the system.
- Movie listings: Users can view a list of available movies.
- Seat selection: Users can select seats for a specific movie and showtime.
- Ticket cancellation: Users can cancel their booked tickets and get a refund.
- Booking confirmation: Users receive a confirmation message after successfully booking tickets.
- Movie reviews: Users can write reviews for movies they have watched.
- Feedback submission: Users can provide feedback, suggestions, or complaints regarding the system.
- Admin panel: Administrators can manage movies, showtimes, and bookings.

## Installation

1. Clone the repository:
https://github.com/Bfindik/movie_project.git
2. Change into the project directory:
cd movie_project
3. Create a virtual environment:
python3 -m venv venv

4. Activate the virtual environment:

- For macOS/Linux:

  ```
  source venv/bin/activate
  ```

- For Windows (Command Prompt):

  ```
  venv\Scripts\activate.bat
  ```

5. Run database migrations:
   ```
   pyhton manage.py makemigrations
   python manage.py migrate 
   ```
7. Create a superuser (admin):
   ```
   python manage.py createsuperuser
   ```
8. Start the development server:
   ```
   python manage.py runserver
   ```
   
9. Open your browser and navigate to `http://localhost:8000` to access the application.

## Usage

- To access the admin panel, go to `http://localhost:8000/admin` and log in with your admin credentials.

- As an admin, you can manage movies, showtimes, bookings, reviews, and feedback.

- Regular users can browse movies, select seats, book tickets, cancel their booked tickets to get a refund, write reviews for movies, and provide feedback, suggestions, or complaints.4
## Database

This project uses SQLite as the database by default. The SQLite database file is located at `db.sqlite3` in the project directory.

If you want to use a different database, you can update the database configuration in the `settings.py` file.


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Contrubuters

- Sevda Karahan
- Elif İnce
- Zeynep Özkayıkçı
- Orhan Sina Alış






