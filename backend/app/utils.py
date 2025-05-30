import os, json

def read_log_file(file) -> str:
    """
    Read the log file and return its content.
    
    Args:
        file: The file object to read from.
        
    Returns:"""
    print("Reading log file...")
    data = json.load(file)
    prompts = data['prompts']
    prompt_list = [prompt['prompt'] for prompt in prompts]
    for prompt in prompt_list:
        print(prompt)
        
    return prompt_list
        
    
def open_log_file() -> str:
    """
    Open the log file and return its content.
    
    Returns:
        str: The content of the log file.
    """
    current_dir = os.path.dirname(__file__)
    log_file_path = os.path.join(current_dir, 'utils','prompt_log.json')
    try:
        with open(log_file_path, 'r', encoding='utf-8') as file:
            history = read_log_file(file)
    except FileNotFoundError:
        return "Log file not found."
    except Exception as e:
        return f"An error occurred while reading the log file: {e}"

def write_log_file(data: str) -> None:
    """
    Write data to the log file.
    
    Args:
        data: The data to write to the log file.
    """
    current_dir = os.path.dirname(__file__)
    log_file_path = os.path.join(current_dir, 'utils', 'prompt_log.json')
    
    try:
        with open(log_file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Log file updated successfully.")
    except Exception as e:
        print(f"An error occurred while writing to the log file: {e}")
open_log_file()
