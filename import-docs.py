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
for previous_file in docs_root.glob('**/*.html'):
    previous_file.unlink()

MD_REGEX = re.compile('^//([A-Z_]+)\s*:\s*(.*)\s*$')
PRE_START_REGEX = re.compile('^<pre><code class="override-lang ([a-z0-9_-]+)">(.*)')

def transliterate_markdown(source_f, dest_f):
    in_code_block = False
    for line in source_f:
        if line.startswith('~~~'):
            in_code_block = not in_code_block
            if in_code_block:
                dest_f.write('{% highlight python %}\n')
            else:
                dest_f.write('{% endhighlight %}\n')
        elif line.startswith('</code></pre>'):
            dest_f.write('{% endhighlight %}\n')
        else:
            ps = PRE_START_REGEX.match(line)
            if ps is not None:
                dest_f.write('{{% highlight {} %}}\n'.format(ps.group(1)))
                dest_f.write(ps.group(2))
                dest_f.write('\n')
            else:
                dest_f.write(line)

def transliterate_html(source_f, dest_f):
    dest_f.write(source_f.read())

FORMATS = {'markdown': (transliterate_markdown, '.md'),
           'html': (transliterate_html, '.html'),
           'md': (transliterate_markdown, '.md')}

redirects = {}

def convert_document(source, destination):
    try:
        destination.parent.mkdir(parents=True)
    except FileExistsError:
        pass
    print('Converting', source, '->', destination)
    with source.open('r') as source_f:
        metadata = {}
        while True:
            md_line = source_f.readline()
            match = MD_REGEX.match(md_line)
            if match is None:
                break
            if match.group(2):
                metadata[match.group(1)] = match.group(2)
        if 'REDIRECT' in metadata:
            redirects[source.relative_to(docs_root)] = (301, metadata['REDIRECT'])
            return
        content_type = metadata.get('CONTENT_TYPE', 'markdown')
        yaml_data = {'layout': 'default'}
        yaml_data['title'] = metadata.get('TITLE', 'Documentation')
        if 'DESCRIPTION' in metadata:
            yaml_data['description'] = metadata['DESCRIPTION']
        transliterator, extension = FORMATS[content_type]
        with destination.with_suffix(extension).open('w') as dest_f:
            dest_f.write('---\n')
            yaml.dump(yaml_data, dest_f, default_flow_style=False)
            dest_f.write('---\n')
            transliterator(source_f, dest_f)

for doc_page in srweb_root.glob('**/*'):
    if doc_page.is_dir():
        continue
    if doc_page.name.startswith('.'):
        continue
    target_path = (docs_root / doc_page.relative_to(srweb_root))
    convert_document(doc_page, target_path)

redirects_path = docs_root / 'redirects.yaml'

# emit redirects
with redirects_path.open('w') as f:
    yaml.dump(redirects, f)

