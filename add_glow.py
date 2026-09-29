import os
import re

def implement_glow_cursor():
    # 1. Update HTML
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    if '<div id="glow-cursor"></div>' not in html:
        # Insert right after body tag opening
        html = re.sub(r'(<body[^>]*>)', r'\1\n    <div id="glow-cursor"></div>', html)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)

    # 2. Update CSS
    with open('style.css', 'r', encoding='utf-8') as f:
        css = f.read()
        
    if '#glow-cursor' not in css:
        cursor_css = """

/* --- Interactive Glow Cursor --- */
#glow-cursor {
    position: fixed;
    top: 0;
    left: 0;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(0, 122, 255, 0.1) 0%, rgba(173, 5, 230, 0.05) 50%, transparent 70%);
    border-radius: 50%;
    pointer-events: none;
    z-index: -1;
    will-change: transform;
    mix-blend-mode: multiply;
}

body.dark #glow-cursor {
    background: radial-gradient(circle, rgba(0, 122, 255, 0.25) 0%, rgba(173, 5, 230, 0.1) 50%, transparent 70%);
    mix-blend-mode: screen;
}
"""
        css += cursor_css
        with open('style.css', 'w', encoding='utf-8') as f:
            f.write(css)

    # 3. Update JS
    with open('script.js', 'r', encoding='utf-8') as f:
        js = f.read()

    if 'Interactive Glowing Cursor' not in js:
        cursor_js = """
    // --- Interactive Glowing Cursor ---
    const glowCursor = document.getElementById('glow-cursor');
    if (glowCursor) {
        let mouseX = window.innerWidth / 2;
        let mouseY = window.innerHeight / 2;
        let glowX = mouseX;
        let glowY = mouseY;

        document.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
        });

        const animateGlow = () => {
            // Easing for smooth follow effect
            glowX += (mouseX - glowX) * 0.1;
            glowY += (mouseY - glowY) * 0.1;
            
            // Offset by half the width/height (300px) to center it on the cursor
            glowCursor.style.transform = `translate(${glowX - 300}px, ${glowY - 300}px)`;
            requestAnimationFrame(animateGlow);
        };
        animateGlow();
    }
"""
        # Append before the last closing }); of DOMContentLoaded
        js = re.sub(r'\}\);$', f'{cursor_js}\n}});', js)
        with open('script.js', 'w', encoding='utf-8') as f:
            f.write(js)

if __name__ == '__main__':
    implement_glow_cursor()
