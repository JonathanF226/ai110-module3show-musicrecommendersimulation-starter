# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

The features that each song uses in my system will be genre, valence, energy, acousticness, and mood. UserProfile will store a preferred value for each of the features. 
The flow will be input user preferences with data on genre, mood, energy, valance, and acousticness. The process will load songs and scor them. The output will sort the songs and return recommendations.
The algorithm recipe is:
score = 2.0 * (song.genre == target.genre)                   # +2.0  genre match  (hard gate)
      + 1.2 * (song.mood  == target.mood)                    # +1.2  mood match   (vibe)
      + 0.3 * (1 - abs(song.energy       - target.energy))         # 0 to +0.3  tie-breaker
      + 0.2 * (1 - abs(song.acousticness - target.acousticness))   # 0 to +0.2  tie-breaker
      + 0.1 * (1 - abs(song.valence      - target.valence))        # 0 to +0.1  tie-breaker
This is biased towards genres because of the wieght. 



---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

User profile: genre=pop, mood=happy, energy=0.8

```
Loaded songs: 18

============================================
  TOP RECOMMENDATIONS
============================================

1. Sunrise City  —  Neon Echo
   Score: 3.49
   Why:   genre match (+2.0), mood match (+1.2), energy closeness (+0.29)

2. Gym Hero  —  Max Pulse
   Score: 2.26
   Why:   genre match (+2.0), energy closeness (+0.26)

3. Rooftop Lights  —  Indigo Parade
   Score: 1.49
   Why:   mood match (+1.2), energy closeness (+0.29)

4. Concrete Pulse  —  Grey District
   Score: 0.30
   Why:   energy closeness (+0.30)

5. Night Drive Loop  —  Neon Echo
   Score: 0.28
   Why:   energy closeness (+0.28)

============================================
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



