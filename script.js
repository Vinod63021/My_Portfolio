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

    // --- Infinite Scroller Accessibility (REMOVED) ---
    // The OS reduced-motion check was removed because it disabled the scroll for some users unexpectedly.
});

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

});


// ============================================================
//  Antigravity Mouse Bubble Effect
//  – Vanilla JS, plain-HTML portfolio edition
//  – Fully self-contained, zero dependencies
// ============================================================
(function () {
  'use strict';

  // ── Disable on touchscreens / mobile ──────────────────────
  if (window.matchMedia('(pointer: coarse)').matches) return;

  // ── Palette – tweak these to match your brand ─────────────
  var BUBBLE_COLORS = [
    '#4285F4', // Google Blue
    '#EA4335', // Google Red
    '#FBBC04', // Google Yellow
    '#34A853', // Google Green
    '#A142F4', // Pastel Purple
    '#00BCD4', // Cyan accent
  ];

  // ── Canvas setup ──────────────────────────────────────────
  var canvas = document.getElementById('bubble-canvas');
  if (!canvas) return;

  var ctx = canvas.getContext('2d');

  function resizeCanvas() {
    canvas.width  = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resizeCanvas();
  window.addEventListener('resize', resizeCanvas, { passive: true });

  // ── Particle pool ─────────────────────────────────────────
  var particles   = [];
  var lastSpawn   = 0;
  var SPAWN_MS    = 40;   // spawn interval in milliseconds
  var MAX_BUBBLES = 20;   // hard cap on simultaneous bubbles

  // ── Mouse tracking ────────────────────────────────────────
  var mouseX = -500;
  var mouseY = -500;

  window.addEventListener('mousemove', function (e) {
    mouseX = e.clientX;
    mouseY = e.clientY;

    // Throttled spawn
    var now = performance.now();
    if (now - lastSpawn > SPAWN_MS && particles.length < MAX_BUBBLES) {
      lastSpawn = now;
      particles.push({
        x:     e.clientX,
        y:     e.clientY,
        size:  Math.random() * 4 + 2.5,           // radius 2.5–6.5 px
        color: BUBBLE_COLORS[Math.floor(Math.random() * BUBBLE_COLORS.length)],
        vx:    (Math.random() - 0.5) * 1.2,       // gentle horizontal sway
        vy:    (Math.random() - 0.5) * 1.2 - 0.45, // upward antigravity drift
        alpha: 0.8,
      });
    }
  }, { passive: true });

  // ── Physics + render loop ─────────────────────────────────
  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    var alive = [];
    for (var i = 0; i < particles.length; i++) {
      var p = particles[i];

      // Physics step
      p.x    += p.vx;
      p.y    += p.vy;
      p.alpha -= 0.022; // fade speed – lower = longer trail

      if (p.alpha > 0.01) {
        // Draw bubble
        ctx.save();
        ctx.globalAlpha = p.alpha;
        ctx.fillStyle   = p.color;
        ctx.shadowColor = p.color;
        ctx.shadowBlur  = 6;          // subtle glow halo around each bubble
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
        alive.push(p);
      }
    }
    particles = alive;

    requestAnimationFrame(animate);
  }

  requestAnimationFrame(animate);
})();
