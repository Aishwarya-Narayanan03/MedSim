# cli.py - Simple CLI for MedSim admin tasks
import argparse
import requests

def verify_admin(user_id, api_url):
    response = requests.post(f"{api_url}/admin/verify", json={"user_id": user_id})
    print(response.json())

def main():
    parser = argparse.ArgumentParser(description="MedSim Admin CLI")
    parser.add_argument("--verify-admin", nargs=2, metavar=("USER_ID", "API_URL"), help="Verify admin user")
    args = parser.parse_args()

    if args.verify_admin:
        user_id, api_url = args.verify_admin
        verify_admin(user_id, api_url)

if __name__ == "__main__":
    main()
