import os

def fix_garbled():
    with open('index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    # The user pasted the garbled strings from the webpage itself, 
    # meaning the file literally has those characters encoded as utf-8.
    replacements = {
        'ðŸŒŸ': '🌟',
        'ðŸ†': '🏆',
        'â€“': '–',
        'ðŸ¥‰': '🥉',
        'â€”': '—',
        'â€™': "'",
        'â€œ': '"',
        'â€': '"'
    }

    for old, new in replacements.items():
        text = text.replace(old, new)
        
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == '__main__':
    fix_garbled()
