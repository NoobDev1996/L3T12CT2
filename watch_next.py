from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine

def read_movie_descriptions():
    # Read the movie descriptions from the 'movies.txt'
    with open('movies.txt', 'r') as file:
        movie_descriptions = file.readlines()
    return movie_descriptions

def find_most_similar_movie(description):
    movie_descriptions = read_movie_descriptions()
    # Load the SentenceTransformer model for encoding
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    # Encode the input description
    description_embedding = model.encode([description])[0]
    # Encode all the movie descriptions
    movie_embeddings = model.encode(movie_descriptions)
    # Calculate the similarity scores between the input description and all movie descriptions
    similarity_scores = [1 - cosine(description_embedding, movie_embedding) for movie_embedding in movie_embeddings]
    # Find the index of the movie with the highest similarity score
    most_similar_index = similarity_scores.index(max(similarity_scores))
    # Extract the title of the most similar movie
    most_similar_movie = movie_descriptions[most_similar_index].split(':')[0].strip()

    return most_similar_movie

if __name__ == '__main__':
    # Example description for testing
    description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

    # Find the most similar movie based on the description
    most_similar_movie = find_most_similar_movie(description)

    # Print the title of the most similar movie
    print(f"The most similar movie is: {most_similar_movie}")
