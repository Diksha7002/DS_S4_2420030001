#1. Euclidean Distance
import numpy as np
from scipy.spatial import distance

pointA = np.array([2, 4, 6])
pointB = np.array([5, 1, 9])

# Euclidean Distance
euclidean_dist = distance.euclidean(pointA, pointB)
print("Euclidean Distance:", euclidean_dist)

# Similarity (inverse of distance)
similarity_euclidean = 1 / (1 + euclidean_dist)
print("Euclidean Similarity:", similarity_euclidean)

#2.Manhattan Distance
import numpy as np
from scipy.spatial import distance

pointA = np.array([2, 4, 6])
pointB = np.array([5, 1, 9])

#Manhattan Distance
manhattan_dist = distance.cityblock(pointA, pointB)
print("Manhattan Distance:", manhattan_dist)

# Similarity (inverse of distance)
similarity_manhattan = 1 / (1 + manhattan_dist)
print("Manhattan Similarity:", similarity_manhattan)

#3. Minkowski Distance
import numpy as np
from scipy.spatial import distance

pointA = np.array([2, 4, 6])
pointB = np.array([5, 1, 9])

# Minkowski Distance with p=3
minkowski_dist_p3 = distance.minkowski(pointA, pointB, p=3)
print("Minkowski Distance (p=3):", minkowski_dist_p3)

# Similarity (inverse of distance)
similarity_minkowski = 1 / (1 + minkowski_dist_p3)
print("Minkowski Similarity (p=3):", similarity_minkowski)

#4.Pearson Correlation
# Example dataset
import pandas as pd
df = pd.DataFrame({
    'X': [10, 20, 30, 40, 50],
    'Y': [12, 24, 33, 45, 60]   })

# Pearson correlation matrix
corr_matrix = df.corr(method='pearson')
print("Pearson Correlation Matrix:\n", corr_matrix)

#for Dataset:
#print("\n Pearson Correlation Dataset:\n")
#df = pd.read_csv("pearson_correlation_dataset.csv")
#print(df.corr(method='pearson'))

#5.Spearman Correlation
import pandas as pd
from scipy.stats import spearmanr

# Example dataset
df = pd.DataFrame({
    'X': [10, 20, 30, 40, 50],
    'Y': [12, 18, 33, 47, 55]
})

# Spearman correlation coefficient and p-value
corr_value, p_value = spearmanr(df['X'], df['Y'])
print(f"Spearman Correlation Coefficient: {corr_value}")
print(f"P-value: {p_value}")

#for dataset:
#print("\n spearman Correlation Dataset:\n")
#df = pd.read_csv("pearson_correlation_dataset.csv")
#print(df.corr(method='spearman'))

#6.Hamming Distance
def hamming_distance(str1, str2):
    # Ensure strings are of equal length
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")
    
    # Count differing positions
    return sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))

# Example usage
s1 = "karolin"
s2 = "kathrin"

dist = hamming_distance(s1, s2)
print(f"Hamming Distance between '{s1}' and '{s2}': {dist}")

#7.Jaccard Index
def jaccard_index(str1, str2):
    set1, set2 = set(str1.split()), set(str2.split())
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)

# Example usage
s1 = "data science is fun"
s2 = "science makes data useful"

print("Jaccard Index:", jaccard_index(s1, s2))

#8.Cosine Similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Example sentences
s1 = "data science is fun"
s2 = "science makes data useful"
# Convert text to vector representation
vectorizer = CountVectorizer().fit([s1, s2])
vectors = vectorizer.transform([s1, s2])
# Compute cosine similarity
cos_sim = cosine_similarity(vectors[0], vectors[1])[0][0]
print("Cosine Similarity:", cos_sim)

#9.Sequence Based Measures
def lcs_length(X, Y):
    m, n = len(X), len(Y)
    # Create a matrix to store lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # Build the matrix
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[m][n]
# Example usage
seq1 = "ABCDEF"
seq2 = "AEBDF"
length = lcs_length(seq1, seq2)
print(f"Longest Common Subsequence length between '{seq1}' and '{seq2}': {length}")

