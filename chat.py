from http.server import BaseHTTPRequestHandler
import json
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

class handler(BaseHTTPRequestHandler):

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        data = json.loads(body)

        message = data.get("message", "")

        prompt = f"""
Сен SoulTalk психологиялық көмекші чатботсың.
Жылы, сабырлы, түсіністікпен жауап бер.
Қазақша сөйле.

User:
{message}
"""

        response = model.generate_content(prompt)

        reply = {
            "reply": response.text
        }

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        self.wfile.write(json.dumps(reply).encode())