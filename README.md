Customer Segmentation using K-Means Clustering

This project focuses on segmenting mall customers into meaningful groups using the K-Means clustering algorithm. The goal is to understand customer behavior based on income and spending patterns so that businesses can make better marketing and business decisions.

+ Project Structure

customer_segmentation.py → Main Python script

Mall_Customers.csv → Input dataset

customer_clusters.csv → Output file with cluster labels

README.md → Project documentation

+ About the Dataset

The dataset used in this project is Mall_Customers.csv. It contains customer details such as:

CustomerID

Gender

Age

Annual Income (k$)

Spending Score (1–100)

For clustering, the following two features are used:

Annual Income (k$)

Spending Score (1–100)

+ What This Project Does

Loads the customer dataset

Visualizes customer distribution

Uses the Elbow Method to find the best number of clusters

Applies K-Means clustering

Visualizes the segmented customer groups

Saves the final clustered data to a CSV file

+ Tools and Libraries

Python

Pandas

Matplotlib

Seaborn

Scikit-learn

+ How to Run the Project

Install required libraries:

pip install pandas matplotlib seaborn scikit-learn


Run the script:

python customer_segmentation.py


The program will:

Display scatter plots

Show the Elbow Method graph

Visualize customer clusters

Save the output as customer_clusters.csv

+ Output

Cluster visualization plots

A new file called customer_clusters.csv

An extra column named Cluster in the dataset

+ Use Case

This project can help:

Identify high-value customers

Understand spending behavior

Improve marketing and sales strategies
