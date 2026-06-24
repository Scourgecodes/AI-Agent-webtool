import urllib.request
import json

class WebTool:
    def __init__(self):
        self.name = "Hermione_Web_Tool"

    def run_command(self, user_input):
        parts = user_input.split(",", 1)
        command = parts[0].lower().strip()
        
        try:
            # 1. Check if a website is online
            if command == "check site":
                url = parts[1].strip() if len(parts) > 1 else "https://www.google.com"
                if not url.startswith("http://") and not url.startswith("https://"):
                    url = "https://" + url
                
                with urllib.request.urlopen(url, timeout=5) as response:
                    return f"Result -> {url} is ONLINE (Status Code: {response.getcode()})"
            
            # 2. Fetch sample data from an internet API
            elif command == "fetch api":
                url = "https://jsonplaceholder.typicode.com/todos/1"
                with urllib.request.urlopen(url, timeout=5) as response:
                    data = response.read()
                    json_data = json.loads(data)
                    return f"Result -> API Connected! Internet Task Title: '{json_data['title']}'"
            
            else:
                return "Unknown command. Available tools: check site | fetch api"

        except Exception as e:
            return f"An error occurred: {str(e)}"

# Interactive loop to run the Web Tool
if __name__ == "__main__":
    agent = WebTool()
    print(f"=== {agent.name} is online ===")
    print("Type 'exit' to stop.")
    print("Commands: check site | check site, google.com | fetch api")
    print("-" * 40)

    while True:
        user_input = input("Enter command: ")
        if user_input.lower().strip() == "exit":
            print("Shutting down Web Tool. Goodbye!")
            break
        
        if not user_input.strip():
            continue
            
        response = agent.run_command(user_input)
        print(response)
        print("-" * 40)