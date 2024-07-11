import pandas as pd
from datetime import datetime
from typing import Optional, List
from Patient import Patient

def parse_bool(value: str) -> bool:
    return value.strip().lower() in ['yes', 'true', '1', 'oui']

def parse_date(value: str) -> Optional[datetime]:
    try:
        return datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        return None
    
def load_patients_from_csv(csv_file: str) -> List[Patient]:
    df = pd.read_csv(csv_file)