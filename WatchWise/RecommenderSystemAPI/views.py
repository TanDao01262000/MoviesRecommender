from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def recommended_movies(request):
    pass


@api_view(['GET'])
def input_recommended_movies(request):
    pass


""" from lightfm import LightFM
from lightfm.datasets import fetch_movielens
import numpy as np

def recommend_movies(user_input):
    # Specify the version of MovieLens dataset
    dataset_version = '20m'

    # Load MovieLens data
    data = fetch_movielens(version=dataset_version)

    # Create a LightFM model
    model = LightFM(loss='warp')  # You can experiment with different loss functions

    # Train the model
    model.fit(data['train'], epochs=30, num_threads=2)

    # Extract genre information for all movies
    all_genres = data['item_genres']

    # Identify movies with genres related to the user input
    related_movies = []
    for movie_id, genres in enumerate(all_genres):
        if any(keyword.lower() in user_input.lower() for keyword in genres):
            related_movies.append(movie_id)

    if not related_movies:
        return "No movies found based on the input."

    # Generate recommendations based on related genres
    scores = model.predict(0, np.array(related_movies))

    # Sort recommendations in descending order
    top_movie_ids = np.argsort(-scores)

    # Recommend top 10 movies related to the user input
    recommended_movies = [data['item_labels'][movie_id] for movie_id in top_movie_ids[:10]]

    return recommended_movies

# Example usage:
user_input = "I wanna watch a thriller with mystery"
recommendations = recommend_movies(user_input)
print("Recommended movies:", recommendations)
 """
