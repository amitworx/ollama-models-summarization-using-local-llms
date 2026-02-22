from flask import Flask, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup
import ollama

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search')
def search():
    query = request.args.get('q', '')
    url = 'https://ollama.com/library'
    if query:
        url = f'https://ollama.com/library?q={query}'
        
    try:
        print(f"Fetching {url}...")
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
        response.raise_for_status()
        print(f"Status OK. Received {len(response.text)} bytes.")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        models = []
        
        # Ollama library model cards are typically <li> elements containing <a> tags
        # with h2 for name and p for description
        # We will look for elements that look like model listings
        # The exact classes might change, so we look for 'a' tags that wrap 'h2'
        
        # Ollama site structure: <a class="group ... href="/library/model"> <h2 ...>Model</h2> <p ...>Desc</p> </a>
        links = soup.select('a[href^="/library/"]')
        
        seen = set()
        for link in links:
            href = link.get('href', '')
            model_name = href.replace('/library/', '').strip()
            
            if not model_name: continue
            
            # Avoid duplicates if the same model appears multiple times
            if model_name in seen:
                continue
            seen.add(model_name)
            
            # Find description - usually a p tag next to it or inside
            p = link.find('p', class_=lambda c: c and 'max-w' in c)
            if not p:
                p = link.find('p')
            
            description = p.text.strip() if p else "No description available."
            
            # Tags / Pulls counts (Optional, if we can parse them)
            # Typically spans with specific classes, will skip for simplicity
            
            models.append({
                'name': model_name,
                'description': description
            })
            
        return jsonify({'success': True, 'models': models})
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/summarize', methods=['POST'])
def summarize():
    data = request.json
    model_name = data.get('model_name')
    model_desc = data.get('description', '')
    
    if not model_name:
        return jsonify({'success': False, 'error': 'Model name required'})
        
    prompt = f"Please provide a detailed, highly informative summary and evaluation of the AI model named '{model_name}'. The official short description is: '{model_desc}'. What are the use cases, strengths, weaknesses, and potential performance characteristics of this model? Give a comprehensive overview."
    
    try:
        # Use gpt-oss:20b to summarize
        response = ollama.chat(model='gpt-oss:20b', messages=[
            {
                'role': 'system',
                'content': 'You are an AI model expert. Provide comprehensive, accurate, and structured insights about different open-source and proprietary AI models. Format the output in Markdown.'
            },
            {
                'role': 'user',
                'content': prompt
            }
        ])
        
        summary = response['message']['content']
        return jsonify({'success': True, 'summary': summary})
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
