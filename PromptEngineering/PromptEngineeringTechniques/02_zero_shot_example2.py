from llm_helper import llm_model

# 1. Movie review classification
review_prompt = """Classify the following movie review as positive or negative:
'The plot was predictable and the acting felt wooden, but the visuals were stunning.'

Classification:
"""

# 2. Summarization
summary_prompt = """Summarize the following paragraph in one sentence:
'Climate change refers to long-term shifts in temperatures and weather patterns.
Human activities, especially the burning of fossil fuels, have been the main driver
since the 1800s, producing heat-trapping gases that warm the planet and lead to
rising sea levels, extreme weather, and ecosystem disruption.'

Summary:
"""

# 3. Translation
translation_prompt = """Translate this English phrase to Spanish:
'Where is the nearest train station?'

Spanish translation:
"""

for name, p in [("review", review_prompt),
                ("summary", summary_prompt),
                ("translation", translation_prompt)]:
    print(f"=== {name.upper()} ===")
    print(llm_model(p), "\n")