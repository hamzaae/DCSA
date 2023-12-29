# DCSA (Darija Comments Sentiment Analysis)

## Overview

DCSA (Darija Comments Sentiment Analysis) is a project that focuses on sentiment analysis of comments written in Darija, using machine learning and deep learning techniques. Darija is a variety of Arabic spoken in the Maghreb region, written in Arabic script. The project involves data gathering from multiple sources, data cleaning, transformation, and the development of various models for sentiment analysis.

## Dataset

The dataset used in this project consists of 12,000 rows of comments from diverse domains, including sports, religion, economy, politics, and more. The data preprocessing pipeline involves normalization, stemming, removing stop words, and transforming emojis into words, all while keeping the Darija text intact.

## Models

Different machine learning and deep learning models were experimented with, and the DistilBERT uncased model was fine-tuned on various hyperparameters. The selection of the best metrics for each model was a crucial step in determining the optimal sentiment analysis model.
![pipeline](https://github.com/hamzaae/DCSA/assets/122805922/7613e61e-40ab-48cb-a300-884e2eca8e81)


## Flask App

The project includes a Flask web application that provides a live demo of the sentiment analysis model. The app features a section where users can input an Hespress article, and it scrapes comments, classifying each one as either positive or negative. Additionally, an API is provided for users to integrate the sentiment analysis functionality into their applications.

The web app has been deployed using Render, making it accessible for users to experience the sentiment analysis in real-time.

## MLOPS Integration

In the MLOPS (Machine Learning Operations) phase, every comment is stored in MongoDB along with the model's prediction. An external language model (LLM) from Hugging Face is used in conjunction with the trained model, and the results are combined to assign a sentiment score. The comment is then labeled with a resultant score, utilizing a weighted approach (0.7 for the LLM and 0.3 for the custom model). The model is retrained periodically to adapt to evolving patterns in sentiment expression.

![full](https://github.com/hamzaae/DCSA/assets/122805922/80ce9063-d764-4bd3-9020-fe3dcd1d8380)



## Deployment

The DCSA project is live at [lfahim.tech](https://lfahim.tech), providing users with a practical and interactive way to analyze sentiment in Darija comments.
NB. It's available for a periode!
## How to Use

To utilize the sentiment analysis functionality, you can visit the web app at [lfahim.tech](https://lfahim.tech) for the live demo. Additionally, the API endpoint is available for integration into your own applications.

Some screenshots:
![image](https://github.com/hamzaae/DCSA/assets/122805922/110e1df0-ca59-4c93-9c47-8e210f7e7d6c)
![image](https://github.com/hamzaae/DCSA/assets/122805922/888bf76a-10ae-42cb-b844-25ad1ec5b254)
![image](https://github.com/hamzaae/DCSA/assets/122805922/713d9849-8fe5-476e-83ba-43fafa8bfe71)
![image](https://github.com/hamzaae/DCSA/assets/122805922/fdf36e91-6840-4bf4-b1c9-befffec27bd6)



## Acknowledgments

Special thanks to the contributors and open-source community for their support and collaboration on this project.

Feel free to explore, contribute, and use DCSA for your sentiment analysis needs!

