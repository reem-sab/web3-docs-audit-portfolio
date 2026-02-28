# Documentation Audit Methodology

This document describes the framework used to evaluate the Sui Network documentation as part of a Developer Experience (DX) audit.

-----

## Framework: Diátaxis

This audit applies the [Diátaxis framework](https://diataxis.fr/) as its structural foundation. Diátaxis organizes documentation into four distinct content types, each serving a different user need:

|Content Type    |User Need         |Question It Answers                  |
|----------------|------------------|-------------------------------------|
|**Tutorial**    |Learning          |“Help me get started.”               |
|**How-to Guide**|Completing a task |“Help me accomplish a specific goal.”|
|**Reference**   |Information lookup|“What does this do?”                 |
|**Explanation** |Understanding     |“Why does this work this way?”       |

Mixing these content types — or omitting them entirely — is one of the most common sources of developer friction. This audit evaluates whether each section of the Sui documentation serves its intended purpose clearly, and flags cases where content types are conflated or missing.

-----

## Audit Pillars

### 1. Findability

**Goal:** Can a developer locate what they need in under 30 seconds?

**Criteria:**

- Consistent heading hierarchy (H1 → H2 → H3)
- Functional and accurate search
- Clear separation of tutorial content from reference material
- Logical information architecture aligned with Diátaxis content types

**Weight:** 20%

-----

### 2. Technical Accuracy

**Goal:** Is the documentation correct and current?

**Criteria:**

- Code samples execute without modification
- Environment-specific instructions (Devnet, Testnet, Mainnet) are clearly differentiated
- CLI installation commands are valid across all major operating systems (macOS Intel, macOS Apple Silicon, Linux, Windows)
- Rate limits, API responses, and error codes reflect the current state of the product

**Weight:** 40%

-----

### 3. Time-to-Hello-World

**Goal:** How long does it take a new developer to complete their first successful transaction?

**Criteria:**

- Friction points in the onboarding path are identified and documented
- Prerequisites are stated upfront, not discovered mid-tutorial
- Gas requirements and Object-centric architecture concepts are introduced before they are needed, not after
- The happy path is unambiguous

**Weight:** 20%

-----

### 4. Voice & Terminology

**Goal:** Does the documentation communicate with clarity and consistency?

**Criteria:**

- Active voice is used throughout
- Terminology is consistent (e.g., “Objects” vs. “Assets” — one term, used everywhere)
- Alienating language is avoided: words like “just,” “simply,” and “easy” are flagged, as they create friction for developers who are struggling
- Tone is authoritative without being condescending

**Weight:** 20%

-----

## Scoring Rubric

Each pillar is scored on a 1–5 scale:

|Score|Meaning                                                  |
|-----|---------------------------------------------------------|
|5    |Excellent — meets or exceeds best practices              |
|4    |Good — minor gaps, no meaningful friction                |
|3    |Acceptable — noticeable gaps that affect usability       |
|2    |Poor — significant friction or inaccuracies present      |
|1    |Critical — blocking issues that prevent developer success|

-----

## Tooling

|Tool                                 |Purpose                                                     |
|-------------------------------------|------------------------------------------------------------|
|Python (`BeautifulSoup4`, `Requests`)|Automated link validation and detection of information decay|
|GitHub Issues                        |Cataloging and prioritizing documentation gaps              |
|GitHub Projects (Kanban)             |Managing audit lifecycle and sprint progress                |
|Markdown                             |Authoring audit reports and recommendations                 |

-----

## What This Audit Does Not Cover

- **Marketing content** — landing pages and promotional copy are out of scope
- **SDK internals** — code correctness beyond what documentation claims
- **Community content** — Discord, forums, and third-party tutorials

-----

*Methodology authored by Reem Sabawi. Framework credit: [Diátaxis](https://diataxis.fr/) by Daniele Procida.*
