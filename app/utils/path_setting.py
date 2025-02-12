import os
from pathlib import Path



youtube_download_path = f'{os.path.join(Path("__file__").absolute().parent, 'asset', 'downloads', 'youtube')}'
speech_file_path = f'{os.path.join(Path("__file__").absolute().parent, 'asset', 'downloads', 'speech')}'

system_reserved_path = f'{os.path.join(Path("__file__").absolute().parent, 'asset', 'data')}'
faq_json_path = f'{os.path.join(system_reserved_path, 'faqs.json')}'
embedding_path = f'{os.path.join(system_reserved_path, 'embedding.json')}'

