# Cymarl-Framework

<p align="center">
  <img src="https://img.shields.io/badge/SIEM-Splunk-blue">
  <img src="https://img.shields.io/badge/Endpoint-Sysmon-brightgreen">
  <img src="https://img.shields.io/badge/Attack-Simulation-orange">
  <img src="https://img.shields.io/badge/Kali-Linux-red">
  <img src="https://img.shields.io/badge/Logs-Windows_Event_Logs-yellow">
  <img src="https://img.shields.io/badge/MARL-PPO-purple">
  <img src="https://img.shields.io/badge/Framework-Cybersecurity-darkblue">
</p>

---

# Cybersecurity Multi-Agent Reinforcement Learning Framework

A research-oriented Cyber MARL framework designed for attacker–defender simulations in enterprise-like environments using reinforcement learning, PPO training, and cybersecurity event analysis.

This project simulates adversarial cyber behavior where intelligent agents interact dynamically in a monitored network environment. The framework supports attack simulation, defense response analysis, reward engineering, and visualization of training metrics.

---

# Features

- Multi-Agent Reinforcement Learning (MARL)
- PPO-based training architecture
- Attacker vs Defender cyber simulation
- Reward engineering and policy optimization
- Network attack emulation
- Training metric generation
- GIF-based simulation visualization
- Security event logging and monitoring
- Splunk and Sysmon integration concepts
- Cyber attack path experimentation

---

# Technologies Used

| Category | Technologies |
|---|---|
| Programming | Python |
| RL Framework | PPO |
| Visualization | Matplotlib |
| Security Monitoring | Splunk |
| Endpoint Monitoring | Sysmon |
| Environment | Kali Linux |
| Data Handling | NumPy, Pandas |
| Logging | Windows Event Logs |

---

# Project Architecture

```text
Attacker Agent
       ↓
Attack Simulation Environment
       ↓
Defender Agent
       ↓
Reward Calculation
       ↓
PPO Training Loop
       ↓
Metrics & Visualization
