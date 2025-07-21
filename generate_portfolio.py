import pandas as pd
import matplotlib.pyplot as plt

# CapEx data
capex_data = {
    "Component": [
        "Basic Data Center Buildout (per MW)",
        "High-Density GPU Racks (per rack)",
        "Power & Cooling (Liquid/Direct)",
        "Network Infrastructure (Infiniband/10/100GbE)"
    ],
    "Estimated Cost (USD)": [
        "8M - 15M",
        "200K - 400K",
        "30–40% of total CapEx",
        "1M–3M"
    ]
}

# OpEx data
opex_data = {
    "Category": [
        "Power",
        "Staffing & Ops",
        "Cooling Maintenance",
        "Hardware Refresh",
        "Support Software Licenses"
    ],
    "Range / Unit": [
        "$0.10–$0.15 per kWh",
        "$500K–$1M annually per site",
        "$100K–$300K annually",
        "Every 3–5 years (~20% annualized)",
        "Varies (open source or vendor support)"
    ]
}

# Cloud vs On-Prem GPU cost
cloud_vs_onprem = {
    "Platform": ["AWS / Azure / GCP", "Dedicated On-Prem", "Shared Community Model (NCShare-like)"],
    "Cost per GPU Hour (USD)": [3.5, 1.15, 0.8]
}

# Create DataFrames
capex_df = pd.DataFrame(capex_data)
opex_df = pd.DataFrame(opex_data)
cloud_vs_onprem_df = pd.DataFrame(cloud_vs_onprem)

# Plot Cloud vs On-Prem GPU cost
plt.figure(figsize=(6, 4))
plt.bar(cloud_vs_onprem_df["Platform"], cloud_vs_onprem_df["Cost per GPU Hour (USD)"])
plt.title("Cloud vs On-Prem GPU Cost Comparison")
plt.ylabel("Cost per GPU Hour (USD)")
plt.xticks(rotation=15, ha='right')
plt.tight_layout()
plt.savefig("cloud_vs_onprem_cost.png")
plt.close()

# Institutional Investments
institutions = [
    "University of Florida",
    "MIT Schwarzman College",
    "SDSC (Expanse)",
    "MGHPCC",
    "University of Tennessee + Oak Ridge"
]
investments = [70, 1000, 11.5, 90, 600]

plt.figure(figsize=(8, 5))
plt.bar(institutions, investments)
plt.title("Institutional AI Center Investments (in Millions USD)")
plt.ylabel("Investment (Million USD)")
plt.xticks(rotation=20, ha='right')
plt.tight_layout()
plt.savefig("institutional_investments.png")
plt.close()

print("Portfolio files (README and graphs) will be generated.")
