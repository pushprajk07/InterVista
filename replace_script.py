import os
import glob

# Replace text in files
directories = ['templates', 'Frontend', '.']
for d in directories:
    if d == '.':
        files = glob.glob('*.md') + glob.glob('*.html')
    else:
        files = glob.glob(os.path.join(d, '*.html')) + glob.glob(os.path.join(d, '*.css')) + glob.glob(os.path.join(d, '*.js'))
        
    for file_path in files:
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            if 'IntelliView' in content:
                print(f"Replacing in {file_path}")
                content = content.replace('IntelliView', 'InterVista')
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

# Rename files
files_to_rename = [
    os.path.join('static', 'IntelliView.png'),
    os.path.join('Frontend', 'IntelliView.png')
]

for file_path in files_to_rename:
    if os.path.exists(file_path):
        new_path = file_path.replace('IntelliView', 'InterVista')
        os.rename(file_path, new_path)
        print(f"Renamed {file_path} to {new_path}")
