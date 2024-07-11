from typing import List, Optional, Union
from datetime import datetime

class DataPreprocess:
    @staticmethod
    def clean_boolean(value: str) -> bool:
        if isinstance(value, str):
            return value.lower() in ['yes', 'oui', 'true', '1']
        return bool(value)

    @staticmethod
    def clean_float(value: str) -> float:
        try:
            return float(value)
        except ValueError:
            return float('nan')

    @staticmethod
    def clean_int(value: str) -> int:
        try:
            return int(value)
        except ValueError:
            return 0

    @staticmethod
    def clean_date(value: str) -> Optional[datetime]:
        try:
            return datetime.strptime(value, '%d/%m/%Y')
        except ValueError:
            return None

    @staticmethod
    def clean_list(value: str, delimiter: str = '/') -> List[str]:
        if value:
            return value.split(delimiter)
        return []

    @staticmethod
    def clean_list_of_ints(value: str, delimiter: str = '/') -> List[int]:
        return [DataPreprocess.clean_int(v) for v in value.split(delimiter) if v]