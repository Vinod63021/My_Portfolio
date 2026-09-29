import os

def enhance_js():
    with open('script.js', 'r', encoding='utf-8') as f:
        js = f.read()

    if 'Project Filtering' not in js:
        filter_script = """
    // --- Project Filtering ---
    const filterBtns = document.querySelectorAll('.filter-btn');
    const projects = document.querySelectorAll('.project-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all buttons
            filterBtns.forEach(b => {
                b.classList.remove('bg-zinc-900', 'dark:bg-white', 'text-white', 'dark:text-black', 'shadow-md');
                b.classList.add('bg-zinc-200', 'dark:bg-zinc-800', 'text-zinc-700', 'dark:text-zinc-300', 'shadow-sm');
            });

            // Add active class to clicked button
            btn.classList.add('bg-zinc-900', 'dark:bg-white', 'text-white', 'dark:text-black', 'shadow-md');
            btn.classList.remove('bg-zinc-200', 'dark:bg-zinc-800', 'text-zinc-700', 'dark:text-zinc-300', 'shadow-sm');

            const filterValue = btn.getAttribute('data-filter');

            projects.forEach(project => {
                if (filterValue === 'all' || project.getAttribute('data-category') === filterValue) {
                    project.style.display = 'block';
                    // Re-trigger animation
                    project.classList.remove('is-visible');
                    setTimeout(() => project.classList.add('is-visible'), 50);
                } else {
                    project.style.display = 'none';
                    project.classList.remove('is-visible');
                }
            });
        });
    });
"""
        js += "\n" + filter_script
        
        with open('script.js', 'w', encoding='utf-8') as f:
            f.write(js)

if __name__ == '__main__':
    enhance_js()
