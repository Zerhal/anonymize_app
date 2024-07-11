# Data Anonymization App

This project is a Streamlit app for anonymizing data. The app allows users to upload a CSV file and apply various anonymization techniques to the data.

## Features

- Anonymization techniques:
  - Top/bottom-coding
  - Rank-swapping
  - Post-randomisation
  - t-closeness

## Setup

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**

```
git clone https://github.com/Zerhal/anonymize_app.git
cd votre-repo
```

2. **Create a virtual environment and activate it:**

On macOS and Linux:

```
python3 -m venv env
source env/bin/activate
```

On Windows:

```
python -m venv env
.\env\Scripts\activate
```

3. **Install the dependencies:**

```
pip install -r requirements.txt
```

### Running the App

1. **Run the app:**

```
streamlit run anonymize_app.py
```


2. **Open the app in your browser:**

The app should automatically open in your default web browser. If it doesn't, go to http://localhost:8501.

### Usage

1. **Upload a CSV file:**

Upload a CSV file containing the data you want to anonymize.

2. **Choose the anonymization techniques:**

Select the appropriate anonymization techniques and set their parameters.

3. **Preview the anonymized data:**

View the anonymized data in the app.

4. **Download the anonymized data:**

Download the anonymized data as a CSV file.

### Anonymization Techniques

- **Top/Bottom-coding**: Limits the values in a column to a specified range to prevent extreme values from revealing sensitive information.
- **Rank-swapping**: Randomly swaps values within a column to maintain the overall distribution while anonymizing individual data points.
- **Post-randomisation**: Adds random noise to values in a column to anonymize the data while preserving its statistical properties.
- **t-closeness**: Ensures that the distribution of values in the anonymized dataset is close to the original distribution, reducing the risk of re-identification.

### File Structure

├── anonymize_app.py        # Main Streamlit application script
├── DataProcessor           # Class to manage data
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore file
├── README.md               # Project README
└── env                     # Directory for storing data files (ignored by Git)