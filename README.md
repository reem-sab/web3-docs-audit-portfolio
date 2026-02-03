# Web3 Documentation Audit & DX Strategy: Sui Network

## Project Overview
This repository serves as a comprehensive **Developer Experience (DX) Audit** of the Sui Network documentation. As a Technical Writer and Project Manager, I have identified strategic documentation gaps that create friction for new developers and proposed actionable solutions to reduce "Time-to-Hello-World."

### Key Objectives:
* **Audit Methodology:** Applied the **Diátaxis framework** to evaluate content usability.
* **Issue Tracking:** Managed a backlog of technical blockers and documentation "debt" using GitHub Projects.
* **Technical Automation:** Integrated Python-based link checking to ensure information integrity.

---

## Project Management & Strategy
I have organized this audit as a managed sprint. You can view the live progress here: 
👉 **https://github.com/users/reem-sab/projects/1/views/1**

### Scoring Rubric
I evaluated the current documentation state against the following criteria:

| Category | Impact | Weight |
| :--- | :--- | :--- |
| **Code Accuracy** | High (Blockers) | 40% |
| **Navigability** | Medium (Friction) | 20% |
| **Conceptual Clarity** | High (Retention) | 20% |
| **Visual/Tooling** | Low (Polish) | 20% |

---

## Top Audit Findings (The Backlog)
Below are the primary "Documentation Gaps" identified during this sprint. Each issue includes a proposed technical fix.

1. **[Critical] Faucet Rate Limit Transparency:** New users face "Too Many Requests" errors due to undocumented cooldown periods.
2. **[Major] M1/M2 Mac CLI Pathing:** Installation guides lack specific shell environment configurations for Apple Silicon.
3. **[Strategy] EVM-to-Sui Glossary:** A missing conceptual bridge for Ethereum developers transitioning to Sui’s Object-centric model.

---

## Technical Tooling
To support the manual audit, I utilized Python to automate the detection of "Information Decay" (broken links).

**Tools used:**
* `Python 3.12`
* `BeautifulSoup4` & `Requests` (for web scraping/link validation)
* `Git` (for version control and collaboration)

---

## Impact Analysis
By addressing these issues, a Web3 protocol can expect:
* **Higher Dev Retention:** Reduced abandonment during the "Getting Started" phase.
* **Lower Support Overhead:** Fewer repetitive questions in Discord/Telegram regarding installation and faucets.
* **Faster Ecosystem Growth:** Lowering the barrier to entry for Ethereum-native developers.
