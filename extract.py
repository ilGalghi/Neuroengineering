import os
import shutil

# Definisci la directory corrente e la cartella di destinazione
base_dir = os.path.dirname(os.path.abspath(__file__))
target_dir = os.path.join(base_dir, 'all-files')

# Crea la cartella "all-files" se non esiste
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Naviga attraverso tutte le cartelle e i file
for root, dirs, files in os.walk(base_dir):
    # Rimuovi le cartelle nascoste (come .git) dalla lista di navigazione
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    
    # Salta la cartella di destinazione per evitare di copiare i file su loro stessi
    if target_dir in root:
        continue
        
    for file in files:
        # Salta i file nascosti o il file LICENSE
        if file.startswith('.') or file == 'LICENSE':
            continue
            
        # Crea i percorsi completi per il file sorgente e di destinazione
        source_path = os.path.join(root, file)
        target_path = os.path.join(target_dir, file)
        
        # Evita di copiare lo script stesso
        if source_path == os.path.abspath(__file__):
            continue
            
        # Gestisci i conflitti di nome: se un file con quel nome esiste già in all-files, aggiungi un numero
        base_name, extension = os.path.splitext(file)
        counter = 1
        while os.path.exists(target_path):
            target_path = os.path.join(target_dir, f"{base_name}_{counter}{extension}")
            counter += 1
            
        # Copia il file
        shutil.copy2(source_path, target_path)

print(f"Copia di tutti i file in '{target_dir}' completata!")