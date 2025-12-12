# etl.py
# -*- coding: utf-8 -*-
"""

This script:
1. Extracts and loads data from multiple sources (Google Sheet, URL, CSV, HTML, SQL).
2. Cleans & transforms datasets.

Author: Nhi Le (nheesele)

"""


import os
import pandas as pd
from sqlalchemy import create_engine


# -----------------------------
# 1. EXTRACT
# -----------------------------
def extract():
    print("\n=== EXTRACTING DATA ===\n")

    data = {}

    # --- Enrollies (Google Sheet XLSX) ---
    ggsheet = '1VCkHwBjJGRJ21asd9pxW4_0z2PWuKhbLR3gUHm-p4GI'
    url_gsheet = f'https://docs.google.com/spreadsheets/d/{ggsheet}/export?format=xlsx'

    data["df"] = pd.read_excel(url_gsheet, sheet_name="enrollies")

    # --- Education (Excel) ---
    url_edu = "https://assets.swisscoding.edu.vn/company_course/enrollies_education.xlsx"
    data["df_education"] = pd.read_excel(url_edu, sheet_name="enrollies_education")

    # --- Working experience (CSV) ---
    url_exp = "https://assets.swisscoding.edu.vn/company_course/work_experience.csv"
    data["df_exp"] = pd.read_csv(url_exp)

    # --- City development index (HTML Table) ---
    tables = pd.read_html("https://sca-programming-school.github.io/city_development_index/index.html")
    data["df_city"] = tables[0]

    # --- SQL Database ---
    engine = create_engine("mysql+pymysql://etl_practice:550814@112.213.86.31:3360/company_course")
    data["df_training_hours"] = pd.read_sql("training_hours", con=engine)
    data["df_employment"] = pd.read_sql("employment", con=engine)

    print("Extraction completed!\n")
    return data


# -----------------------------
# 2. TRANSFORM
# -----------------------------
def transform(data):
    print("=== TRANSFORMING DATA ===\n")

    # Fill NA
    data["df"]["gender"] = data["df"]["gender"].fillna("Unknown")
    data["df_education"] = data["df_education"].fillna("Unknown")
    data["df_exp"] = data["df_exp"].fillna("Unknown")

    print("Transform completed!\n")
    return data


# -----------------------------
# 3. LOAD
# -----------------------------
def load(data):
    print("=== LOADING DATA ===\n")

    # Create output folder
    if not os.path.exists("output"):
        os.makedirs("output")

    # Save as CSV
    for name, df in data.items():
        df.to_csv(f"output/{name}.csv", index=False)

    print("All datasets saved to output/ folder.\n")


# -----------------------------
# MAIN PROCESS
# -----------------------------
def main():
    print("\n======= STARTING ETL PIPELINE =======\n")

    data = extract()
    data = transform(data)
    load(data)

    print("======= ETL PROCESS COMPLETED =======\n")


if __name__ == "__main__":
    main()