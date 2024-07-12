from typing import List
import pandas as pd
import streamlit as st
from patient_data_loader import load_patients_from_csv
from Patient import Patient

# Fonction principale de l'application
def main():
    st.title("Data Anonymization App")
    
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        patients: List[Patient] = load_patients_from_csv(uploaded_file)

        if patients is None or len(patients) == 0:
            st.error("Failed to load data from CSV file.")
            return
        
        if patients is not None and len(patients) > 0:
            df = pd.DataFrame(patients)
            st.subheader("Data Preview:")
            st.write(df.head())
            
            if st.button("Anonymize All"):
                anonymized_data = []
                for patient in patients:
                    anonymized_data.append(patient.anonymize())

                anonymized_data = pd.DataFrame(anonymized_data)
                
                st.subheader("Anonymized Data Preview:")
                st.write(anonymized_data.head())
                
                csv = anonymized_data.to_csv(index=False)
                if csv:
                    st.download_button(
                        label="Download Anonymized Data",
                        data=csv,
                        file_name='anonymized_data.csv',
                        mime='text/csv',
                    )

# Exécuter l'application principale
if __name__ == "__main__":
    main()
