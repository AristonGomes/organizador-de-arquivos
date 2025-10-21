import shutil
import argparse
import logging
from pathlib import Path
from collections import Counter

# --- Configuração do Logging ---
# Configura um logger para registrar informações em um arquivo e também no console.
# Isso é mais robusto e flexível do que usar print() e escrita manual de arquivo.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("organization_log.log", mode='a', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def organize_files(source_dir: Path, dest_dir: Path):
    """
    Organiza os arquivos de um diretório de origem para um diretório de destino,
    agrupando-os em subpastas baseadas em suas extensões.

    Args:
        source_dir (Path): O caminho para o diretório com os arquivos a serem organizados.
        dest_dir (Path): O caminho para o diretório onde os arquivos organizados serão salvos.
    """
    if not source_dir.is_dir():
        logging.error(f"O diretório de origem '{source_dir}' não existe ou não é um diretório.")
        return

    # Cria a pasta de destino principal. O `exist_ok=True` evita erros se a pasta já existir.
    dest_dir.mkdir(exist_ok=True)
    logging.info(f"Diretório de destino: '{dest_dir}'")

    file_extensions = []

    # Usamos .rglob('*') para pegar arquivos em subdiretórios também. Se quiser só o diretório raiz, use .glob('*')
    for file_path in source_dir.glob('*'):
        # --- 1. Robustez: Ignorar subdiretórios e processar apenas arquivos ---
        if not file_path.is_file():
            logging.info(f"Ignorando diretório: '{file_path.name}'")
            continue

        # --- 2. Robustez: Lidar com arquivos sem extensão ---
        extension = file_path.suffix[1:].lower() if file_path.suffix else "sem_extensao"
        file_extensions.append(extension)

        # Cria a subpasta de destino para a extensão
        target_subdir = dest_dir / extension
        target_subdir.mkdir(exist_ok=True)

        # Define o caminho final do arquivo
        destination_path = target_subdir / file_path.name

        try:
            # --- 3. Melhoria: Usar copy2 para preservar metadados (data de criação/modificação) ---
            shutil.copy2(file_path, destination_path)
            logging.info(f"Copiado '{file_path.name}' para '{target_subdir}'")
        except shutil.SameFileError:
            logging.warning(f"O arquivo '{file_path.name}' já está no destino. Ignorando.")
        except PermissionError:
            logging.error(f"Sem permissão para copiar '{file_path.name}'. Ignorando.")
        except Exception as e:
            logging.error(f"Erro ao copiar '{file_path.name}': {e}")

    # --- 4. Eficiência: Usar collections.Counter para contagem ---
    if not file_extensions:
        logging.info("Nenhum arquivo encontrado para organizar.")
        return

    stats = Counter(file_extensions)
    total_files = sum(stats.values())

    logging.info("-" * 30)
    logging.info("Organização Concluída!")
    logging.info(f"Total de arquivos processados: {total_files}")
    logging.info("Arquivos por extensão:")
    for ext, count in stats.items():
        logging.info(f"  - {ext}: {count} arquivo(s)")
    logging.info("-" * 30)


import shutil
import argparse
import logging
from pathlib import Path
from collections import Counter

# --- Configuração do Logging ---
# Configura um logger para registrar informações em um arquivo e também no console.
# Isso é mais robusto e flexível do que usar print() e escrita manual de arquivo.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("organization_log.log", mode='a', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def organize_files(source_dir: Path, dest_dir: Path):
    """
    Organiza os arquivos de um diretório de origem para um diretório de destino,
    agrupando-os em subpastas baseadas em suas extensões.

    Args:
        source_dir (Path): O caminho para o diretório com os arquivos a serem organizados.
        dest_dir (Path): O caminho para o diretório onde os arquivos organizados serão salvos.
    """
    if not source_dir.is_dir():
        logging.error(f"O diretório de origem '{source_dir}' não existe ou não é um diretório.")
        return

    # Cria a pasta de destino principal. O `exist_ok=True` evita erros se a pasta já existir.
    dest_dir.mkdir(exist_ok=True)
    logging.info(f"Diretório de destino: '{dest_dir}'")

    file_extensions = []

    # Usamos .rglob('*') para pegar arquivos em subdiretórios também. Se quiser só o diretório raiz, use .glob('*')
    for file_path in source_dir.glob('*'):
        # --- 1. Robustez: Ignorar subdiretórios e processar apenas arquivos ---
        if not file_path.is_file():
            logging.info(f"Ignorando diretório: '{file_path.name}'")
            continue

        # --- 2. Robustez: Lidar com arquivos sem extensão ---
        extension = file_path.suffix[1:].lower() if file_path.suffix else "sem_extensao"
        file_extensions.append(extension)

        # Cria a subpasta de destino para a extensão
        target_subdir = dest_dir / extension
        target_subdir.mkdir(exist_ok=True)

        # Define o caminho final do arquivo
        destination_path = target_subdir / file_path.name

        try:
            # --- 3. Melhoria: Usar copy2 para preservar metadados (data de criação/modificação) ---
            shutil.copy2(file_path, destination_path)
            logging.info(f"Copiado '{file_path.name}' para '{target_subdir}'")
        except shutil.SameFileError:
            logging.warning(f"O arquivo '{file_path.name}' já está no destino. Ignorando.")
        except PermissionError:
            logging.error(f"Sem permissão para copiar '{file_path.name}'. Ignorando.")
        except Exception as e:
            logging.error(f"Erro ao copiar '{file_path.name}': {e}")

    # --- 4. Eficiência: Usar collections.Counter para contagem ---
    if not file_extensions:
        logging.info("Nenhum arquivo encontrado para organizar.")
        return

    stats = Counter(file_extensions)
    total_files = sum(stats.values())

    logging.info("-" * 30)
    logging.info("Organização Concluída!")
    logging.info(f"Total de arquivos processados: {total_files}")
    logging.info("Arquivos por extensão:")
    for ext, count in stats.items():
        logging.info(f"  - {ext}: {count} arquivo(s)")
    logging.info("-" * 30)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organiza arquivos de um diretório em subpastas por extensão.")
    
    # Observe: 'required=False' e 'default=None'.
    # O script não vai quebrar se o usuário não passar nada.
    parser.add_argument("-s", "--source", type=Path, default=None, help="Diretório de origem contendo os arquivos a serem organizadosDiretório de destino para salvar os arquivos organizados. (Padrão: 'arquivos_organizados')."
    )
    parser.add_argument("-d", "--destination", type=Path, default=None, help="Diretório de destino.")
    
    args = parser.parse_args()

    # --- Lógica Híbrida ---
    
    # 1. Verifica se a origem foi fornecida via linha de comando
    if args.source is None:
        print("--- Modo Interativo ---")
        # Se não foi, entra no modo interativo e pergunta
        source_path_str = input("Qual o caminho da pasta de ORIGEM que você quer organizar? ")
        args.source = Path(source_path_str)
        
        # (Aqui você adicionaria validações, ex: um loop while para garantir que a pasta existe)
        while not args.source.is_dir():
            print(f"Erro: O caminho '{args.source}' não foi encontrado ou não é uma pasta.")
            source_path_str = input("Por favor, digite um caminho de ORIGEM válido: ")
            args.source = Path(source_path_str)

    # 2. Verifica se o destino foi fornecido
    if args.destination is None:
        # Se não foi, pergunta
        dest_path_str = input("Onde você quer salvar os arquivos? (Pressione ENTER para usar 'arquivos_organizados'): ")
        if not dest_path_str: # Se o usuário só apertou Enter
            args.destination = Path("arquivos_organizados")
        else:
            args.destination = Path(dest_path_str)

    # 3. Executa a função principal com os argumentos (sejam eles do argparse ou do input)
    print(f"\nIniciando organização...")
    # (A função logging continuará funcionando normalmente)
    organize_files(args.source, args.destination)