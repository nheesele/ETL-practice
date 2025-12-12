# ETL Pipeline for Enrollies Data 
![](https://github.com/nheesele/ETL-practice/blob/main/Data-Analyst.jpg)
> Souce: https://thecore.co.in/wp-content/uploads/2025/09/Data-Analyst-Course-in-Chandigarh56.jpg

**Author**: Nhi Le (nheesele)

**Date**: December 2025

**Purpose**: ETL Practice  


## Project Overview

This project implements a complete **ETL (Extract → Transform → Load)** pipeline that collects data about enrolled students (enrollies) from **6 different data sources**, cleans and consolidates them into structured CSV files for further analysis or dashboard building.

The goal is to create a reproducible, well-documented, and schedulable data pipeline.

## Data Sources

| Source                  | Format      | URL / Connection                                       | Key Columns                          |
|-------------------------|--------------|---------------------------------------------------------|--------------------------------------|
| Enrollies basic info    | Google Sheet | `https://docs.google.com/spreadsheets/d/.../export?format=xlsx` | enrollee_id, full_name, city, gender |
| Education               | Excel        | `enrollies_education.xlsx`                              | education_level, major_discipline    |
| Work Experience         | CSV          | `work_experience.csv`                                   | experience, company_size, company_type |
| Training Hours          | MySQL        | Remote DB (provided below)                        | enrollee_id, training_hours          |
| Employment Status       | MySQL        | Remote DB (provided below)                               | enrollee_id, employed (0/1)           |
| City Development Index  | HTML Table   | `https://www.google.com/url?q=https%3A%2F%2Fsca-programming-school.github.io%2Fcity_development_index%2Findex.html` | city, city_development_index         |
**MySQL Database Details** 
- Database type: MySQL  
- Host: 112.213.86.31  
- Port: 3360  
- Login: etl_practice  
- Password: 550814  
- Database name: company_course  
- Tables: `training_hours`, `employment`
### 1. Extract
- All sources are read using `pandas` appropriate readers.
- Google Sheet is accessed publicly via `export?format=xlsx`.
- MySQL connection uses `sqlalchemy` + `pymysql`.
### 2. Transform
Current cleaning steps:
- Fill missing `gender` with "Unknown"
- Fill all missing values in education & experience tables with "Unknown" (to preserve joinability and avoid NaN in analysis)
> **Why "Unknown" instead of drop/remove?**  
> Because `enrollee_id` is crucial for joining tables. Dropping rows would lose valuable data from other sources. "Unknown" keeps the record while clearly marking missing info.
### 3. Load
- Saves each dataset as clean CSV in `/output` folder
- Ready for Power BI, Tableau, or further merging in analysis phase
## How to Run
### Install dependencies
pip install pandas openpyxl sqlalchemy pymysql
### Run the pipeline
python etl.py
