import os, json, io

def open_log_file(mode='r', data='', file_name='') -> str:
    """Abre el archivo de log."""
    def read_log_file(file) -> list:
      
        print("Reading log file...")
        data = json.load(file)
        return data['prompts']
    
    def write_log_file(file, data: str) -> None:
        """
        Escribe los datos en el archivo de log.
        args:
            data (str): Los datos a escribir en el archivo de log.
            log_file_path (str): La ruta del archivo de log.
        """
        prompt_list = read_log_file(file)

        json.dump(data, file, ensure_ascii=False, indent=4)
        
    file = open_file(file_name, mode)
    if not isinstance(file, io.IOBase):
        return file
    else:
        if mode == 'r':
            data = read_log_file(file)
            file.close()
            return data
        elif mode == 'w':
            write_log_file(file, data)
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
