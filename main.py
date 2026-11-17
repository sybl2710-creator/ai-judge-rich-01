import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "30-Day Plan: Turn $100 into max capital via B2B AI Shopify video ads.",
        "Edge: AI creates pro ads in minutes for $2 vs human agencies charging $500+ taking weeks. Free sample proves value before payment.",
        "Day 1: Launch landing page offering 3x15-second Shopify product ads for $99 upfront.",
        "Days 2-5: Find 200 Shopify stores lacking video, generate a free 15-sec sample from store photos, email owners.",
        "Days 6-30: Deliver paid orders in 24 hours via AI video APIs. Cap API costs at $60. Push $249 monthly upsell pack. Apply 7-day kill rule on underperforming outreach.",
        "Expected Money: 6-10 paid orders from 200 leads = $594-$990 revenue minus $60 costs = $534-$930 net profit.",
    ]
)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
