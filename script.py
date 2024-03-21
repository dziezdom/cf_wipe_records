import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Configuration settings
api_token = 'YOUR_API_TOKEN_HERE'  # Replace with your actual API token.
zone_id = 'YOUR_ZONE_ID_HERE'  # Replace with the actual Zone ID of your domain.

headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

def list_dns_records(zone_id):
    """
    Fetches a list of DNS records for a given zone.

    Parameters:
        zone_id (str): The Zone ID of the Cloudflare domain.

    Returns:
        list: A list of DNS records, each represented as a dictionary.
    """
    list_url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    response = requests.get(list_url, headers=headers)
    if response.status_code == 200:
        return response.json()['result']
    else:
        print(f"Error listing DNS records: {response.text}")
        return None

def delete_dns_record(zone_id, record_id):
    """
    Deletes a DNS record by its ID.

    Parameters:
        zone_id (str): The Zone ID of the Cloudflare domain.
        record_id (str): The ID of the DNS record to be deleted.

    Returns:
        bool: True if deletion was successful, False otherwise.
    """
    delete_url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"
    response = requests.delete(delete_url, headers=headers)
    return response.status_code == 200

def delete_records_in_parallel(records):
    """
    Deletes DNS records in parallel to speed up the process.

    Parameters:
        records (list): A list of DNS records to be deleted.
    """
    with ThreadPoolExecutor(max_workers=20) as executor:
        future_to_record = {executor.submit(delete_dns_record, zone_id, record['id']): record for record in records}
        for future in as_completed(future_to_record):
            record = future_to_record[future]
            try:
                success = future.result()
                if success:
                    print(f"Successfully deleted record {record['id']}.")
                else:
                    print(f"Failed to delete record {record['id']}.")
            except Exception as exc:
                print(f"Error deleting record {record['id']}: {exc}")

# Main script execution
if __name__ == "__main__":
    while True:
        records = list_dns_records(zone_id)
        if records:
            print(f"Found {len(records)} records to delete.")
            delete_records_in_parallel(records)
            time.sleep(2)  # Short break to avoid overwhelming the API
        else:
            print("No more records found to delete.")
            break
