# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

A tool that suggests songs to match your mood and taste.

---

## 2. Intended Use  

**Goal:** Given a person's taste (genre, mood, energy), suggest the top 5 songs that fit.

**Made for:** Classroom exploration, not real users.

**Should be used for:** Learning how a simple recommender turns preferences into picks.

**Should not be used for:** Real music apps, ranking artists, or any real decision. It only knows 18 songs and does not understand lyrics or how songs actually sound.

---

## 3. How the Model Works  

Each song gives points based on how well it fits you:

- Same genre: +2.0 (the biggest bonus)
- Same mood: +1.2
- Close energy: up to +0.3
- Close acousticness: up to +0.2
- Close valence (happy/sad feel): up to +0.1

We add up the points for every song and show the 5 with the highest totals.
Genre matters most, so it usually decides the winner. The other traits just break ties.

---

## 4. Data  

- **Size:** 18 songs.
- **Features:** genre, mood, energy, tempo, valence, danceability, acousticness.
- **Genres:** 15 genres, but 13 of them have only one song. Only lofi (3) and pop (2) have more.
- **Changes:** I did not add or remove any songs.
- **Limits:** Too small to be realistic, and no lyrics, language, or artist info.

---

## 5. Strengths  

- It works well for popular genres like pop and lofi, where there are enough songs to choose from.
- It correctly puts a perfect match (same genre and mood) at the top.
- The picks matched my gut: chill lofi got quiet songs, high-energy pop got upbeat ones.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The biggest weakness I found is a "genre lottery" bias from the +2.0 genre weight on a skewed catalog, where 13 of the 15 genres have only one song. Because energy, acousticness, and valence together add up to just +0.6, they can never override a genre match, so a user asking for an "acoustic metal" song still gets the loud non-acoustic one. This favors users whose taste falls in the well-stocked lofi and pop lanes, while niche-genre users are pushed toward the same high-energy filler regardless of their "energy gap."

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

**Profiles I tested:** High-Energy Pop, Chill Lofi, and Deep Intense Rock.

**What surprised me:** the same few loud songs (like "Gym Hero") kept showing up even for people who did not ask for them. That happens because once a song can't match your genre or mood, the only points left come from having similar energy. High-energy songs are close to almost everyone who wants energetic music, so they fill the leftover spots by default.

**Comparing the profiles:**
- **Pop vs. Lofi:** Pop pulls upbeat, danceable songs; Lofi pulls quiet, low-energy ones. This makes sense — the two profiles ask for opposite energy levels, so the lists barely overlap.
- **Pop vs. Rock:** Both want high energy, so their filler songs look alike (the same loud tracks), but each still puts its own genre first. The top pick differs, the bottom of the list looks similar.
- **Lofi vs. Rock:** These are the most different. Lofi wants calm and quiet, Rock wants loud and intense, so almost nothing is shared between them.

---

## 8. Future Work  

- Add more songs so every genre has real choices.
- Make genre less overpowering so energy and mood matter more.
- Stop showing weak filler songs when there aren't 5 good matches.

---

## 9. Personal Reflection  

I learned that a recommender is really just points and math. The surprising part was how one big rule (genre) can quietly control the whole result. It made me realize real apps can have hidden biases too, based on how they weigh things and what data they have.
