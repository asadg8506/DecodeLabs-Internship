movies = {
    "action": ["John Wick", "Mad Max", "Avengers"],
    "comedy": ["The Mask", "Superbad", "Mr. Bean"],
    "horror": ["Conjuring", "Insidious", "Annabelle"],
    "sci-fi": ["Interstellar", "Inception", "Matrix"],
    "drama": ["Forrest Gump", "Joker", "Fight Club"]
}

print("=== Movie Recommendation System ===")

genre = input("Enter your favorite genre: ").lower()

if genre in movies:
    print("\nRecommended Movies:")
    
    for movie in movies[genre]:
        print("-", movie)

else:
    print("Sorry, genre not found.")