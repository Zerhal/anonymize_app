import pandas as pd
import numpy as np
import difflib
import streamlit as st

class DataProcessor:
    def __init__(self):
        self.data = None
        self.variable_transformations = {
            'Âge au dg CMH': self.top_bottom_coding,
            'Date Baseline': self.t_closeness,
            'Gradient intraVG max au repos (mmHg)': self.post_randomization,
            'Gradient intraVG max après Vasalva (mmHg)': self.post_randomization,
            'Valeur NT-pro BNP (ng/L)': self.top_bottom_coding,
            'Date AVC ou AIT (depuis baseline)': self.t_closeness
        }

    def load_data(self, csv_file):
        """Load CSV data and handle potential errors."""
        try:
            self.data = pd.read_csv(csv_file)
            st.success("Data loaded successfully!")
        except pd.errors.ParserError as e:
            st.warning(f"Error parsing CSV file: {e}")
            return None
        except Exception as e:
            st.warning(f"An error occurred: {e}")
            return None
        return self.data

    def clean_data(self):
        """Clean data by standardizing formats and handling missing values."""
        for col in self.data.columns:
            self.data[col] = self.standardize_decimal_format(self.data[col])
            self.data[col] = self.convert_to_numeric(self.data[col])
            if self.data[col].isnull().any():
                self.data[col] = self.data[col].fillna(self.data[col].mean())

    def standardize_decimal_format(self, series):
        """Standardize decimal format to use points instead of commas."""
        return series.astype(str).str.replace(',', '.')

    def convert_to_numeric(self, series):
        """Convert a pandas series to numeric, coercing errors."""
        return pd.to_numeric(series, errors='coerce')

    def anonymize_data(self):
        """Anonymize data using predefined transformations."""
        if self.data is not None:
            self.clean_data()
            for col in self.data.columns:
                closest_match = self.find_closest_variable(col)
                if closest_match:
                    try:
                        st.write(f"Anonymizing column: {col} using {closest_match}")
                        transformation = self.variable_transformations.get(closest_match)
                        if transformation:
                            self.data[col] = transformation(self.data[col])
                        else:
                            st.warning(f"No transformation found for {col} ({closest_match})")
                    except Exception as e:
                        st.warning(f"An error occurred while anonymizing column {col}: {e}")
                else:
                    st.warning(f"No close match found for column: {col}")
        return self.data

    def find_closest_variable(self, column_name):
        """Find the closest variable name for transformation."""
        matches = difflib.get_close_matches(column_name, self.variable_transformations.keys(), n=1, cutoff=0.95)
        if not matches:
            st.warning(f"No close match found for column: {column_name}")
        return matches[0] if matches else None

    def save_anonymized_data(self):
        """Save anonymized data to CSV."""
        if self.data is not None:
            return self.data.to_csv(index=False)
        return None

    def top_bottom_coding(self, series, lower_quantile=0.05, upper_quantile=0.95):
        """Apply top and bottom coding to a series."""
        if pd.api.types.is_numeric_dtype(series):
            lower_bound = series.quantile(lower_quantile)
            upper_bound = series.quantile(upper_quantile)
            st.write(f"Top-Bottom Coding: Lower bound = {lower_bound}, Upper bound = {upper_bound}")
            return np.clip(series, lower_bound, upper_bound)
        else:
            st.warning(f"Top-Bottom Coding not applicable for non-numeric data in column {series.name}.")
            return series

    def rank_swapping(self, series, max_swap_fraction=0.05):
        """Apply rank swapping to a series."""
        if pd.api.types.is_numeric_dtype(series):
            sorted_series = series.sort_values().reset_index(drop=True)
            swap_count = int(len(series) * max_swap_fraction)
            swap_indices = np.random.permutation(len(series))[:swap_count]
            for idx in swap_indices:
                swap_with = np.random.randint(0, len(series))
                sorted_series[idx], sorted_series[swap_with] = sorted_series[swap_with], sorted_series[idx]
            return sorted_series.sort_index()
        else:
            st.warning(f"Rank Swapping not applicable for non-numeric data in column {series.name}.")
            return series

    def post_randomization(self, series, noise_level=0.01):
        """Apply post-randomization to a series."""
        if pd.api.types.is_numeric_dtype(series):
            noise = np.random.normal(0, noise_level, series.shape)
            return series * (1 + noise)
        else:
            st.warning(f"Post Randomization not applicable for non-numeric data in column {series.name}.")
            return series

    def t_closeness(self, series):
        """Placeholder for t-closeness implementation."""
        st.write(f"Applying t-closeness to column {series.name}")
        return series
