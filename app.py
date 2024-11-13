from flask import Flask, request, jsonify
from flask_cors import CORS
from invoke_agent import askQuestion

app = Flask(__name__)
CORS(app) 

agentId = "7KMZ9NREMV"  # INPUT YOUR AGENT ID HERE
agentAliasId = "6WP9QSOXDY"
theRegion = "us-west-2"

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    session_id = data.get('sessionId', 'defaultSession')
    end_session = data.get('endSession', False)

    url = f'https://bedrock-agent-runtime.{theRegion}.amazonaws.com/agents/{agentId}/agentAliases/{agentAliasId}/sessions/{session_id}/text'


    try:
        response = askQuestion(question, url, end_session)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
