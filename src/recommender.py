import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read songs from a CSV file into a list of dicts, converting numeric fields to int/float."""
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": int(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against the user's preferences, returning (score, list of reasons)."""
    # Scoring recipe from README:
    #   +2.0  genre match (hard gate / heaviest weight)
    #   +1.2  mood match
    #   0..+0.3  energy closeness       (tie-breaker)
    #   0..+0.2  acousticness closeness (tie-breaker)
    #   0..+0.1  valence closeness      (tie-breaker)
    score = 0.0
    reasons: List[str] = []

    if user_prefs.get("genre") == song["genre"]:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if user_prefs.get("mood") == song["mood"]:
        score += 1.2
        reasons.append("mood match (+1.2)")

    if "energy" in user_prefs:
        pts = 0.3 * (1 - abs(song["energy"] - user_prefs["energy"]))
        score += pts
        reasons.append(f"energy closeness (+{pts:.2f})")

    if "acousticness" in user_prefs:
        pts = 0.2 * (1 - abs(song["acousticness"] - user_prefs["acousticness"]))
        score += pts
        reasons.append(f"acousticness closeness (+{pts:.2f})")

    if "valence" in user_prefs:
        pts = 0.1 * (1 - abs(song["valence"] - user_prefs["valence"]))
        score += pts
        reasons.append(f"valence closeness (+{pts:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song and return the top k as (song, score, explanation), highest first."""
    # Score every song in the catalog, then rank highest-first.
    scored = [
        (song, *score_song(user_prefs, song))  # (song, score, reasons)
        for song in songs
    ]
    scored.sort(key=lambda item: item[1], reverse=True)

    # Turn the reasons list into a readable explanation string.
    return [
        (song, score, ", ".join(reasons) if reasons else "no strong match")
        for song, score, reasons in scored[:k]
    ]
