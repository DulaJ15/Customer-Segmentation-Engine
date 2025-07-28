# 👥 Customer Segmentation Engine

Uncover hidden patterns in customer behavior using clustering techniques and auto-generate customer personas to support marketing strategy.

## 🔍 Features
- Ingest transaction-level data (frequency, recency, revenue)
- Cluster customers using KMeans, DBSCAN, or GMM
- Visualize clusters with PCA / t-SNE
- Generate PDF personas per cluster (demographic + behavior)
- Streamlit app interface for interactive exploration

## 🤖 Tech Stack
- Python, Pandas, Scikit-learn
- Streamlit
- Matplotlib, Seaborn
- FPDF / ReportLab for persona generation

## 📊 Sample Input
| Customer ID | Recency | Frequency | Monetary |
|-------------|---------|-----------|----------|
| C001        | 5       | 12        | 4500     |

## 📦 Output
- Number of clusters
- Summary stats per segment
- PDF persona report with:
  - Age group
  - Spend behavior
  - Loyalty level
  - Suggested strategy
