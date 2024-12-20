import requests
import json
import os
from datetime import datetime

# 네 개의 엔드포인트 URL
ENDPOINTS = {
    "items": "https://poe.game.daum.net/api/trade2/data/items",
    "stats": "https://poe.game.daum.net/api/trade2/data/stats",
    "static": "https://poe.game.daum.net/api/trade2/data/static",
    "filters": "https://poe.game.daum.net/api/trade2/data/filters"
}

# 저장 경로 (Git 리포지토리 내)
OUTPUT_DIR = "data"  # JSON 파일들이 저장될 디렉토리

def fetch_data(url):
    """엔드포인트에서 데이터를 가져옵니다."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data from {url}. Status code: {response.status_code}")

def save_data_to_file(data, file_path):
    """데이터를 JSON 파일로 저장합니다."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    """메인 실행 함수."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)  # 저장 디렉토리가 없으면 생성

    for name, url in ENDPOINTS.items():
        print(f"Fetching data from {url}...")
        data = fetch_data(url)
        file_path = os.path.join(OUTPUT_DIR, f"{name}.json")
        print(f"Saving data to {file_path}...")
        save_data_to_file(data, file_path)

    print("All data fetched and saved successfully.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
