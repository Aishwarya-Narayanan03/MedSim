# batch_upload.py - Batch upload script for MedSim
import csv
import requests

def upload_cases(csv_path, api_url):
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            response = requests.post(api_url, json=row)
            print(f"Uploaded: {row['case_id']} Status: {response.status_code}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python batch_upload.py <csv_path> <api_url>")
    else:
        upload_cases(sys.argv[1], sys.argv[2])
