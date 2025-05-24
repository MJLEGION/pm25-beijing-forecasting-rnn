# In src/data_loader.py, update column names to match your data
def preprocess_columns(self, data):
    # Rename columns to standard names
    column_mapping = {
        'your_datetime_column': 'datetime',
        'your_pm25_column': 'PM2.5',
        'your_temp_column': 'temperature',
        # Add more mappings as needed
    }
    return data.rename(columns=column_mapping)