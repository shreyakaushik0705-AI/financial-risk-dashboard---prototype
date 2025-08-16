import pandas as pd

def generate_summary(data):
    # placeholder summary
    return "Financial summary generated"

def calculate_risk_score(data):
    # dummy risk score logic
    return 42

if __name__ == "__main__":
    sample_data = pd.DataFrame({"Revenue":[100,150,200]})
    summary = generate_summary(sample_data)
    score = calculate_risk_score(sample_data)
    print("Summary:", summary)
    print("Risk Score:", score)
