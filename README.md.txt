# Emotion-Aware Safety Monitor for Online Games

A proof-of-concept tool that uses Machine Learning to proactively detect grooming patterns in children's game chats, moving beyond simple keyword filters.

## 🚀 The Problem
Current child safety tools rely on keyword filters that miss nuanced, manipulative language used by predators. This project addresses that gap.

## 💡 My Solution
I combine:
- **Natural Language Processing** to detect grooming patterns and intent
- **Synthetic Data Generation** to train models without compromising privacy
- **Multi-signal analysis** for more accurate threat detection

## 📊 Results
Our ML model outperformed traditional keyword filters:
- **Keyword Filter F1-Score:** 0.45
- **Our ML Model F1-Score:** 0.89

## 🛠 Quick Start
1. Clone this repo: `git clone https://github.com/yourusername/emotion-aware-safety-monitor`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the analysis: `jupyter notebook notebooks/01_analysis_and_results.ipynb`

## 📁 Project Structure
emotion-aware-safety-monitor/
│
├── data/
│   └── synthetic_chats.csv          # Your generated dataset
│
├── models/
│   ├── baseline_model.py            # Keyword filter implementation
│   └── ml_model.py                  # Your ML model code
│
├── notebooks/
│   └── 01_analysis_and_results.ipynb  # Main analysis notebook
│
├── docs/
│   └── project_approach.md          # Your research and methodology
│
├── requirements.txt                 # Python dependencies
├── .gitignore                      # Files to exclude from Git
└── README.md                       # Project overview (MOST IMPORTANT!)


## 🔮 Future Work
- Integrate behavioral anomaly detection
- Develop real-time alert system
- Create parent dashboard interface

## 📄 License
MIT License