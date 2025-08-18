# Comparação de Métricas de Classificação em IA
# Exemplo corrigido com Random Forest e Breast Cancer Dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, roc_curve
)

# ----------------------------
# 1. Carregar o dataset
# ----------------------------
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name="target")  # 0 = maligno, 1 = benigno

# ----------------------------
# 2. Dividir em treino e teste (70/30)
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# ----------------------------
# 3. Treinar o modelo Random Forest
# ----------------------------
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# ----------------------------
# 4. Predições e probabilidades
# ----------------------------
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]  # probabilidade da classe positiva (1 = benigno)

# ----------------------------
# 5. Cálculo das métricas (classe positiva = 1 = benigno)
# ----------------------------
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label=1)
recall = recall_score(y_test, y_pred, pos_label=1)
f1 = f1_score(y_test, y_pred, pos_label=1)
auc = roc_auc_score(y_test, y_proba)

results = pd.DataFrame({
    "Métrica": ["Acurácia", "Precisão (classe 1=benigno)", 
                "Recall (classe 1=benigno)", 
                "F1-Score (classe 1=benigno)", 
                "AUC-ROC"],
    "Valor": [accuracy, precision, recall, f1, auc]
}).round(4)

print("\nDesempenho do Modelo Random Forest:")
print(results.to_string(index=False))

# ----------------------------
# 6. Matriz de confusão (ordem fixa de classes [0,1])
# ----------------------------
cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
classes = ["maligno (0)", "benigno (1)"]

plt.figure(figsize=(5, 4))
plt.imshow(cm, cmap="Blues")
plt.title("Matriz de Confusão - Random Forest")
plt.xlabel("Previsto")
plt.ylabel("Real")
plt.xticks([0, 1], classes, rotation=15)
plt.yticks([0, 1], classes)

# Anotações dos valores em cada célula
thresh = cm.max() / 2.0
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, format(cm[i, j], "d"),
                 ha="center", va="center",
                 color="white" if cm[i, j] > thresh else "black")

plt.colorbar(fraction=0.046, pad=0.04)
plt.tight_layout()
plt.show()

# ----------------------------
# 7. Curva ROC
# ----------------------------
fpr, tpr, thresholds = roc_curve(y_test, y_proba)

plt.figure(figsize=(6, 5))
plt.plot(fpr, tpr, label=f"AUC = {auc:.3f}")
plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
plt.xlabel("Taxa de Falsos Positivos (FPR)")
plt.ylabel("Taxa de Verdadeiros Positivos (TPR)")
plt.title("Curva ROC - Random Forest (classe positiva = 1 = benigno)")
plt.legend(loc="lower right")
plt.tight_layout()
plt.show()
gi

