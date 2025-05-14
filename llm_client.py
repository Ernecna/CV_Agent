import requests
import json
from typing import Dict, Tuple

API_KEY = "AIzaSyCz_nkFk_okMP_jdfvyuI0p3zHwk8XiIAM"
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"


def _call_gemini_model(prompt: str, model: str) -> Tuple[str, Dict[str, int]]:
    url = f"{BASE_URL}/{model}:generateContent?key={API_KEY}"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    # Hata kontrolü ekleyebilirsin burada
    output_text = result["candidates"][0]["content"]["parts"][0]["text"]
    return output_text, {}
def ask_gemini(prompt: str) -> str:
    response, _ = _call_gemini_model(prompt, "gemini-2.0-flash")
    return response

def ask_gemini_lite(prompt: str) -> str:
    response, _ = _call_gemini_model(prompt, "gemini-2.0-flash-lite")
    return response

def ask_gemini_pro_preview(prompt: str) -> str:
    response, _ = _call_gemini_model(prompt, "gemini-2.5-pro-preview-05-06")
    return response

def ask_gemma_3_27B(prompt: str) -> str:
    response, _ = _call_gemini_model(prompt, "gemma-3-27b-it")
    return response