# ⚽ Football Analytics Engine

A probabilistic football forecasting engine built using Python, Poisson Distribution, and Monte Carlo Simulation.

This project predicts:
- Match outcomes
- Expected goals
- League winner probabilities
- Scoreline probabilities
- Future competition simulations

---

# 🚀 Features

## ✅ Current Features

- Historical football data preprocessing
- Multi-season dataset merging
- Exploratory Data Analysis (EDA)
- Team attack & defense strength calculation
- Home/Away performance modeling
- Poisson-based expected goals prediction
- Match win/draw/loss probability prediction

---

# 🧠 Statistical Models Used

## Poisson Distribution
Used to model football score probabilities based on expected goals.

## Monte Carlo Simulation *(In Progress)*
Will simulate thousands of league seasons to estimate:
- League winners
- Top 4 probabilities
- Relegation probabilities

---

# 📊 Current Dataset

Currently includes:
- English Premier League (1993–2025)

Future expansion:
- La Liga
- Bundesliga
- Serie A
- Ligue 1
- UEFA Champions League
- UEFA Europa League
- FIFA World Cup
- Domestic Cups

---

# 🏗 Project Structure

```bash
Football Analytics/
│
├── Data/
│   ├── Raw/
│   └── Processed/
│
├── Src/
│   ├── Data/
│   │   ├── merge.py
│   │   ├── preprocess.py
│   │   └── eda.py
│   │
│   ├── Models/
│   │   ├── poisson.py
│   │   └── predict_match.py
│   │
│   └── Simulations/
│
├── Notebooks/
│
├── venv/
│
├── .gitignore
└── README.md
```

---

# ⚙️ Tech Stack

- Python
- Pandas
- NumPy
- SciPy
- Git & GitHub

Planned:
- Node.js + Express
- React Dashboard
- REST APIs
- Docker Deployment

---

# 📈 Example Prediction

Example:
- Arsenal vs Chelsea

Output:
```python
Expected Arsenal Goals: 1.54
Expected Chelsea Goals: 1.10

Arsenal Win: 46.9%
Draw: 25.4%
Chelsea Win: 27.0%
```

---

# 🔥 Future Roadmap

- Scoreline probability matrix
- Monte Carlo season simulation
- League table forecasting
- Multi-league support
- European competition simulation
- REST API integration
- Interactive dashboard
- Automated data pipelines

---

# ▶️ Installation

Clone the repository:

```bash
git clone <your-repo-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run prediction engine:

```bash
python Src/Models/predict_match.py
```

---

# 📌 Status

🚧 Active Development

Currently building:
- Score simulation engine
- Monte Carlo forecasting system

---

# 👨‍💻 Author

Shridhar A