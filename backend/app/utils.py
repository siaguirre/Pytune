import os, json, io
from datetime import datetime

# Inicializar variables globales
prompt_history = []
prompt_variations = []

def open_log_file(mode='r', data='', file_name='') -> str:
    """Abre el archivo de log."""
    def read_log_file(file) -> list:
        file.seek(0)
        first_char = file.read(1)
        if not first_char:
            return []
        file.seek(0)
        data = json.load(file)
        file.close()
        return data.get('prompts', [])
    
    def write_log_file(file, data: str, old_prompts) -> None:
        """ Escribe los datos en el archivo de log. """
        data = {
            'prompt': data,
            'fecha_introduccion': datetime.now().isoformat()
        }
        if old_prompts:
            prompts = {'prompts': [process_prompt(prompt, list(prompt.keys())) for prompt in old_prompts]}
            prompts['prompts'].append(data)
            if len(prompts['prompts']) > 10:
                prompts['prompts'] = prompts['prompts'][-10:]
            json.dump(prompts, file, indent=4, ensure_ascii=False)
        else:
            json.dump({'prompts': [data]}, file, indent=4, ensure_ascii=False)

    file = open_file(file_name)
    if not isinstance(file, io.IOBase):
        return file
    else:
        if mode == 'r':
            data = read_log_file(file)
            file.close()
            return data
        elif mode == 'w':
            old_prompts = read_log_file(file)
            file.close()
            file = open_file(file_name, 'w')
            write_log_file(file, data, old_prompts)
            file.close()
    
def process_prompt(prompt, keys, i=0):
    """Recibe prompt y llaves totales del diccionario para quedarse con las que resulten importantes """
    important_keys = ['fecha_introduccion', 'prompt']
    
    if len(prompt) <= len(important_keys):
        return prompt
        
    if i >= len(keys):
        i = 0
    
    if keys[i] not in important_keys:
        prompt.pop(keys[i])
        keys.pop(i)
    i+=1
    return process_prompt(prompt, keys, i)
    
def open_file(file_name, mode='r'):
    current_dir = os.path.dirname(__file__)
    log_file_path = os.path.join(current_dir, 'utils',file_name)
    try:
        return open(log_file_path, mode, encoding='utf-8')    
    except FileNotFoundError:
        return "No se encontró el archivo."
    except Exception as e:
        return f"Se encontró un error al abrir el archivo de Log {e}"

def get_prompt_history():
    prompts = open_log_file('r', file_name='prompt_log.json')
    clean_prompts = [process_prompt(prompt, list(prompt.keys())) for prompt in prompts]
    return clean_prompts


def open_variations_file(mode='r', data='', file_name='') -> str:
    """Abre el archivo de variations."""
    def read_variations_file(file) -> list:
      
        print("Reading variations file...")
        data = json.load(file)
        return data
        
    file = open_file(file_name, mode)
    if not isinstance(file, io.IOBase):
        return file
    else:
        data = read_variations_file(file)
        file.close()
        return data

def get_variations():
    variations = open_variations_file('r', file_name='prompt_variations.json')
    return variations

def save_prompt(prompt):
    """Guarda un prompt en el archivo de log."""
    open_log_file('w', data=prompt, file_name='prompt_log.json')