
import requests
from io import BytesIO
from zipfile import ZipFile
import os

url = 'https://api.worldbank.org/v2/en/indicator/SN.ITK.DEFC.ZS?downloadformat=csv'
response = requests.get(url)
if response.status_code == 200:
    with ZipFile(BytesIO(response.content)) as z:
        os.makedirs('data/raw_data', exist_ok=True)
        for file in z.namelist():
            if file.startswith('API_') and file.endswith('.csv'):  # Main data file
                z.extract(file, 'data/raw_data')
                print(f'Extracted {file} to data/raw_data/')
else:
    print('Download failed:', response.status_code)
