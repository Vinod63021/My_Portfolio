// --- Dark Mode Toggle ---
const themeToggleBtn = document.getElementById('theme-toggle');
const darkIcon = document.getElementById('theme-toggle-dark-icon');
const lightIcon = document.getElementById('theme-toggle-light-icon');
const html = document.documentElement;

// Function to set theme
function setTheme(theme) {
    if (theme === 'dark') {
        html.classList.add('dark');
        darkIcon.classList.remove('hidden');
        lightIcon.classList.add('hidden');
        localStorage.setItem('theme', 'dark');
    } else {
        html.classList.remove('dark');
        darkIcon.classList.add('hidden');
        lightIcon.classList.remove('hidden');
        localStorage.setItem('theme', 'light');
    }
}

// Check for saved theme in localStorage or system preference
const savedTheme = localStorage.getItem('theme');
const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

if (savedTheme) {
    setTheme(savedTheme);
} else if (systemPrefersDark) {
    setTheme('dark');
} else {
    setTheme('light');
}

// Toggle listener
themeToggleBtn.addEventListener('click', () => {
    const currentTheme = html.classList.contains('dark') ? 'dark' : 'light';
    setTheme(currentTheme === 'dark' ? 'light' : 'dark');
});


// --- Animations on Scroll & Load ---
document.addEventListener('DOMContentLoaded', () => {
    
    // --- Fade-in on Scroll Animation ---
    const sections = document.querySelectorAll('.fade-in-section');

    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    // No longer need to unobserve if we want animations to replay
                    // observer.unobserve(entry.target); 
                }
            });
        }, {
            root: null,
            threshold: 0.1, 
            rootMargin: '0px 0px -50px 0px'
        });

        sections.forEach(section => {
            observer.observe(section);
        });

    } else {
        // Fallback for older browsers
        sections.forEach(section => {
            section.classList.add('is-visible');
        });
    }

    // --- Infinite Scroller Accessibility (NEW) ---
    const scroller = document.querySelector('.scroller-inner');
    
    if (scroller) {
        const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
        
        const handleMotionChange = () => {
            if (mediaQuery.matches) {
                scroller.style.animationPlayState = 'paused';
            } else {
                scroller.style.animationPlayState = 'running';
            }
        };
        
        // Check on load
        handleMotionChange();
        
        // Listen for changes
        mediaQuery.addEventListener('change', handleMotionChange);
    }
});