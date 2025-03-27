import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def load_api_traffic(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def query_openai(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a security engineer. Analyze the given API request for endpoint details and vulnerabilities."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    api_traffic = load_api_traffic("sample_api_call.txt")
    prompt = f"""Analyze this API call and extract:
- Endpoint
- Method
- Headers
- Parameters
- Response (if any)
- Security issues (IDOR, injection, auth issues, verbose errors, etc.)

API Call:
{api_traffic}
"""
    result = query_openai(prompt)
    print("\n[Analysis Output]\n")
    print(result)
