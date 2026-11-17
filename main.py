import os

PLAN = (
    "Day 0 starts an autonomous AI agent with $100, internet, and zero human labor; goal: maximize day 30 funds. "
    "Venture focus: business-to-business artificial intelligence video advertisements for Shopify merchants. "
    "Cost structure: ninety-nine dollars paid upfront secures a trio of fifteen-second promotional clips. "
    "Outreach: find 200 Shopify shops missing video, make a free 15-second sample ad from store photos, email owner. "
    "Delivery: paid orders fulfilled in 24 hours via AI video APIs. "
    "Cost cap: total API expenses capped at $60. "
    "Upsell: $249/month ad pack. "
    "Kill rule: halt underperforming outreach after 7 days. "
    "Outcome: 6 to 10 paid orders from 200 leads, $594-$990 revenue, minus $60 costs equals $534-$930 net profit. "
    "Edge: AI crafts pro ads in minutes for $2 versus $500+ and weeks for human agencies; free sample proves value prior to payment."
)

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, "entry.txt")
    encoded = PLAN.encode("utf-8")
    with open(out_path, "wb") as f:
        f.write(encoded)
    print(f"Character count: {len(PLAN)}")
    print(f"Byte size: {len(encoded)}")

if __name__ == "__main__":
    main()
