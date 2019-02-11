-----------------------------------------------
STUDIO SOLUTION DATABASES 2
-----------------------------------------------
1. SELECT DISTINCT country FROM directors;
2. SELECT * FROM directors WHERE country = "France";
3. SELECT MIN(date_viewed) FROM viewings;
4. SELECT COUNT(*) FROM movies INNER JOIN directors ON movies.director_id = directors.director_id WHERE directors.country = "USA";
5. SELECT movies.title FROM movies INNER JOIN directors ON directors.director_id = movies.director_id WHERE directors.first = "Akira" AND directors.last = "Kurosawa";
6. SELECT COUNT(*) FROM viewings INNER JOIN movies ON viewings.movie_id = movies.movie_id WHERE movies.title = "Talk to Me";
7. SELECT MAX(date_viewed) FROM viewings;
8. SELECT movie_id FROM viewings WHERE date_viewed = (SELECT MAX(date_viewed) FROM viewings);
9. SELECT movies.title FROM movies INNER JOIN viewings ON movies.movie_id = viewings.movie_id WHERE viewings.date_viewed = (SELECT MIN(date_viewed) FROM viewings);
10. SELECT viewers.first, viewers.last FROM viewers INNER JOIN viewings ON viewers.viewer_id = viewings.viewer_id WHERE viewings.date_viewed = (SELECT MIN(date_viewed) FROM viewings);
11. SELECT title, COUNT(*) FROM viewings INNER JOIN movies ON viewings.movie_id = movies.movie_id GROUP BY viewings.movie_id ORDER BY COUNT(*) DESC;
12. SELECT email FROM viewers 
INNER JOIN viewings
ON viewings.viewer_id = viewers.viewer_id
INNER JOIN movies
ON movies.movie_id = viewings.movie_id
WHERE movies.title = "The Tango Lesson";
13. SELECT DISTINCT viewers.first, viewers.last, viewers.email FROM viewers 
INNER JOIN viewings
ON viewings.viewer_id = viewers.viewer_id
INNER JOIN movies
ON movies.movie_id = viewings.movie_id
INNER JOIN directors
ON directors.director_id = movies.director_id
WHERE directors.last = "Kurosawa";



--------------------------------------------
STUDIO WALKTHROUGH FLICKLIST 6
--------------------------------------------
git checkout walkthrough6
git checkout walkthrough6a
git diff walkthrough6 walkthrough6a

python
from main import db, Movie

(db.drop_all() if necessary)

db.create_all()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flicklist:flicklist@localhost:8889/flicklist'

<!-- TODO 0: Refactor Current Code to use movie objects in edit form html -->
main.py(line 36)
    return Movie.query.filter_by(watched = False).all()

(Check where this is used)

edit.html(lines 10, 11)
    movie -> movie.name
    movie -> movie.id
    
(We will deal with crossoff later)

    
main.py(line 41)
    return Movie.query.filter_by(watched = True).all()

(Check where this is used)

(You will deal with this in the studio)


<!-- TODO 1: Adding Movies -->

main.py (delete line 101)
    new_movie = Movie(new_movie)
    db.session.add(new_movie)
    db.session.commit()

add-confirmation.html (line 5)
    movie becomes  movie.name


<!-- TODO 2: Crossing-off Movies -->
main.py(lines 69-83)
    crossed_off_movie = Movie.query.filter_by(id = crossed_off_movie_id).first()
    
    if crossed_off_movie == None:
        ....

    crossed_off_movie.watched = True
    db.session.add(crossed_off_movie)
    db.session.commit()

crossoff.html(line 4)
    crossed_off_movie -> crossed_off_movie.name

<!-- TODO 3: Ratings -->

First of all! We need to add a rating to our class! Think about how you might do this. Good luck!
