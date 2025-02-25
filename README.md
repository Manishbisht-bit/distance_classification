# Distance-Based Classification with Experiment Tracking

This project applies distance-based classification to a dataset using Python and various tools, including OpenCV, Scikit-Learn, Docker, GitHub Actions, and Weights & Biases (WandB). The main objective is to detect faces, extract features, perform clustering, and track experiments in a fully automated and containerized workflow.

## Project Overview

This project implements distance-based classification using K-Means clustering on face images. The workflow includes:

- **Face Detection:** Using OpenCV’s Haar cascades.
- **Feature Extraction:** Extracting hue and saturation from detected faces.
- **Clustering:** Applying K-Means clustering to group faces based on their color features.
- **Experiment Tracking:** Logging results to WandB.
- **Automation & Containerization:** Running experiments using Docker and GitHub Actions.

## Findings

The project successfully detected faces, extracted features, and clustered them using K-Means. Here are the key findings:

- Detected **X faces** in `plaksha_Faculty.jpg`.
- K-Means successfully grouped faces into **2 clusters**.
- The template image was classified into **Cluster X**.
- All results were logged to Weights & Biases.

## Technical Questions & Answers

1. **What are common distance metrics used in classification?**

   - Euclidean, Manhattan, Minkowski, Cosine Similarity, Hamming Distance.
2. **What are real-world applications of distance-based classification?**

   - Face recognition, image retrieval, fraud detection, medical diagnosis, document classification.
3. **Explain various distance metrics:**

   - **Euclidean:** Straight-line distance.
   - **Manhattan:** Sum of absolute differences.
   - **Minkowski:** Generalization of Euclidean and Manhattan.
   - **Cosine Similarity:** Measures cosine of the angle between vectors.
   - **Hamming Distance:** Measures the number of differing bits.
4. **What is the role of cross-validation?**

   - Helps assess model performance by splitting the data into multiple training and validation sets.
5. **Variance vs. Bias in KNN?**

   - **Low k:** Low bias, high variance (sensitive to noise).
   - **High k:** Higher bias, lower variance (smoother classification).


![WandB Overview](https://github.com/Manishbisht-bit/distance_classification/blob/main/image/d1.png)
![WandB Overview](https://github.com/Manishbisht-bit/distance_classification/blob/main/image/d2.png)