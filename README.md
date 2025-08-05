# Book Recommender — Project 3 (Group 53)

A personalized book recommendation system that helps users discover new reads based on their favorite authors, genres, and books. Built with a Python backend (Flask) and an interactive HTML/CSS/JavaScript frontend.

---

## Project Summary

- **Team Name:** Group 53  
- **Team Members:**
  - Kamafo Neizer-Ashun (@kamafo)
  - Benjamin Nguyen (@benjamin-username)
  - Polina Antonenko (@polina-username)

- **Course:** COP3530  
- **Semester:** Summer C 2025  

---

## Features

- Dynamic search for favorite authors, genres, and books
- Book rating system (1–5 stars)
- Algorithm toggle to support future recommendation models
- Real-time book recommendations using content-based filtering
- Responsive and visually engaging UI

---

## Dataset

**Source:** [Goodreads 100k Books Dataset on Kaggle](https://www.kaggle.com/datasets/mdhamani/goodreads-books-100k)

This file (`books.csv`) is too large to include in the repository. To run the project locally, follow these steps:

See [`DATASET_SETUP.md`](./DATASET_SETUP.md) for instructions on how to download and place the dataset in your project directory.

---

## Tools & Technologies

- **Backend:** Python 3.11, Flask
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Libraries:** pandas, textdistance, Jinja2
- **Version Control:** Git & GitHub

---

## File Structure

Book-Recommender---Project-3-Group-53/
│
├── app.py # Flask web server
├── recommender_logic.py # Cleaned logic to recommend books
├── alg1.py # Polina's original algorithm
├── books.csv # Not pushed to GitHub (see dataset instructions)
│
├── templates/
│ └── index.html # Main web UI
│
├── static/
│ ├── style.css # Styling
│ └── autocomplete.js # Search & rating logic
│
├── .gitignore
├── README.md # ← You are here
└── DATASET_SETUP.md # Dataset instructions

yaml
Copy
Edit

---

## Instructions for Running the App

### 1. Clone the repo
```bash
git clone https://github.com/kamafo/Book-Recommender---Project-3-Group-53.git
cd Book-Recommender---Project-3-Group-53
2. Set up Python virtual environment
bash
Copy
Edit
python -m venv env
env\Scripts\activate  # On Windows
3. Install dependencies
bash
Copy
Edit
pip install flask pandas
4. Place books.csv
Follow DATASET_SETUP.md to get the dataset in the correct location.

5. Run the Flask app
bash
Copy
Edit
python app.py
Then go to:
📡 http://127.0.0.1:5000/

git push origin main

