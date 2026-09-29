import re

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Fix garbled hero text
    html = re.sub(r'YOY|ðŸŒŸ|\?\?Final', '🌟 Final', html)
    html = re.sub(r'Y\?|ðŸ†|\?\?\|', '🏆 |', html)
    html = html.replace('1st Prize ??', '1st Prize 🏆')

    # 2. Add Resume Button in Hero Section
    # Find the View My Work button and wrap it in a flex container with the new button
    view_my_work_regex = r'(<a href="#projects" class="[^"]*?bg-apple-blue[^"]*?">\s*View My Work\s*</a>)'
    
    resume_button = """<div class="mt-12 flex flex-col sm:flex-row justify-center items-center gap-4">
            <a href="#projects" class="px-6 py-3 bg-apple-blue text-white font-semibold rounded-full shadow-lg hover:bg-blue-600 transition duration-300 transform hover:scale-105 animate-pulse-slow">
                View My Work
            </a>
            <a href="./resume.pdf" target="_blank" class="px-6 py-3 bg-white dark:bg-zinc-800 text-zinc-900 dark:text-white border border-zinc-200 dark:border-zinc-700 font-semibold rounded-full shadow-lg hover:bg-zinc-100 dark:hover:bg-zinc-700 transition duration-300 transform hover:scale-105">
                Download Resume
            </a>
        </div>"""
    
    # Replace the single button with the dual button flex container, removing the mt-12 from the original button regex matching
    if 'Download Resume' not in html:
        html = re.sub(r'<a href="#projects" class="mt-12[^"]*?bg-apple-blue[^"]*?">\s*View My Work\s*</a>', resume_button, html)


    # 3. Add Project Filtering
    # Insert filter buttons before the grid
    filter_html = """
            <!-- Project Filters -->
            <div class="flex flex-wrap justify-center gap-4 mb-12 fade-in-section filter-container">
                <button class="filter-btn active px-6 py-2 rounded-full bg-zinc-900 dark:bg-white text-white dark:text-black font-medium transition-all shadow-md" data-filter="all">All</button>
                <button class="filter-btn px-6 py-2 rounded-full bg-zinc-200 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300 hover:bg-zinc-300 dark:hover:bg-zinc-700 font-medium transition-all shadow-sm" data-filter="ai">AI & ML</button>
                <button class="filter-btn px-6 py-2 rounded-full bg-zinc-200 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300 hover:bg-zinc-300 dark:hover:bg-zinc-700 font-medium transition-all shadow-sm" data-filter="iot">IoT & Hardware</button>
                <button class="filter-btn px-6 py-2 rounded-full bg-zinc-200 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300 hover:bg-zinc-300 dark:hover:bg-zinc-700 font-medium transition-all shadow-sm" data-filter="web">Full Stack Web</button>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8" id="projects-grid">"""
            
    if 'data-filter="all"' not in html:
        html = html.replace('<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">', filter_html)


    # Assign data-category to projects (approximate based on titles)
    def categorize_project(match):
        full_card = match.group(0)
        title = match.group(1).lower()
        cat = 'web'
        if 'ai' in title or 'rag' in title or 'yolo' in title or 'object detection' in title or 'jarvis' in title or 'anpr' in title or 'plate' in title or 'model' in title:
            cat = 'ai'
        elif 'iot' in title or 'esp' in title or 'robot' in title or 'rover' in title or 'drone' in title or 'motor' in title or 'guardian' in title or 'wi-fi' in title or 'obstacle' in title:
            cat = 'iot'
        
        # Add data-category to the outer div
        if 'data-category' not in full_card:
            return full_card.replace('class="project-card', f'data-category="{cat}" class="project-card')
        return full_card

    html = re.sub(r'<div class="project-card[^>]*>.*?<h3 class="text-2xl font-bold mb-2">(.*?)</h3>', categorize_project, html, flags=re.DOTALL)


    # 4. Add lazy loading to images
    # Replace <img ...> with <img ... loading="lazy"> if not present
    html = re.sub(r'(<img\s+(?!.*?loading=)[^>]*?)>', r'\1 loading="lazy">', html)

    # 5. Update Contact Form
    form_start = r'<form class="space-y-6">'
    form_replacement = r"""<form action="https://api.web3forms.com/submit" method="POST" class="space-y-6">
                    <input type="hidden" name="access_key" value="YOUR_ACCESS_KEY_HERE">"""
    html = html.replace(form_start, form_replacement)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    update_html()
