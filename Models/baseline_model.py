import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, f1_score
import matplotlib.pyplot as plt
import seaborn as sns

class ProvenBaselines:
    """
    Based on Leiva-Bianchi et al. (2025) meta-analysis:
    - SVM: Best F1-score (0.79) and robust performance
    - MLP: Highest accuracy (92%) in grooming detection
    """
    
    def __init__(self):
        self.svm_model = SVC(kernel='linear', probability=True, random_state=42)
        self.mlp_model = MLPClassifier(hidden_layer_sizes=(100,), random_state=42, max_iter=1000)
    
    def train_svm(self, X_train, y_train):
        """SVM baseline - proven robust performer in grooming detection"""
        self.svm_model.fit(X_train, y_train)
        return self.svm_model
    
    def train_mlp(self, X_train, y_train):
        """MLP baseline - highest accuracy in literature"""
        self.mlp_model.fit(X_train, y_train)
        return self.mlp_model

class SafetyMonitor:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=1000, stop_words='english', ngram_range=(1, 2))
        self.model = LogisticRegression(random_state=42, max_iter=1000)
        self.is_trained = False
    
    def load_data(self):
        df = pd.read_csv('data/synthetic_chats.csv')
        return df['text'], df['label']
    
    def prepare_data(self):
        X, y = self.load_data()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
        X_train_vec = self.vectorizer.fit_transform(X_train)
        X_test_vec = self.vectorizer.transform(X_test)
        return X_train_vec, X_test_vec, y_train, y_test
    
    def train(self):
        print("🔄 Training Safety Monitor with Research Baselines...")
        X_train_vec, X_test_vec, y_train, y_test = self.prepare_data()
        
        # Train main model
        self.model.fit(X_train_vec, y_train)
        self.accuracy = self.model.score(X_test_vec, y_test)
        
        # Compare with research baselines
        self.compare_with_proven_baselines(X_test_vec, y_test, X_train_vec, y_train)
        
        self.is_trained = True
        return self.accuracy
    
    def compare_with_proven_baselines(self, X_test, y_test, X_train, y_train):
        """
        Compare my model against literature-proven baselines
        """
        print("\n📊 COMPARISON WITH PROVEN BASELINES FROM LITERATURE")
        print("=" * 60)
        
        baselines = ProvenBaselines()
        
        # Train and test SVM (literature's best F1-score)
        svm_model = baselines.train_svm(X_train, y_train)
        svm_accuracy = svm_model.score(X_test, y_test)
        svm_pred = svm_model.predict(X_test)
        svm_f1 = f1_score(y_test, svm_pred)
        
        # Train and test MLP (literature's best accuracy)  
        mlp_model = baselines.train_mlp(X_train, y_train)
        mlp_accuracy = mlp_model.score(X_test, y_test)
        mlp_pred = mlp_model.predict(X_test)
        mlp_f1 = f1_score(y_test, mlp_pred)
        
        # Our model's F1 score
        our_pred = self.model.predict(X_test)
        our_f1 = f1_score(y_test, our_pred)
        
        print(f"🤖 Our Model:      Accuracy: {self.accuracy:.4f}, F1: {our_f1:.4f}")
        print(f"📚 SVM Baseline:   Accuracy: {svm_accuracy:.4f}, F1: {svm_f1:.4f}")
        print(f"📚 MLP Baseline:   Accuracy: {mlp_accuracy:.4f}, F1: {mlp_f1:.4f}")
        
        # Show improvement over literature baselines
        improvement_over_svm = our_f1 - svm_f1
        improvement_over_mlp = our_f1 - mlp_f1
        
        print(f"\n📈 Improvement over SVM:  {improvement_over_svm:+.4f}")
        print(f"📈 Improvement over MLP:  {improvement_over_mlp:+.4f}")

def main():
    """Main function to run the enhanced safety monitor"""
    print("🎮 Emotion-Aware Safety Monitor - Research Edition")
    print("Building on established grooming detection literature...")
    
    monitor = SafetyMonitor()
    accuracy = monitor.train()
    
    print(f"\n✅ Final Results:")
    print(f"   Our model achieved {accuracy:.4f} accuracy")
    print(f"   With comparison to research-proven baselines")

if __name__ == "__main__":
    main()