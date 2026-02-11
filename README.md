[![ORGAN-VII: Kerygma](https://img.shields.io/badge/ORGAN--VII-Kerygma-6a1b9a?style=flat-square)](https://github.com/organvm-vii-kerygma)
[![Templates](https://img.shields.io/badge/templates-multi--platform-9c27b0?style=flat-square)]()
[![POSSE](https://img.shields.io/badge/POSSE-enabled-blueviolet?style=flat-square)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-6a1b9a?style=flat-square)]()

# Announcement Templates

**A structured template library for all outbound communications across the eight-organ creative-institutional system -- platform-specific formats, tone calibration, variable interpolation, and quality checklists for every announcement type.**

Announcement Templates is the canonical library of reusable communication artifacts for ORGAN-VII (Kerygma), the marketing and distribution organ of the [organvm](https://github.com/organvm-vii-kerygma) ecosystem. Every public-facing message that leaves this system -- whether a Mastodon thread announcing a new essay, a Discord embed promoting a release, or a press release introducing the project to grant reviewers -- originates from or is validated against templates maintained here.

The problem this repository solves is consistency at scale. An eight-organ system spanning 67+ repositories across 8 GitHub organizations produces a continuous stream of announcements: new releases, essay publications, community events, partnership opportunities, grant application supplements, conference submissions, and system-wide milestones. Without a centralized template library, each announcement becomes an ad-hoc composition -- inconsistent in voice, variable in quality, and disconnected from the strategic positioning that makes this system legible to its target audiences.

This repository provides the structured alternative: a template for every announcement type, calibrated for every distribution channel, with built-in quality gates and variable interpolation from the system's machine-readable registry.

---

## Table of Contents

- [Overview](#overview)
- [Target Audiences](#target-audiences)
- [Template Categories](#template-categories)
- [Platform-Specific Formats](#platform-specific-formats)
- [Tone and Voice Guides](#tone-and-voice-guides)
- [Variable Interpolation](#variable-interpolation)
- [Quality Checklists](#quality-checklists)
- [Publishing Calendar Integration](#publishing-calendar-integration)
- [Template Inventory](#template-inventory)
- [Usage Workflow](#usage-workflow)
- [Metrics and Tracking](#metrics-and-tracking)
- [Cross-Organ Dependencies](#cross-organ-dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Author and Contact](#author-and-contact)

---

## Overview

Announcement Templates operates as a content factory floor. Raw inputs -- a new repository reaching DEPLOYED status, a meta-system essay clearing editorial review, a community salon date being confirmed -- enter the template pipeline and emerge as platform-ready communications. The templates themselves are not static boilerplate; they are structured documents with variable slots, conditional sections, tone modifiers, and post-composition checklists that ensure every outbound message meets quality standards.

The library is organized along two axes: **announcement type** (what kind of event is being communicated) and **distribution channel** (where the message will appear). A single event -- say, the publication of a new ORGAN-V essay -- generates multiple template instantiations: a Mastodon thread (segmented into 500-character posts with strategic thread structure), a Discord embed (rich formatting with metadata fields), a potential LinkedIn article (long-form professional framing), and an email newsletter segment (personal tone with context-setting). Each format serves a different audience and respects different platform conventions, but all derive from the same source event and maintain consistent factual content.

### Design Principles

1. **Single Source, Multiple Outputs.** Every announcement begins as a canonical event record. Templates transform that record into channel-specific formats. This prevents factual drift between platforms and ensures that a correction in one place propagates everywhere.

2. **Voice Consistency With Channel Adaptation.** The organvm system has a distinctive voice -- intellectually serious without being academic, technically precise without being exclusionary, strategically aware without being corporate. Templates encode this voice while adapting register for each platform: more conversational on Mastodon, more structured on Discord, more formal in press materials.

3. **Machine-Readable Inputs.** Templates consume data from `registry-v2.json` and the orchestration hub's governance files. Repository names, descriptions, organ assignments, documentation status, and dependency relationships are injected automatically, reducing manual transcription errors and keeping announcements synchronized with the actual state of the system.

4. **Quality Gates Before Publication.** Every template includes a pre-publication checklist. No announcement ships without confirming: factual accuracy (cross-checked against registry), link validity (all URLs tested), tone compliance (reviewed against voice guide), platform format compliance (character limits, embed constraints), and strategic alignment (does this announcement serve the current phase's goals?).

---

## Target Audiences

Understanding who receives these announcements determines every template design decision. The organvm system targets five distinct audience segments, each with different information needs, attention patterns, and credibility markers.

### Academic Researchers and Theorists

Researchers in digital humanities, computational creativity, media studies, and systems theory represent the intellectual core audience. They evaluate work based on conceptual rigor, citation of relevant literature, methodological transparency, and contribution to ongoing scholarly conversations. Announcements targeting this segment emphasize the theoretical frameworks underlying the system (recursive ontology, rhizomatic coordination, stigmergic communication models), reference relevant thinkers and traditions, and position deliverables within research contexts. Tone: precise, substantive, respectful of disciplinary conventions.

### Grant Reviewers and Funding Bodies

Program officers at foundations (Knight, Mellon, NEA, NSF) and fellowship committees assess organizational capacity, sustainability planning, community impact, and alignment with funding priorities. They read quickly, evaluate against rubrics, and look for evidence of professional infrastructure. Announcements targeting this segment lead with outcomes and impact, demonstrate institutional maturity (governance structures, quality processes, documentation standards), and connect individual deliverables to broader systemic goals. Tone: confident, evidence-oriented, outcome-focused.

### Hiring Managers and Technical Recruiters

Engineering managers, CTO offices, and technical recruiters evaluating portfolio evidence look for production-quality code, architectural reasoning, testing discipline, and systems thinking at scale. Announcements targeting this segment emphasize technical sophistication (test counts, coverage metrics, architecture decisions, scalability characteristics), demonstrate real engineering work (not toy projects), and position the eight-organ system as evidence of extraordinary organizational capacity. Tone: technically specific, results-oriented, pragmatic.

### Fellow Artists and Creative Technologists

Practitioners working at the intersection of art and technology -- generative artists, creative coders, interactive designers, performance technologists -- evaluate work based on aesthetic ambition, technical craft, conceptual depth, and community contribution. Announcements targeting this segment foreground the creative vision, share process insights (building in public), and invite participation and collaboration. Tone: collegial, exploratory, generous with knowledge.

### Open Source Community

Developers, contributors, and users of open-source tools evaluate projects based on code quality, documentation completeness, maintainer responsiveness, and community health. Announcements targeting this segment follow open-source communication conventions (changelogs, release notes, migration guides), emphasize contribution pathways, and demonstrate commitment to sustainable maintenance. Tone: direct, inclusive, technically clear.

---

## Template Categories

### Launch Announcements

Used when a repository, organ, or system-wide milestone reaches a deployment threshold. Launch templates are the highest-stakes communications in the library -- they establish first impressions and set expectations for everything that follows.

**Included templates:**
- **Repository Launch** -- announces a single repo reaching DEPLOYED status. Includes: repo name, organ assignment, description, key technical highlights, link to README, link to org profile. Conditional sections for flagship vs. standard tier.
- **Organ Launch** -- announces an entire organ reaching operational status. Includes: organ name and domain, repository count, flagship highlights, portfolio angle, governance status. Used during system-wide launch coordination.
- **System Milestone** -- announces cross-organ achievements (all 8 organs operational, validation complete, 100K words deployed). Includes: quantitative metrics, timeline narrative, strategic framing for portfolio audiences.

### Release Notes

Used when existing repositories ship significant updates, new features, or breaking changes. Release note templates follow semantic versioning conventions and include structured sections for additions, changes, deprecations, and migration instructions.

**Included templates:**
- **Feature Release** -- new capability added to an existing repo. Structured: summary, motivation, technical approach, usage examples, testing evidence, upgrade path.
- **Bug Fix Release** -- targeted fix for a reported issue. Structured: issue reference, root cause, fix description, affected versions, verification steps.
- **Breaking Change Release** -- updates that require consumer action. Structured: what changed, why, migration instructions (step-by-step), deprecation timeline, support resources.

### Essay Promotion

Used when ORGAN-V (Public Process) publishes new essays on the Jekyll/GitHub Pages site. Essay promotion templates are critical to the POSSE workflow -- they drive traffic from social platforms back to the canonical publication site.

**Included templates:**
- **Essay Announcement** -- standard promotion for a new essay. Includes: title, thesis statement (one sentence), key arguments (bullet points), word count, reading time estimate, canonical URL, author attribution.
- **Essay Series Update** -- announces a new entry in an ongoing series. Includes: series context, previous entries (with links), how this entry advances the argument, canonical URL.
- **Essay Highlight** -- re-promotes an existing essay for a new context (relevant conference, related news event, grant deadline alignment). Includes: original publication date, relevance hook, canonical URL.

### Community Event Invitations

Used for ORGAN-VI (Koinonia) community events -- salons, reading groups, workshops, collaborative sessions.

**Included templates:**
- **Salon Announcement** -- structured invitation with: topic, date/time (with timezone), format (synchronous/asynchronous), preparation materials, participation guidelines, RSVP mechanism.
- **Reading Group Session** -- announces a reading group meeting with: selected text, discussion questions, facilitator, logistics.
- **Workshop/Sprint** -- announces a collaborative working session with: objective, prerequisites, expected outcomes, contribution recognition.

### Press and Institutional Communications

Formal communications for external institutional audiences -- press releases, partnership announcements, grant supplements.

**Included templates:**
- **Press Release** -- standard press release format (headline, dateline, lead paragraph, body, boilerplate, contact). Calibrated for arts/technology media outlets.
- **Partnership Announcement** -- announces collaborations with other organizations, institutions, or communities.
- **Grant Supplement** -- supplementary material for grant applications that references the organvm system as evidence of institutional capacity.

---

## Platform-Specific Formats

### Mastodon (Primary Social Channel)

Mastodon's 500-character limit and thread-based conversation model require careful segmentation. Templates for Mastodon follow these structural rules:

- **Thread architecture:** Opening post establishes the hook (what and why). Subsequent posts deliver detail. Final post provides the canonical link and call to action. Thread length: 3-7 posts depending on announcement type.
- **Character budgeting:** Each post reserves 30 characters for the thread indicator (e.g., "1/5") and 23 characters for a hashtag block. Effective content budget: ~447 characters per post.
- **Hashtag strategy:** Maximum 3 hashtags per post, drawn from a controlled vocabulary: `#CreativeTech`, `#OpenSource`, `#GenerativeArt`, `#BuildingInPublic`, `#DigitalHumanities`, `#SystemsThinking`, organ-specific tags.
- **Alt text requirements:** All images include descriptive alt text. Screenshots of code or architecture diagrams include text-equivalent summaries.
- **Content warnings:** Used appropriately for long threads (CW: long thread, 5 posts) to respect timeline etiquette.

### Discord (Community Channel)

Discord embeds provide rich formatting with structured metadata fields. Templates for Discord use the embed specification:

- **Embed structure:** Title (announcement headline), description (2-3 sentence summary), color (organ-specific hex -- ORGAN-VII uses `#6a1b9a`), fields (key-value metadata pairs), footer (timestamp and organ attribution), thumbnail (organ badge or repo logo).
- **Field conventions:** Fields include: Organ, Repository, Status, Links. Additional fields vary by announcement type.
- **Channel targeting:** Templates specify which Discord channel receives each announcement type (general, announcements, releases, community-events).
- **Mention policy:** Templates indicate when `@everyone` or role mentions are appropriate (system milestones only) vs. when they should be avoided (routine updates).

### LinkedIn (Professional Visibility)

LinkedIn articles and posts serve the hiring manager and grant reviewer audiences. Templates for LinkedIn adopt professional register:

- **Post format:** 1,300-character posts for standard announcements. Long-form articles (1,500-2,500 words) for system milestones and essay re-publications.
- **Professional framing:** Every announcement connects to professional competencies: systems architecture, project management, technical writing, open-source stewardship.
- **Media attachments:** Architecture diagrams, metric dashboards, and progress visualizations enhance professional credibility.

### Email Newsletter

Newsletter templates serve subscribers who prefer consolidated updates over real-time social feeds:

- **Digest format:** Weekly or biweekly compilation of announcements, organized by organ.
- **Personal tone:** Newsletter voice is slightly more informal and reflective than social posts -- it speaks directly to the reader, acknowledges the journey, and provides context that social posts cannot.
- **Sections:** Featured announcement, organ roundup, upcoming events, reading recommendations, metrics snapshot.

---

## Tone and Voice Guides

### System-Wide Voice Principles

The organvm system speaks with a voice that is **intellectually serious without being academic**, **technically precise without being exclusionary**, and **strategically aware without being corporate**. Every template encodes these three tensions.

- **Intellectual seriousness** means: claims are substantiated, frameworks are named and attributed, complexity is respected rather than flattened. We do not simplify for simplification's sake.
- **Technical precision** means: numbers are specific (not "many tests" but "1,312 tests passing"), architectures are described accurately, limitations are acknowledged honestly.
- **Strategic awareness** means: every announcement serves a purpose beyond information transmission. We are building a portfolio, establishing credibility, and inviting participation. Templates encode this intentionality.

### Organ-Specific Voice Modifiers

Each organ has a tonal register that reflects its domain:

| Organ | Voice Modifier | Example Register |
|-------|---------------|------------------|
| I (Theory) | Contemplative, precise | "The recursive engine demonstrates that..." |
| II (Art) | Evocative, process-oriented | "This work explores the space between..." |
| III (Commerce) | Pragmatic, results-oriented | "The system processes 10K records/second..." |
| IV (Orchestration) | Architectural, systematic | "Governance rules ensure that..." |
| V (Public Process) | Reflective, narrative | "Building this in public means..." |
| VI (Community) | Warm, invitational | "Join us for a conversation about..." |
| VII (Marketing) | Strategic, audience-aware | "This positions the system as..." |
| VIII (Meta) | Integrative, panoramic | "Across all eight organs..." |

### Anti-Patterns

Templates include explicit anti-pattern warnings to prevent voice degradation:

- **No hype language.** Never use "revolutionary", "game-changing", "disrupting". The work speaks for itself.
- **No false modesty.** Do not undersell genuine achievements. "A comprehensive eight-organ system" is accurate, not boastful.
- **No jargon without context.** Technical terms are fine; undefined acronyms are not.
- **No platform-native cringe.** Do not adopt platform-specific promotional language (LinkedIn buzzwords, Twitter engagement-bait patterns).

---

## Variable Interpolation

Templates use a mustache-style interpolation syntax that draws values from the system's machine-readable data sources:

```
{{ repo.name }}           -- Repository name from registry-v2.json
{{ repo.description }}    -- Repository description
{{ repo.organ }}          -- Organ assignment (e.g., "ORGAN-III")
{{ repo.organ_name }}     -- Organ name (e.g., "Ergon")
{{ repo.status }}         -- Current status (ACTIVE, DEPLOYED, etc.)
{{ repo.word_count }}     -- README word count
{{ repo.tier }}           -- Tier (flagship, standard, stub)
{{ organ.repo_count }}    -- Number of repos in the organ
{{ system.total_repos }}  -- Total repos across all organs
{{ system.total_words }}  -- Total words deployed
{{ system.launch_date }}  -- System launch date
{{ date.today }}          -- Current date (ISO 8601)
{{ date.formatted }}      -- Current date (human-readable)
```

Conditional sections use block syntax:

```
{{#if repo.tier == "flagship"}}
This is the flagship repository for {{ repo.organ_name }}, representing the
definitive expression of {{ repo.organ }}'s domain.
{{/if}}
```

This interpolation system ensures that announcements always reflect the current state of the registry. When a repository's status changes, all templates that reference it automatically produce updated content.

---

## Quality Checklists

Every template includes a post-composition checklist. No announcement is published until all items are confirmed:

### Universal Checklist (All Templates)

- [ ] Factual accuracy: all claims verified against registry-v2.json
- [ ] Link validity: all URLs tested and returning 200
- [ ] Tone compliance: reviewed against voice guide for target audience
- [ ] Platform format: character limits, embed constraints, image specs met
- [ ] Strategic alignment: announcement serves current phase goals
- [ ] Cross-reference: related announcements on other platforms are consistent
- [ ] Accessibility: alt text on images, readable contrast, screen-reader friendly

### Platform-Specific Additions

**Mastodon:** Thread segmentation tested (each post under 500 chars), hashtag vocabulary compliance, CW applied if appropriate.

**Discord:** Embed renders correctly (preview tested), color matches organ, fields display properly on mobile.

**LinkedIn:** Professional framing present, no casual tone leakage, media attachments high-resolution.

**Email:** Subject line under 60 characters, preview text set, unsubscribe link present, mobile rendering tested.

---

## Publishing Calendar Integration

Templates connect to the distribution calendar maintained in [distribution-strategy](https://github.com/organvm-vii-kerygma/distribution-strategy). The calendar defines:

- **Regular cadences:** Weekly digest (Monday), essay promotion (within 24 hours of publication), community event invitations (7 days before event).
- **Grant-aligned windows:** Announcements timed to precede major grant deadlines (Knight Foundation, NEA, Mellon, NSF) by 2-4 weeks, ensuring recent visible activity during review periods.
- **Conference seasons:** Increased posting frequency during SIGGRAPH, Ars Electronica, ISEA, NeurIPS, and other relevant conferences.
- **Quiet periods:** Reduced posting during major holidays and academic breaks to avoid low-engagement windows.

Templates include calendar metadata (suggested publication window, urgency level, expiration date) that the scheduling system in [social-automation](https://github.com/organvm-vii-kerygma/social-automation) uses for queue management.

---

## Template Inventory

| Template Name | Type | Channels | Variables | Checklist Items |
|--------------|------|----------|-----------|-----------------|
| `repo-launch.md` | Launch | Mastodon, Discord, LinkedIn | 8 | 9 |
| `organ-launch.md` | Launch | Mastodon, Discord, LinkedIn, Email | 12 | 11 |
| `system-milestone.md` | Launch | All channels | 15 | 12 |
| `feature-release.md` | Release | Mastodon, Discord | 7 | 8 |
| `bugfix-release.md` | Release | Discord | 5 | 7 |
| `breaking-change.md` | Release | Mastodon, Discord, Email | 9 | 10 |
| `essay-announce.md` | Essay | Mastodon, Discord, LinkedIn | 8 | 9 |
| `essay-series.md` | Essay | Mastodon, Discord | 10 | 9 |
| `essay-highlight.md` | Essay | Mastodon, LinkedIn | 6 | 8 |
| `salon-invite.md` | Community | Discord, Email | 7 | 8 |
| `reading-group.md` | Community | Discord | 6 | 7 |
| `workshop-sprint.md` | Community | Discord, Email | 8 | 9 |
| `press-release.md` | Institutional | Email, LinkedIn | 11 | 12 |
| `partnership.md` | Institutional | All channels | 9 | 10 |
| `grant-supplement.md` | Institutional | Email | 14 | 13 |

---

## Usage Workflow

1. **Event occurs** -- a repository reaches DEPLOYED, an essay publishes, a community event is confirmed.
2. **Select template** -- choose the appropriate template based on event type.
3. **Populate variables** -- run the interpolation engine against `registry-v2.json` and event metadata.
4. **Adapt for channels** -- generate platform-specific variants from the populated template.
5. **Run quality checklist** -- verify each item on the universal and platform-specific checklists.
6. **Submit to scheduling queue** -- pass the finalized announcement to [social-automation](https://github.com/organvm-vii-kerygma/social-automation) for timed dispatch.
7. **Confirm delivery** -- monitor dispatch confirmation from the automation system.

---

## Metrics and Tracking

Template effectiveness is measured across three dimensions:

- **Reach:** impressions/views per announcement (Mastodon: boosts + favorites; Discord: reactions; LinkedIn: views).
- **Engagement:** click-through rate to canonical URLs (tracked via UTM parameters appended by the automation system).
- **Consistency:** percentage of announcements that pass all checklist items on first review (target: 90%+).

Metrics flow back to the orchestration hub in ORGAN-IV for cross-organ analytics and are used to refine templates iteratively.

---

## Cross-Organ Dependencies

| Dependency | Direction | Purpose |
|-----------|-----------|---------|
| ORGAN-IV orchestration-start-here | VII consumes IV | distribute-content.yml workflow triggers template instantiation |
| ORGAN-V public-process | VII consumes V | Essay publication events trigger essay promotion templates |
| ORGAN-VI community repos | VII consumes VI | Community event scheduling triggers invitation templates |
| registry-v2.json | VII consumes IV | Variable interpolation source for all templates |
| social-automation | VII internal | Templates are consumed by the automation dispatch system |
| distribution-strategy | VII internal | Calendar and audience data inform template selection |

---

## Contributing

Contributions to the template library follow the standard organvm contribution workflow:

1. **Propose** -- open an issue describing the template need (announcement type, target channels, target audiences).
2. **Draft** -- create the template following the structure conventions documented above (sections, variables, checklist).
3. **Review** -- submit a pull request. Review criteria: voice compliance, variable correctness, checklist completeness, platform format accuracy.
4. **Merge** -- approved templates are added to the inventory and become available for the automation pipeline.

See [CONTRIBUTING.md](https://github.com/organvm-vii-kerygma/.github/blob/main/CONTRIBUTING.md) for general contribution guidelines.

---

## License

MIT License. See [LICENSE](LICENSE) for full text.

---

## Author and Contact

**4444J99** -- [@4444J99](https://github.com/4444J99)

Part of the [organvm](https://github.com/meta-organvm) eight-organ creative-institutional system.
ORGAN-VII (Kerygma) -- Marketing, Distribution, and Audience Building.
