# byjus-capstones
A collection of my capstone projects from BYJU's FutureSchool.

### Table of Contents
> * [Rock Paper Scissors](https://github.com/rina-reimer/byjus-capstones/edit/main/README.md#rock-paper-scissors-august-2020)
> * [Sieve Of Eratosthenes](https://github.com/rina-reimer/byjus-capstones/edit/main/README.md#sieve-of-eratosthenes-august-2020)
> * [Gender Voices Classification](https://github.com/rina-reimer/byjus-capstones/edit/main/README.md#gender-voices-classification-november-2020)
> * [Pulsar Star Prediction](https://github.com/rina-reimer/byjus-capstones/edit/main/README.md#Pulsar-Star-Prediction-december-2020)
> * [Bengaluru House Prices](https://github.com/rina-reimer/byjus-capstones/edit/main/README.md#bengaluru-house-prices-january-2021)
> * [Guess a Word](https://github.com/rina-reimer/byjus-capstones/edit/main/README.md#guess-a-word-may-2021)
> * [Internet of Things](https://github.com/rina-reimer/byjus-capstones/edit/main/README.md#internet-of-things-august-2021)
> * [Life Expectancy Analysis](https://github.com/rina-reimer/byjus-capstones/edit/main/README.md#life-expectancy-analysis-january-2022)
> * [Payroll Calculation OOP](https://github.com/rina-reimer/byjus-capstones/edit/main/README.md#payroll-calculation-OOP-january-2022)
> * [Diamond Price Prediction](https://github.com/rina-reimer/byjus-capstones/edit/main/README.md#diamond-price-prediction-march-2022)
> * [House Price Prediction](https://github.com/rina-reimer/byjus-capstones/edit/main/README.md#House-price-prediction-june-2022)
> * [Olivetti Faces Case-Study](https://github.com/rina-reimer/byjus-capstones/edit/main/README.md#Olivetti-Faces-Case-Study-november-2022)

## [Rock Paper Scissors](rockPaperScissors.py) August 2020
### The Algorithm

In the algorithm, the computer should keep a count of player moves (i.e., the counts for 0, 1, and 2) in three separate variables - `count_rock`, `count_paper`, and `count_scissors`. The algorithm should decide the computer's move based on the following possibilities:

- If the value of the `count_rock` variable is greater than the values of the `count_paper` and `count_scissors` variables, then the computer's move should be ROCK.

- If the value of the `count_paper` variable is greater than the values of the`count_rock` and `count_scissors` variables, then the computer's move should be PAPER.

- If the value of the `count_scissors` variable is greater than the values of the `count_rock` and `count_paper` variables, then the computer's move should be SCISSORS.

- In all other cases, the computer should play ROCK, PAPER, and SCISSORS randomly.

## [Sieve Of Eratosthenes](sieveOfEratosthenes.py) August 2020
### Overview

In this project, you need to implement the Sieve of Eratosthenes algorithm in Python. This algorithm extracts only the prime numbers from a list of given natural numbers.

A prime number is a number that is divisible either by itself or by 1.

### The **Sieve of Eratosthenes** Algorithm

The Sieve of Eratosthenes is an algorithm that allows us to extract prime numbers (or primes) from a given list of natural numbers.

*An algorithm is a well-defined and well-structured set of instructions to perform a specific task*.

The Sieve of Eratosthenes algorithm finds primes up to a number, say 50, by eliminating every multiple of a prime number (starting from 2).

<img src='https://drive.google.com/uc?id=1EGqif9JT_4JExYaLUUTQA1QLZ6UpREUy' width=300>

It also assumes that every number between 2 and 50 is a prime number (even though they are actually not prime). Hence, all the multiples of a number (except the number itself) must be discarded from the list.

For example, in a list containing the natural numbers between 2 and 50, assume that

- 2 is a prime number so all of its multiples (except 2), i.e., 4, 6, 8... must be discarded

  <img src='https://drive.google.com/uc?id=1ZvPfhK0AhdFK6zF_frQ-YYsRfb_-doRe' width=300>

- 3 is a prime number so all of its multiples (except 3), i.e., 3, 6, 9... must be discarded

  <img src='https://drive.google.com/uc?id=1POSGQ8kf145SoGcAHqwcGFhscuzcOl1J' width=300>


- 4 is a prime number so all of its multiples (except 4), i.e., 8, 12, 16... must be discarded. Since every multiple of 4 is also a multiple of 2 so, they already got discarded in the first step.

  <img src='https://drive.google.com/uc?id=1POSGQ8kf145SoGcAHqwcGFhscuzcOl1J' width=300>

- 5 is a prime number so all of its multiples (except 5), i.e., 5, 10, 15... must be discarded.

  <img src='https://drive.google.com/uc?id=1GC9gaFj32sC-xAw1wKiFb7qWJ6er35xS' width=300>

This process is continued until all the **actual non-prime numbers** are discarded from the list.

## [Gender Voices Classification](genderVoicesClassification.py) November 2020
### Project Requirements

1. Create a pandas DataFrame for the train and test datasets.

2. Display the first five rows of both the training and test DataFrames.

3. Display the last five rows of both the training and test DataFrames.

4. Find the number of rows and columns in the train and test DataFrames.

5. Check for the missing values in the train and test DataFrames.

6. Count the number of `male` and `female` classes in the train DataFrame. 

7. Separate the feature variables, i.e., `x_train` and `x_test` from both the DataFrames.

8. Separate the target variable, i.e., `y_train` and `y_test` from both the DataFrames.

9. Apply the `RandomForestClassifier` machine learning model to predict the `males` and `female` classes in the test DataFrame, i.e, `x_test`.

10. Print the confusion matrix and the classification report to evaluate your prediction model. Also, based on the confusion matrix, precision, recall and f1-score values, report whether the prediction model deployed by you is making accurate predictions or not.

## [Pulsar Star Prediction](pulsarStarPrediction.py) December 2020
### Overview 

Pulsar stars are a rare type of Neutron star that produce radio emissions detectable on Earth. They are of considerable scientific interest as probes of space-time, the interstellar medium, and states of matter. As pulsars rotate, their emission beam sweeps across the sky, and when this crosses our line of sight, it produces a detectable pattern of broadband radio emission. As pulsars rotate rapidly, this pattern repeats periodically. Thus pulsar search involves looking for periodic radio signals using large radio telescopes.

Each pulsar produces a slightly different emission pattern, which varies slightly with each rotation. Thus a potential signal detection known as a 'candidate', is averaged over many rotations of the pulsar, as determined by the length of observation. In the absence of additional info, each candidate could potentially describe a real pulsar. However, in practice almost all detections are caused by Radio Frequency Interference (RFI) and noise, making legitimate signals hard to find.

Machine learning tools are now being used to automatically label pulsar candidates to facilitate rapid analysis. The classification algorithms, in particular, are being widely adopted, which treat the candidate datasets as binary classification problems (predict either `0` or `1`). Here, the legitimate pulsar examples are a minority positive class (less in numbers), and the remaining examples are a majority negative class.

The class labels used are `0` (negative class) and `1` (positive class). Hence, **we need to deploy the XGBoost Classifier classification model which can accurately detect the class 1 examples.**

### Project Requirements

1. Create a pandas DataFrame for both the train and test datasets.

2. Display the first five rows of both the training and test DataFrames.

3. Display the last five rows of both the training and test DataFrames.

4. Find the number of rows and columns in both the train and test DataFrames.

5. Check for the missing values in both the train and test DataFrames.

6. Count the number of `0` and `1` classes in the training dataset.

7. Separate the feature variables, i.e., `x_train` and `x_test` from both the DataFrames.

8. Separate the target variable, i.e., `y_train` and `y_test` from both the DataFrames.

9. Apply the `XGBClassifier` machine learning model to predict the `0` and `1` classes in the test dataset, i.e., `x_test`.

10. Print the confusion matrix and the classification report to evaluate your prediction model. Also, based on the confusion matrix, precision, recall, and f1-score values, report whether the prediction model deployed by you is making accurate predictions or not.

## [Bengaluru House Prices](bengaluruHousePrices.py) January 2021
### [Context](https://www.businesstoday.in/sectors/infra/residential-real-estate-prices-property-drop-3-per-cent-realty/story/267752.html)

A techie, residing in Mumbai, who is a data scientist got an excellent job opportunity from one of his dream companies in Bengaluru. He soon wants to shift to Bengaluru and hence, he decides to buy a home in the city.
The lack of trust in property developers in the city resulted in a drop of 7% in housing unit sales across India in 2017. Property prices in Bengaluru fell by around 5% in the second half of 2017, according to a study published by a property consultancy firm called Knight Frank. Buying a home, especially in a city like Bengaluru, is a tricky choice. While the major factors are usually the same for all metro cities, there are others to be considered for the Silicon Valley of India. Because of the millennial crowd, vibrant culture, great climate, and a slew of job opportunities in Bengaluru, it is difficult to ascertain the price of a house in the city.
As he is a data scientist he manages to find the dataset for Bengaluru house prices on the internet.

The dataset he found was vast with some useless information and some empty values. He only wants to extract some of the useful information from the dataset.

### Problem Statement

The dataset acquired by the techie is full of irregularities, incorrect values, and missing values. As a data scientist (or analyst in this context), your task is to clean the dataset given to you. 

This process of preparing data for analysis by removing or modifying data that is incorrect, incomplete, irrelevant, duplicated, or improperly formatted is known as data cleaning.

## [Guess a Word](guessAWord.py) May 2021
### Problem Statement 

In this project, you have to write a computer program to create an interactive game application called **Guess A Word**. The game must have the following major components:

1. A repository of English words, their parts of speech, and their meanings.

2. Another repository containing the player's name, the number of guesses made by them, and the time taken (in seconds) to guess the words.

3. A function to jumble the letters of the English words.

4. A timer to calculate the total time taken by a player to guess the words.

5. Display a word such that its letters are jumbled, its part of speech, and its meaning. Then prompt the player to guess the word one by one.  

6. Check whether the player has guessed the correct word.

7. Keep a count of the player's correct guesses.

### Project Requirements

1. Create the `my_words` tuple which should contain the following 10 words, their parts of speech, and their meanings as shown in the image below.

  <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project10_tuple_eg.png'>
 
2. Create an empty tuple. Call it `records`. 

3. Create the `shuffler()` function which returns a string having jumbled letters of a word.

3. Create the `count` variable to store the counts of the player's guess.

4. Create a `for` to run the game.

5. Calculate the time taken by a player (`tdelta`) to guess the words.

6. Add the records for a player in the `records` tuple.

7. Display the time taken by the player (`tdelta`) to guess the words.

8. Print all the words, their parts of speech, and their meanings in a tabular format.

9. Print all the values of the `records` tuple.

## [Internet of Things](IoTdevices.py) August 2021
### Context

The **Internet of Things (IoT)** describes the network of physical objects that are embedded with sensors, software, and other technologies to connect and exchange data with other devices and systems over the **Internet**.

IoT devices have been around for quite a while now. They are used to collect data through different kinds of sensors such as **motion sensors**, **heat sensors**, **vibration sensors**, etc.

A lot of people are using smartwatches and fitness watches to track their daily physical activities, calories burnt, average resting heart rates, and sleep cycle so that they lead a fit life. Such wearables are equipped with laser sensors to collect data.

Heat Index (temperature + humidity) is one common data recorded on these IoT readers. The sensor reads hundreds to millions of data per second. There is a huge and versatile application of this data in the real world like agriculture, weather forecasting, soil monitoring and treatment, enterprise maintenance, and so on.

### Problem Statement

Put yourself in the shoes of a quality analyst whose task is to test the efficacy of new IoT devices. You need to create time-series plots for daily temperature variation for the given duration and find any inconsistencies in the temperature readings (if there are any).

In case the data collected through the device is correct, find the percentages of the yellow, orange, and red zones.

## [Life Expectancy Analysis](lifeExpectancyAnalysis.py) January 2022
### Context

The term **Life Expectancy** refers to the number of years a person can expect to live. It is based on an estimate of the average age of a population when they die. Life expectancy is one of the key metrics used for assessing the overall health of a population. 

 The Global Health Observatory (GHO) data repository under the World Health Organization (WHO) keeps track of the health status as well as many other related factors for all countries. It has been observed that in the past 15 years, there has been a huge development in the health sector resulting in the improvement of human mortality rates. The increases are nearly universal, from the richest to the poorest countries. Let's dive deeper into the life expectancy dataset and find out how different factors influence your life expectancy.

### Problem Statement

As the head of a leading life insurance company, your job is to formulate  global health insurance coverage plans and devise different life insurance solutions for different countries. For this, you need to obtain insightful trends and patterns in people's dying ages across different countries. Also, you need to determine the factors that affect the average life expectancy of people around the world to determine the premium rates for insurance policies.

## [Payroll Calculation OOP](payrollCalculation.py) January 2022
### Context

**Payroll System** of any organization calculates the amount the organization owes to its employees based on various factors such as the time and the number of days they worked, their hourly wages or commission rate, and whether they took leave during the pay period. The system determines the gross pay by evaluating taxes and other deductions. On the payroll date, the system provides the employees with the details of payroll deposits in the form of a **pay slip**.

### Problem Statement 

ABC Finance company hired you as a software developer. Your first assignment is to create a simple  **Payroll System** for the company to perform payroll calculations based on an employee inheritance hierarchy that meets the following requirements:

The company has **Salaried employees** and they are paid a fixed salary regardless of the number of hours they work. Their salary is calculated by adding the basic salary, TA (Travelling allowance), DA (Dearness allowance), and HRA (House rent allowance).

To make the system reusable and extensible, the system must be constructed using an object-oriented methodology.

### Program Requirements

The payroll system must be able to perform the following tasks:

 - Allow the user to input employee details such as employee ID, employee name, and social security number.
 - Reject duplicate employee IDs and prompt the user to enter a unique employee ID for every new employee.
 - Store the employee records temporarily in a collection. 
 - Display the information of all the employees on the screen.
 - Update different employees allowances.
 - Calculate the monthly earnings of the employee based on their type. 

## [Diamond Price Prediction](diamondPricePrediction.py) March 2022
### Problem Statement

A diamond distributor decided to put almost 2000 diamonds for auction. A jewelry company is interested in making a bid to purchase these diamonds in order to expand their business. As a data scientist, your job is to build a prediction model to predict the price of diamonds so that your company knows how much it should bid.

### Program Requirements

1. Explore the diamond dataset by creating the following plots:
   - Box plots between each categorical feature and the `price`.
   - Scatter plots between the numerical features and the `price`.
   
2. Convert categorical attributes into numerical attributes.

3. Create a correlation heatmap for all the columns.

4. Build a linear regression model by selecting the most relevant features to predict the price of diamonds.

5. Reduce multicollinearity (if exists) by eliminating highly correlated and high VIF features.

5. Evaluate the linear regression model by calculating the parameters such as coefficient of determination, MAE, MSE, RMSE, and mean of residuals by checking for homoscedasticity.

## [House Price Prediction](housePricePrediction.py) June 2022
### Problem Statement

You are willing to sell your house. You are not sure about the price of your house and want to estimate its price. You are provided with the dataset and need to make a prediction model that will help you to get a good estimate of your house for selling.
### Program Requirements

1. Explore the Housing dataset by creating the following plots:
   - Box plots between each categorical feature and the `price`.
   - Scatter plots between the numerical features and the `price`.
   
2. Convert categorical attributes into numerical attributes using feature encoding.

3. Build a linear regression model by selecting the most relevant features to predict the price of houses.

4. Evaluate the linear regression model by calculating the parameters such as coefficient of determination, MAE, MSE, RMSE, and mean of residuals by checking for homoscedasticity.

## [Olivetti Faces Case-Study](olivettiFaces.py) November 2022
### Context

Face Recognition, a highly active area in Artificial Intelligence, is used to identify faces in photos, videos, or real time. There are various applications of face recognition based on its purpose which can be on small levels like a Mobile Phone or a high level like a Government Document. Some of them are:

- Authenticate services like face lock and attendance system.

- Management of Data like Census Management or small-level Mobile Phone Photo Gallery Management.

### Problem Statement

The dataset contains a set of images taken between April 1992 and 1994 at AT&T Laboratories Cambridge. 

The data includes ten different images of each of 40 distinct people. The images were taken at different times and with varying lights, with different facial expressions (open/closed eyes, smiling/not smiling), and with/without glasses. All the images were taken against a dark background with the people in an upright, frontal position.

The goal here is to train the SVM classification model to identify the recognize  the labels (identifying the people) based on the images.

### Program Requirements

1. Importing and Analysing the Dataset

2. Visualising the Images

3. Train-Test Split

4. Model Training and Prediction

5. Model Evaluation
