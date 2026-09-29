$cards = @"
                    <!-- Card 1: Tri-Mobility -->
                    <div class="achievement-card rounded-3xl bg-zinc-100 dark:bg-zinc-900 overflow-hidden shadow-xl transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
                        <div class="w-full h-56 bg-zinc-200 dark:bg-zinc-800">
                            <img src="./images/achievements/nsrit-trimobility.png" alt="Tri-Mobility Hackathon First Prize" class="w-full h-full object-cover">
                        </div>
                        <div class="p-6">
                            <h3 class="text-2xl font-bold mb-2">Tri-Mobility Hackathon 2026 — 1st Prize 🏆</h3>
                            <p class="text-zinc-600 dark:text-zinc-400">Secured 1st Place in the IoT Domain among 80+ teams at NSRIT's Tri-Mobility Hackathon. Developed "AI-Powered Smart Guardian"</p>
                        </div>
                    </div>

                    <!-- Card 2: AURAX 2K26 -->
                    <div class="achievement-card rounded-3xl bg-zinc-100 dark:bg-zinc-900 overflow-hidden shadow-xl transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
                        <div class="w-full h-56 bg-zinc-200 dark:bg-zinc-800">
                            <img src="./images/achievements/aurax-ai.png" alt="AURAX AI Innovation Challenge" class="w-full h-full object-cover">
                        </div>
                        <div class="p-6">
                            <h3 class="text-2xl font-bold mb-2">AURAX 2K26 AI Innovation Challenge — 3rd Prize 🥉</h3>
                            <p class="text-zinc-600 dark:text-zinc-400">AI-powered intelligent safety platform capable of detecting falls, accidents, and emergencies in real-time while sending instant alerts through SMS.</p>
                        </div>
                    </div>

                    <!-- Card 3: Nexus AI -->
                    <div class="achievement-card rounded-3xl bg-zinc-100 dark:bg-zinc-900 overflow-hidden shadow-xl transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
                        <div class="w-full h-56 bg-zinc-200 dark:bg-zinc-800">
                            <img src="./images/achievements/nexus-ai-au100.png" alt="Andhra University Centenary Project Showcase" class="w-full h-full object-cover">
                        </div>
                        <div class="p-6">
                            <h3 class="text-2xl font-bold mb-2">Andhra University Centenary Project Showcase</h3>
                            <p class="text-zinc-600 dark:text-zinc-400">Presented Nexus AI during the 100-Year Centenary Celebrations of Andhra University.</p>
                        </div>
                    </div>

                    <!-- Card 4: Green Spark -->
                    <div class="achievement-card rounded-3xl bg-zinc-100 dark:bg-zinc-900 overflow-hidden shadow-xl transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
                        <div class="w-full h-56 bg-zinc-200 dark:bg-zinc-800">
                            <img src="./images/achievements/green-spark.png" alt="Green Spark Ideathon Award" class="w-full h-full object-cover">
                        </div>
                        <div class="p-6">
                            <h3 class="text-2xl font-bold mb-2">Green Spark Ideathon 1.0 — First Prize</h3>
                            <p class="text-zinc-600 dark:text-zinc-400">Competition for sustainability solutions (Ecodharma project).</p>
                        </div>
                    </div>

                    <!-- Card 5: Spark Nation -->
                    <div class="achievement-card rounded-3xl bg-zinc-100 dark:bg-zinc-900 overflow-hidden shadow-xl transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
                        <div class="w-full h-56 bg-zinc-200 dark:bg-zinc-800">
                            <img src="./images/achievements/spark-nation.png" alt="Spark Nation Hackathon Award" class="w-full h-full object-cover">
                        </div>
                        <div class="p-6">
                            <h3 class="text-2xl font-bold mb-2">Spark Nation Hackathon — Third Prize</h3>
                            <p class="text-zinc-600 dark:text-zinc-400">Created an AI bot that watches children for dangers and hazard risks.</p>
                        </div>
                    </div>

                    <!-- Card 6: IT Hackathon -->
                    <div class="achievement-card rounded-3xl bg-zinc-100 dark:bg-zinc-900 overflow-hidden shadow-xl transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
                        <div class="w-full h-56 bg-zinc-200 dark:bg-zinc-800">
                            <img src="./images/achievements/it-hackathon.png" alt="IT Hackathon Award" class="w-full h-full object-cover">
                        </div>
                        <div class="p-6">
                            <h3 class="text-2xl font-bold mb-2">IT Hackathon — Second Runner-Up</h3>
                            <p class="text-zinc-600 dark:text-zinc-400">Built an innovative software application under time constraints.</p>
                        </div>
                    </div>

                    <!-- Card 7: Smart India -->
                    <div class="achievement-card rounded-3xl bg-zinc-100 dark:bg-zinc-900 overflow-hidden shadow-xl transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
                        <div class="w-full h-56 bg-zinc-200 dark:bg-zinc-800">
                            <img src="./images/achievements/sih.png" alt="Smart India Hackathon Award" class="w-full h-full object-cover">
                        </div>
                        <div class="p-6">
                            <h3 class="text-2xl font-bold mb-2">Smart India Hackathon — Consolation</h3>
                            <p class="text-zinc-600 dark:text-zinc-400">Developed an AI-powered waste management system.</p>
                        </div>
                    </div>

                    <!-- Card 8: National Hackathon -->
                    <div class="achievement-card rounded-3xl bg-zinc-100 dark:bg-zinc-900 overflow-hidden shadow-xl transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
                        <div class="w-full h-56 bg-zinc-200 dark:bg-zinc-800">
                            <img src="./images/achievements/national-hackathon.png" alt="National Hackathon Award" class="w-full h-full object-cover">
                        </div>
                        <div class="p-6">
                            <h3 class="text-2xl font-bold mb-2">24-Hour National-level Hackathon — Consolation</h3>
                            <p class="text-zinc-600 dark:text-zinc-400">Recognized for creativity and problem-solving in a competitive environment.</p>
                        </div>
                    </div>
"@

$newContent = $cards + "`n" + $cards

# Replace content in index.html
$indexContent = Get-Content -Path "index.html" -Raw

$startTag = '<div class="scroller-inner">'
$endTag = '</section>'
$startIndex = $indexContent.IndexOf($startTag) + $startTag.Length
$endIndex = $indexContent.IndexOf($endTag, $startIndex)

# The ending of the scroller is actually marked by the closing </div> of scroller-inner, then closing </div> of scroller-container.
# Let's be more precise.
$regex = '(?s)<div class="scroller-inner">.*?</div>\s*</div>\s*</section>'
$replacement = "<div class=`"scroller-inner`">`n$newContent`n                </div>`n            </div>`n        </section>"
$newIndexContent = $indexContent -replace $regex, $replacement

Set-Content -Path "index.html" -Value $newIndexContent -Encoding UTF8
