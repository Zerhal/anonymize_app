import DataProcessor as dp
import streamlit as st

# Fonction principale de l'application
def main():
    st.title("Data Anonymization App")
    
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        processor = dp.DataProcessor()
        data = processor.load_data(uploaded_file)
        
        if data is not None:
            st.subheader("Data Preview:")
            st.write(data.head())
            
            if st.button("Anonymize All"):
                anonymized_data = processor.anonymize_data()
                
                st.subheader("Anonymized Data Preview:")
                st.write(anonymized_data.head())
                
                csv = processor.save_anonymized_data()
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
