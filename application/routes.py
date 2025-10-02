from flask import render_template
import random
from application import app
from application.connector import Connector


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/welcome/<string:name>')
def welcome(name='Team'):
    return render_template('welcome.html', title="Welcome", name=name.title(), group='Everyone')


@app.route('/joke')
def joke():
    ca  = Connector()
    joke = ca.extract_joke()
    num_of_jokes = ca.extract_num_of_jokes()
    return render_template('joke.html', title="Joke Time", joke_question=joke[0], joke_answer=joke[1], number_of_jokes=num_of_jokes)


joke_dict = {0: ["Why was Cinderella so bad a football?", "She kept running away from the ball!"],
             1: ["What do you call a pile of cats?", "A meow-ntain"],
             2: ["Why did the bicycle fall over?", "Because it was two tired"],
             3: ["What do you call a sad strawberry?", "A blueberry!"],
             4: ["How do you organise a space party?", "You planet."],
             5: ["What do cows read the most?", "Cattle-logs."],
             6: ["What do clouds wear under their shorts?", "Thunder pants!"],
             7: ["What did 0 say to 8?", "Nice belt."],
             8: ["What did the drummer name her twin daughters?", "Anna 1, Anna 2."],
             9: ["How does the moon cut his hair?", "Eclipse it."],
             10: ["Why did the scarecrow win an award?", "Because he was outstanding in his field."],
             11: ["What’s brown and sticky?", "A stick."],
             12: ["What do you call a sad cup of coffee?", "Depresso."],
             13: ["Why didn't the melons get married?", "Because they cantaloupe."],
             14: ["What goes up and down but doesn’t move?", "Stairs."],
             15: ["What do you get when you cross a fish and an elephant?", "Swimming trunks."],
             16: ["Why can’t a nose be 12 inches long?", "Because then it would be a foot."],
             17: ["What do you call a magician that loses his magic?", "Ian."],
             18: ["How do rabbits travel?", "By hareplanes."],
             19: ["What do you call a sleeping dinosaur?", "A dino-snore."],
             20: ["Why did the strawberry cry?", "He found himself in a jam."]
             }

       
@app.route('/hello')
def hello():
    return render_template('hello.html', title='Hello')