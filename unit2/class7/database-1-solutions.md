1. SELECT title FROM movies;
2. SELECT title FROM movies ORDER BY year DESC;
3. INSERT INTO directors (first, last, country) VALUES ("Jean-Pierre", "Jeunet", "France");
4. SELECT director_id FROM directors WHERE first="Jean-Pierre" AND last="Jeunet";
5. INSERT INTO movies (title, year, director_id) VALUES ("Amelie", 2001, 2);
6. SELECT * FROM directors ORDER BY country;
7. SELECT directors.country FROM movies JOIN directors ON movies.director_id = directors.director_id WHERE movies.title="Amelie";
8. SELECT movies.title, directors.first, directors.last FROM movies JOIN directors ON movies.director_id = directors.director_id ORDER BY directors.last;