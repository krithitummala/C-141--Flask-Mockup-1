from flask import Flask,jsonify,request
import csv

all_movies = []

with open("movies.csv",encoding='utf8') as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)
    all_movies = data[1:]


liked_movies = []
disliked_movies = []
not_watched = []

app=Flask(__name__)

@app.route("/get-content")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status" : 'success'
    })

@app.route("/liked-content",methods = ["POST"] )
def liked_movie() : 
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status" : 'success'
    })
  
@app.route("/disliked-content",methods = ["POST"] )
def liked_movie() : 
    movie = all_movies[0]
    all_movies = all_movies[1:]
    disliked_movies.append(movie)
    return jsonify({
        "status" : 'success'
    })

if __name__ == "__main__":
    app.run()