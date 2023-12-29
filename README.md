# DCSA (Darija Comments Sentiment Analysis)

## Overview

DCSA (Darija Comments Sentiment Analysis) is a project that focuses on sentiment analysis of comments written in Darija, using machine learning and deep learning techniques. Darija is a variety of Arabic spoken in the Maghreb region, written in Arabic script. The project involves data gathering from multiple sources, data cleaning, transformation, and the development of various models for sentiment analysis.

## Dataset

The dataset used in this project consists of 12,000 rows of comments from diverse domains, including sports, religion, economy, politics, and more. The data preprocessing pipeline involves normalization, stemming, removing stop words, and transforming emojis into words, all while keeping the Darija text intact.

## Models

Different machine learning and deep learning models were experimented with, and the DistilBERT uncased model was fine-tuned on various hyperparameters. The selection of the best metrics for each model was a crucial step in determining the optimal sentiment analysis model.

## Flask App

The project includes a Flask web application that provides a live demo of the sentiment analysis model. The app features a section where users can input an Hespress article, and it scrapes comments, classifying each one as either positive or negative. Additionally, an API is provided for users to integrate the sentiment analysis functionality into their applications.

The web app has been deployed using Render, making it accessible for users to experience the sentiment analysis in real-time.

## MLOPS Integration

In the MLOPS (Machine Learning Operations) phase, every comment is stored in MongoDB along with the model's prediction. An external language model (LLM) from Hugging Face is used in conjunction with the trained model, and the results are combined to assign a sentiment score. The comment is then labeled with a resultant score, utilizing a weighted approach (0.7 for the LLM and 0.3 for the custom model). The model is retrained periodically to adapt to evolving patterns in sentiment expression.

## Deployment

The DCSA project is live at [lfahim.tech](https://lfahim.tech), providing users with a practical and interactive way to analyze sentiment in Darija comments.

## How to Use

To utilize the sentiment analysis functionality, you can visit the web app at [lfahim.tech](https://lfahim.tech) for the live demo. Additionally, the API endpoint is available for integration into your own applications.

## Acknowledgments

Special thanks to the contributors and open-source community for their support and collaboration on this project.

Feel free to explore, contribute, and use DCSA for your sentiment analysis needs!