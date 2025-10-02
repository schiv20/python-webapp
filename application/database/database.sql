Terminal close -- exit!
jokeapp;

CREATE DATABASE jokeapp;
USE jokeapp;

create table user (
	ID int primary key auto_increment,
	Email varchar(100) not null,
	Password varchar(100) not null
);

create table joke (
	ID int primary key auto_increment,
    the_joke varchar(2000) not null,
    punchline varchar(5000) not null
);

INSERT INTO joke (the_joke, punchline) VALUES
('Why was Cinderella so bad a football?', 'She kept running away from the ball!'),
('What do you call a pile of cats?', 'A meow-ntain'),
('Why did the bicycle fall over?', 'Because it was two tired'),
('What do you call a sad strawberry?', 'A blueberry!'),
('How do you organise a space party?', 'You planet.'),
('What do cows read the most?', 'Cattle-logs.'),
('What do clouds wear under their shorts?', 'Thunder pants!'),
('What did 0 say to 8?', 'Nice belt.'),
('What did the drummer name her twin daughters?', 'Anna 1, Anna 2.'),
('How does the moon cut his hair?', 'Eclipse it.'),
('Why did the scarecrow win an award?', 'Because he was outstanding in his field.'),
('What’s brown and sticky?', 'A stick.'),
('What do you call a sad cup of coffee?', 'Depresso.'),
('Why didn''t the melons get married?', 'Because they cantaloupe.'),
('What goes up and down but doesn’t move?', 'Stairs.'),
('What do you get when you cross a fish and an elephant?', 'Swimming trunks.'),
('Why can’t a nose be 12 inches long?', 'Because then it would be a foot.'),
('What do you call a magician that loses his magic?', 'Ian.'),
('How do rabbits travel?', 'By hareplanes.'),
('What do you call a sleeping dinosaur?', 'A dino-snore.'),
('Why did the strawberry cry?', 'He found himself in a jam.');
