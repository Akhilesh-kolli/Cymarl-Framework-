import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

log_dir = Path("logs")

attacker_file = log_dir / "attacker_monitor.csv"
defender_file = log_dir / "defender_monitor.csv"

if not attacker_file.exists():
    raise FileNotFoundError("Attacker log missing")

if not defender_file.exists():
    raise FileNotFoundError("Defender log missing")

# SB3 monitor files contain header comments
attacker = pd.read_csv(attacker_file, comment="#")
defender = pd.read_csv(defender_file, comment="#")

# Rolling averages smooth the curve
attacker["smooth"] = attacker["r"].rolling(window=20).mean()
defender["smooth"] = defender["r"].rolling(window=20).mean()

# ---- Plot attacker ----
plt.figure(figsize=(8,5))
plt.plot(attacker["r"], alpha=0.3, label="Episode reward")
plt.plot(attacker["smooth"], label="Smoothed reward")
plt.title("Attacker Training Reward Curve")
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.legend()
plt.grid()
plt.savefig("attacker_training.png")
plt.show()

# ---- Plot defender ----
plt.figure(figsize=(8,5))
plt.plot(defender["r"], alpha=0.3, label="Episode reward")
plt.plot(defender["smooth"], label="Smoothed reward")
plt.title("Defender Training Reward Curve")
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.legend()
plt.grid()
plt.savefig("defender_training.png")
plt.show()

print("\n✅ Saved:")
print(" - attacker_training.png")
print(" - defender_training.png")
