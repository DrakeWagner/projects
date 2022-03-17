# msds-projects 

### *databricks_pyspark_examples (folder)*
This folder contains several different projects I performed through Spark and databricks. Topics cover machine learning, delta lakes and lake houses, graphx, clustering analyses, model training and testing, recommender system analysis, and classification.

### *Disaster Relief Project*
(disaster_relief_proj.Rmd)<p>
 
The goal of this project was to use various classification methods to solve a real historical data-mining problem: locating displaced persons living in makeshift shelters following the destruction of the earthquake in Haiti in 2010. Following the earthquake, rescue workers, mostly from the United States military, needed to get food and water to the displaced persons. But with destroyed communications, impassable roads, and thousands of square miles, actually locating the people who needed help was challenging. As part of the rescue effort, a team from the Rochester Institute of Technology were flying an aircraft to collect high resolution geo-referenced imagery. It was known that the people whose homes had been destroyed by the earthquake were creating temporary shelters using blue tarps, and these blue tarps would be good indicators of where the displaced persons were. However, this situation was obviously time-sensitive, and there was no way that the thousands of images collected every day would be able to get thoroughly searched by aid workers for the tarps, while also communicating the locations back to rescue workers on the ground. The solution would be provided by data-mining algorithms, which could search the images faster, more scrupulously, and potentially even more accurately than humanly possible. It was crucial to find an algorithm that could effectively search the images in order to locate displaced persons and communicate the locations to rescue workers in a timely manner. <p>
By training 6 different models (GLM, LDA, QDA, KNN, PLR, RF), I was able to conclude via cross validation that KNN (k=6) was the most efficient and accurate model for detecting displaced persons, given the circumstances of the situation.
 
### *Spotify Artist Analysis*
(spotify_proj -> spotify.ipynb) <p>
As a huge music person, I decided to create an customizable analysis of artists of Spotify, using the company's API. This script showcases the ability to input any artist via their Spotify share link to learn more about their style of music, such as their sounds, album lengths, largest correlations in sound statistics, etc. The data is then either graphed or presented in a dataframe. I'm very happy with how this turned out, especially since it is able to work with any artist available on Spotify.

 
### *Natural Language Processing Project*
(nlp.proj -> sentiment_analysis.ipynb) <p>
The goal of this project was to create a digital critical edition of a corpus to support exploration of various contents of the text, such as language used, social events, cultural categories, sentiments, indentity, taste, etc. There were several steps I did to achieve this. First, I converted my collection of long-form text from their original formats into a set of tables that conformed to the Standard Text Analytic Data Model, and to the Machine Learning Corpus Format (two ETA standard designs). Next I annotated the tables with statistical and linguistic features using NLP libraries such as NLTK. Next, I created a vector representation of the corpus to generate TFIDF values to add to the Token and Vocab tables. I then extended the annotated and vectorized model with tables and features derived from the application of various unsupervised methods, including PCA, LDA, and word2vec. I expored the results using statistical and visualization methods, and finally made several conclusions about cultural patterns observed in the corpus. <p>
 

### *NBA Game Outcome Simulator*
(pyspark_proj.zip)<p>

The creation of this project was done through PySpark, a Python API for Apache Spark. Various steps included data preprocessing, data splitting/sampling, exploratory data analyisis, model construction of several models, and model evaluation. Specifically, we used a benchmark model (our baseline regression model) and a more sophisticated (champion) model. Due to the nature of the data some extra steps were needed in creating the model, such as dummy variable construction, feature scaling, handling missing values/outliers, handling semi-structured and unstructured data, and performing dimensionality reduction via PCA. Data splitting and K-fold cross validation of hyperparameters were also utilized. In evaluating the model, we looked at R-squared for our single factor model, and accuracy, precision, recall, F1 score, confusion matrices, and AUROC. We also ran a sensitivity analysis, measuring the effect of changing the model inputs or parameters. Lastly, a report was written up on our findings. <p>
We were able to use our model to predict the winning team 87.2% of the time.
 
 
### *Middle School Analysis*
(r_middle_school_analysis)<p>
A data analysis project using Spark. The goal of this project was to illustrate the effectiveness of an assessment system implemented within two different school systems. This study answered questions about the relationship between the schools' program effectiveness, whether there were any significant correlations with success rate within the program, and predictions about the futures of the program at each school. Findings are discussed in my analysis write-up.
 

### *SQL Mini Project*
(sql_db_mini_proj.ipynb, sql_local_queries_examples.ipynb)<p>
A small class project that includes the creation of a small database for the domain, adding an ER diagram and schema, populating the tables using python, and finally testing several self-created queries. The second file listed above includes several addition examples of SQL queries.
 



