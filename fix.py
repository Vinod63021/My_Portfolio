import re

def fix_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # The cards are defined between <div class="scroller-inner"> and its closing </div>
    # Let's extract the first 8 cards.
    
    # We will just write out the 8 cards properly
    cards = """
                    <div class="achievement-card rounded-3xl bg-zinc-100 dark:bg-zinc-900 overflow-hidden shadow-xl transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
                        <div class="w-full h-56 bg-zinc-200 dark:bg-zinc-800">
                            <img src="./images/achievements/nsrit-trimobility.png"
                                 alt="Tri-Mobility Hackathon First Prize"
                                 class="w-full h-full object-cover">
                        </div>
                        <div class="p-6">
                            <h3 class="text-2xl font-bold mb-2">
                                Tri-Mobility Hackathon 2026 — 1st Prize 🏆
                            </h3>
                            <p class="text-zinc-600 dark:text-zinc-400">
                                Secured 1st Place in the IoT Domain among 80+ teams at NSRIT's Tri-Mobility Hackathon. Developed "AI-Powered Smart Guardian"
                            </p>
                        </div>
                    </div>

                    <div class="achievement-card rounded-3xl bg-zinc-100 dark:bg-zinc-900 overflow-hidden shadow-xl transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
                        <div class="w-full h-56 bg-zinc-200 dark:bg-zinc-800">
                            <img src="./images/achievements/aurax-ai.png"
                                 alt="AURAX AI Innovation Challenge"
                                 class="w-full h-full object-cover">
                        </div>
                        <div class="p-6">
                            <h3 class="text-2xl font-bold mb-2">
                                AURAX 2K26 AI Innovation Challenge — 3rd Prize 🥉
                            </h3>
                            <p class="text-zinc-600 dark:text-zinc-400">
                                AI-powered intelligent safety platform capable of detecting falls, accidents, and emergencies in real-time while sending instant alerts through SMS.
                            </p>
                        </div>
                    </div>

                    <div class="achievement-card rounded-3xl bg-zinc-100 dark:bg-zinc-900 overflow-hidden shadow-xl transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
                        <div class="w-full h-56 bg-zinc-200 dark:bg-zinc-800">
                            <img src="./images/achievements/nexus-ai-au100.png"
                                 alt="Andhra University Centenary Project Showcase"
                                 class="w-full h-full object-cover">
                        </div>
                        <div class="p-6">
                            <h3 class="text-2xl font-bold mb-2">
                                Andhra University Centenary Project Showcase
                            </h3>
                            <p class="text-zinc-600 dark:text-zinc-400">
                                Presented Nexus AI during the 100-Year Centenary Celebrations of Andhra University. 
                            </p>
                        </div>
                    </div>
                    
                    <div class="achievement-card rounded-3xl bg-zinc-100 dark:bg-zinc-900 overflow-hidden shadow-xl transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
                        <div class="w-full h-56 bg-zinc-200 dark:bg-zinc-800">
                            <img src="./images/achievements/green-spark.png" alt="Green Spark Ideathon Award" class="w-full h-full object-cover">
                        </div>
                        <div class="p-6">
                            <h3 class="text-2xl font-bold mb-2">Green Spark Ideathon 1.0 — First Prize</h3>
                            <p class="text-zinc-600 dark:text-zinc-400">Competition for sustainability solutions (Ecodharma project). </p>
                        </div>
                    </div>

                    <div class="achievement-card rounded-3xl bg-zinc-100 dark:bg-zinc-900 overflow-hidden shadow-xl transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
                        <div class="w-full h-56 bg-zinc-200 dark:bg-zinc-800">
                            <img src="./images/achievements/spark-nation.png" alt="Spark Nation Hackathon Award" class="w-full h-full object-cover">
                        </div>
                        <div class="p-6">
                            <h3 class="text-2xl font-bold mb-2">Spark Nation Hackathon — Third Prize</h3>
                            <p class="text-zinc-600 dark:text-zinc-400">Created an AI bot that watches children for dangers and hazard risks. </p>
                        </div>
                    </div>

                    <div class="achievement-card rounded-3xl bg-zinc-100 dark:bg-zinc-900 overflow-hidden shadow-xl transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
                        <div class="w-full h-56 bg-zinc-200 dark:bg-zinc-800">
                            <img src="./images/achievements/it-hackathon.png" alt="IT Hackathon Award" class="w-full h-full object-cover">
                        </div>
                        <div class="p-6">
                            <h3 class="text-2xl font-bold mb-2">IT Hackathon — Second Runner-Up</h3>
                            <p class="text-zinc-600 dark:text-zinc-400">Built an innovative software application under time constraints. </p>
                        </div>
                    </div>

                    <div class="achievement-card rounded-3xl bg-zinc-100 dark:bg-zinc-900 overflow-hidden shadow-xl transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
                        <div class="w-full h-56 bg-zinc-200 dark:bg-zinc-800">
                            <img src="./images/achievements/sih.png" alt="Smart India Hackathon Award" class="w-full h-full object-cover">
                        </div>
                        <div class="p-6">
                            <h3 class="text-2xl font-bold mb-2">Smart India Hackathon — Consolation</h3>
                            <p class="text-zinc-600 dark:text-zinc-400">Developed an AI-powered waste management system. </p>
                        </div>
                    </div>
                    
                    <div class="achievement-card rounded-3xl bg-zinc-100 dark:bg-zinc-900 overflow-hidden shadow-xl transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
                        <div class="w-full h-56 bg-zinc-200 dark:bg-zinc-800">
                            <img src="./images/achievements/national-hackathon.png" alt="National Hackathon Award" class="w-full h-full object-cover">
                        </div>
                        <div class="p-6">
                            <h3 class="text-2xl font-bold mb-2">24-Hour National-level Hackathon — Consolation</h3>
                            <p class="text-zinc-600 dark:text-zinc-400">Recognized for creativity and problem-solving in a competitive environment. </p>
                        </div>
                    </div>"""

    new_inner_html = f'<div class="scroller-inner">\n{cards}\n{cards}\n                </div>'
    
    # Replace everything between <div class="scroller-inner"> and the closing </div> of scroller-inner.
    # The original has <div class="scroller-inner"> at line 658 and its closing </div> at line 809.
    pattern = re.compile(r'<div class="scroller-inner">.*?</div>\s*</div>\s*</section>', re.DOTALL)
    
    new_content = pattern.sub(f'{new_inner_html}\n            </div>\n        </section>', content)

    # We also want to remove garbled characters globally if they exist, but since we're using the backup,
    # the backup has correct characters except where it didn't. Wait, the user said the original had garbled chars?
    # No, the user said "see some unwanren cg=haracters are entered why check and correct and reteifi and tjen like ðŸŒŸ whatall this rub okay remove them first okay".
    # This implies the README or index had them originally? Or my edit introduced them?
    # The string they pasted has "ðŸŒŸFinal Year CSE Student @ Andhra University". 
    # That is exactly how GitHub renders a corrupted README, or how their README currently looks!
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

    # Let's fix README.md too!
    with open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
        readme = readme.replace('ðŸŒŸ', '🌟').replace('ðŸ†', '🏆').replace('â€“', '–').replace('ðŸ¥‰', '🥉')
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme)

fix_html()
