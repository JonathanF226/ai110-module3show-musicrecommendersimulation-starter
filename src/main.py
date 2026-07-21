"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # A few distinct taste profiles to try.
    profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.35},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.9},
    }

    # Pick which profile to run.
    user_prefs = profiles["High-Energy Pop"]

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 44)
    print("  TOP RECOMMENDATIONS")
    print("=" * 44)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n{rank}. {song['title']}  —  {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Why:   {explanation}")

    print("\n" + "=" * 44)


if __name__ == "__main__":
    main()
