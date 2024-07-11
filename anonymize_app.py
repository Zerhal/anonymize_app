from typing import List
import streamlit as st
from DataProcessor import DataProcessor
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
        
        st.subheader("Patients:")
        for patient in patients:
            st.write(patient)
        
        # processor = DataProcessor()
        # data = processor.load_data(uploaded_file)
        
        # if data is None:
        #     st.error("Failed to load data from CSV file.")
        #     return
        
        # if data is not None:
        #     st.subheader("Data Preview:")
        #     st.write(data.head())
            
        #     if st.button("Anonymize All"):
        #         anonymized_data = processor.anonymize_data()
                
        #         st.subheader("Anonymized Data Preview:")
        #         st.write(anonymized_data.head())
                
        #         csv = processor.save_anonymized_data()
        #         if csv:
        #             st.download_button(
        #                 label="Download Anonymized Data",
        #                 data=csv,
        #                 file_name='anonymized_data.csv',
        #                 mime='text/csv',
        #             )

# Exécuter l'application principale
if __name__ == "__main__":
    main()
