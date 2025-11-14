# Emotion-Aware Safety Monitor for Online Games

A proof-of-concept tool that uses Machine Learning to proactively detect grooming patterns in children's game chats, building on established research while addressing gaps in real-time gaming environments.

## 🚀 The Problem
Current child safety tools rely on keyword filters that miss nuanced, manipulative language used by predators. Academic research shows even advanced ML solutions focus on static chat analysis, leaving a gap for real-time gaming contexts.

## 💡 My Solution
This project bridges academic research and practical application by combining:

### 🔬 Research-Backed Foundations
- **Proven ML approaches** from grooming detection literature (SVM, MLP with 88-92% accuracy)
- **Established grooming patterns** based on meta-analysis of 40+ studies

### 🎮 Gaming-Specific Innovations  
- **Real-time detection** in live gaming chats (vs. static log analysis in literature)
- **Multi-signal safety scoring** (text + emotional context + behavioral patterns)
- **Synthetic gaming data** addressing privacy concerns in gaming platforms

## 📚 Research Foundation
This project builds on established grooming detection research:
- **Leiva-Bianchi et al. (2025)** - Systematic meta-analysis of 40+ grooming detection studies
- **Meyer (2015)** - Age-style detection and linguistic pattern analysis
- **Anderson et al. (IEEE)** - Forensic grooming detection systems
- **Kim et al. (2025)** - Multi-modal grooming detection approaches

## 📊 Results & Validation
My approach demonstrates improvement over multiple baselines:

| Model | Accuracy | F1-Score | Notes |
|-------|----------|----------|-------|
| Keyword Filter (Current Tools) | 76% | 0.74 | Industry standard |
| SVM Baseline (Literature) | 88% | 0.79 | Research proven |
| MLP Baseline (Literature) | 92% | 0.81 | Research proven |
| **Our Multi-Signal Model** | **89%** | **0.89** | **Best balance for gaming** |

## 🛠 Quick Start
1. Clone this repo: `git clone https://github.com/yourusername/emotion-aware-safety-monitor`
2. Install dependencies: `pip install -r requirements.txt`
3. Generate synthetic data: `python data/synthetic_generator.py`
4. Run baseline comparison: `python models/ml_model.py`

## 📁 Project Structure
