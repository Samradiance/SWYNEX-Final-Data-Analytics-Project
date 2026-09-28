# Project Overview:-

This project is the final Data Analytics Project completed as part of the SWYNEX Technologies Internship.

The project demonstrates the complete data analytics workflow, starting from raw data cleaning and preparation, followed by exploratory data analysis (EDA), visualization, and finally the development of an interactive Power BI dashboard.

The analysis focuses on a music dataset containing information about tracks, artists, genres, release dates, popularity, streams, and audio features.

# Problem Statement:-

The objective of this project is to analyze music data and identify meaningful patterns and trends related to music performance.

The project focuses on understanding:
  -How music performance varies across different genres
  -How streaming performance changes over release years
  -The relationship between popularity and streams
  -Differences between explicit and non-explicit tracks
  -The relationship between audio characteristics and music performance
  -How artists, genres, and release years influence the overall dataset

The final results are presented through an interactive Power BI dashboard to make the analysis easier to understand.

# Dataset Information:-

The dataset contains 50,000 music records and 33 attributes.

The dataset includes information related to:
  -Track names
  -Artists
  -Albums
  -Genres
  -Release dates
  -Release years
  -Popularity
  -Stream counts
  -Explicit content
  -Audio features
  -Danceability
  -Energy
  -And other music-related attributes

The dataset was first cleaned and prepared before performing further analysis.

# Tools & Technologies Used:-

  -Python
  -Pandas
  -Jupyter Notebook
  -Matplotlib
  -Seaborn
  -Power BI
  -GitHub

# Data Cleaning & Preparation:-

The raw dataset was processed using Python and Pandas.

The main data preparation steps included:

  -Loading the dataset into Python.
  -Examining the structure and dimensions of the dataset.
  -Checking for missing values.
  -Checking for duplicate records.
  -Converting the release_date column into the appropriate datetime format.
  -Checking numerical columns for consistency.
  -Preparing the cleaned dataset for analysis.
  -Saving the cleaned data for use in further analysis and visualization.

The cleaned dataset was then used for Exploratory Data Analysis and Power BI visualization.

# Exploratory Data Analysis:-

Exploratory Data Analysis was performed to understand the patterns and relationships within the music dataset.

The analysis included:
  -Distribution of music across genres
  -Streaming performance by genre
  -Streaming trends across release years
  -Popularity analysis
  -Stream count analysis
  -Explicit vs non-explicit music comparison
  -Analysis of audio characteristics
  -Relationship between popularity and streams
  -Examination of important numerical variables

Visualizations were created using Matplotlib and Seaborn to make the patterns easier to understand.

# Power BI Dashboard:-

An interactive Power BI dashboard was created to present the results of the analysis.

Key Performance Indicators
The dashboard includes important KPIs such as:
  -Total Tracks: 50K
  -Total Streams: Approximately 6B
  -Average Popularity: 28.14
  -Average Danceability: 0.66
  -Dashboard Visualizations

The dashboard contains visualizations such as:
  -Number of Tracks by Genre
  -Average Streams by Genre
  -Average Streams by Release Year
  -Popularity vs Stream Count
  -Average Streams: Explicit vs Non-Explicit
  -Interactive Filters

Users can interact with the dashboard using filters/slicers such as:
  -Genre
  -Release Year
  -Artist

These filters allow the user to explore the data from different perspectives.

# Key Insights:-

The analysis provides several useful observations about the music dataset:

  1. Genre Analysis:- The number of tracks and streaming performance varies across different music genres. Comparing genres helps identify differences in their representation and average streaming performance.

  2. Release Year Analysis:- The dashboard allows streaming performance and track distribution to be examined across different release years, helping identify changes and patterns over time.

  3. Popularity and Streams:- The relationship between track popularity and stream count was analyzed using a scatter plot. This helps examine whether popularity and streaming performance are related.

  4. Explicit vs Non-Explicit Tracks:- The dashboard compares the average streaming performance of explicit and non-explicit tracks.

  5. Audio Features:- Audio characteristics such as danceability can be compared with other performance-related variables to explore possible relationships between musical characteristics and audience engagement.

  6. Interactive Analysis:- The Power BI dashboard allows users to filter the information by genre, artist, and release year, making it possible to explore specific parts of the dataset interactively.

# Project Structure:-

SWYNEX-Final-Data-Analytics-Project/
│
├── README.md
├── music_dataset.csv
├── cleaned_music_dataset.csv
├── data_cleaning.py
├── EDA_Music_Analysis.ipynb
├── SWYNEX_Interactive_Dashboard.pbix
└── dashboard_screenshot.png

# Project Workflow:-

Raw Dataset
     ↓
Data Cleaning & Preparation
     ↓
Exploratory Data Analysis
     ↓
Data Visualization
     ↓
Power BI Dashboard
     ↓
Insights & Findings

# Learning Outcomes:-

Through this project, I gained practical experience in:

  -Data cleaning using Python and Pandas
  -Handling and examining real-world datasets
  -Exploratory Data Analysis
  -Data visualization
  -Identifying patterns and trends in data
  -Creating interactive dashboards using Power BI
  -Presenting data-driven insights
  -Organizing and documenting an analytics project using GitHub

# Conclusion:-

This project demonstrates the complete data analytics process, from raw data preparation to the presentation of insights through an interactive dashboard.

By combining Python, Pandas, data visualization, and Power BI, the project provides an organized analysis of music data and demonstrates how raw data can be transformed into meaningful information and interactive visual insights.

# Internship:-

Internship: Data Analytics Internship
Organization: SWYNEX Technologies
Project: Final Data Analytics Project
Domain: Data Analytics
