import argparse
import re
import yaml
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('srweb', help='Path to an installation of srweb')
args = parser.parse_args()

docs_root = Path('docs')
srweb_root = Path(args.srweb) / 'content' / 'en' / 'docs'

# Clear out existing content
for previous_file in docs_root.glob('**/*.md'):
    previous_file.unlink()

MD_REGEX = re.compile('^//([A-Z_]+)\s*:\s*(.*)\s*$')

def convert_document(source, destination):
    try:
        destination.parent.mkdir(parents=True)
    except FileExistsError:
        pass
    with source.open('r') as source_f, destination.open('w') as dest_f:
        metadata = {}
        while True:
            md_line = source_f.readline()
            match = MD_REGEX.match(md_line)
            if match is None:
                break
            if match.group(2):
                metadata[match.group(1)] = match.group(2)
        if metadata.get('CONTENT_TYPE', 'markdown') != 'markdown':
            print("ERROR: {} is not Markdown".format(source))
            return
        yaml_data = {'layout': 'default'}
        yaml_data['title'] = metadata.get('TITLE', 'Documentation')
        if 'DESCRIPTION' in metadata:
            yaml_data['description'] = metadata['DESCRIPTION']
        dest_f.write('---\n')
        yaml.dump(yaml_data, dest_f, default_flow_style=False)
        dest_f.write('---\n')
        data = source_f.read()
        dest_f.write(data)

for doc_page in srweb_root.glob('**/*'):
    if doc_page.is_dir():
        continue
    if doc_page.name.startswith('.'):
        continue
    target_path = (docs_root / doc_page.relative_to(srweb_root)).with_suffix('.md')
    convert_document(doc_page, target_path)

