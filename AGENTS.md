# Wenmai Skills Repository Instructions

## Scope

These instructions apply to the entire repository. Use them when creating or updating API-backed Skills under `skills/`.

## Working Principles

- Communicate with users in Chinese unless they request another language.
- Inspect `git status --short --branch` before editing. Preserve unrelated or user-authored changes.
- Keep each Skill focused on one documented operation and one fixed endpoint.
- Treat the Skill's `references/api.md` as the source of truth for request fields, limits, defaults, response fields, warnings, and error behavior.
- Prefer concise, operation-specific instructions over generic provider-wide boilerplate.
- Do not add undocumented behavior, fields, defaults, or inferred data.

## Skill Update Workflow

1. Read the complete target `SKILL.md` and `references/api.md` before editing.
2. Inspect the matching script, `skill-card.md`, and `agents/openai.yaml` when they affect the requested change.
3. Compare the current Skill with the API contract and remove generic rules that do not apply to the endpoint.
4. Update frontmatter first, then organize the body around the executable workflow.
5. Keep detailed schemas in `references/api.md`; include only execution-critical rules in `SKILL.md`.
6. Validate the Skill and run the repository tests after editing.

## Frontmatter Contract

Use this structure:

```yaml
---
name: <skill-directory-name>
description: "<capability and trigger description>"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---
```

Write `description` as the primary discovery and triggering contract:

- Start with the provider's recognizable Chinese and English names when available. Use these canonical forms where applicable:
  - `极目数据（JIIMORE）`
  - `卖家精灵（SellerSprite）`
  - `XYDC（西柚洞察）`
- Identify the platform, resource, and operation, such as Amazon ASIN 商品详情。
- Summarize the most decision-relevant response capabilities documented by the API.
- Include important request limits when they define the capability, such as 1～20 个 ASIN。
- List concrete user intents that should trigger the Skill.
- Add an implicit trigger for users who describe the data need without naming the provider.
- Do not claim fields or use cases that are absent from `references/api.md`.
- Keep all trigger guidance in frontmatter; do not add a redundant “When to use” section to the body.

## Recommended SKILL.md Structure

Use the smallest structure that fully explains the operation:

1. `# <Provider> <Platform> <Capability>`
2. `## Overview`
3. `## Workflow`
4. `## How To Run`
5. `## Request Rules`
6. `## Response Rules`
7. `## Error Handling`

### Overview

- State the exact operation code and business purpose.
- Declare that the Skill calls one fixed endpoint and does not accept dynamic endpoints or unrelated operations.
- List the endpoint, authentication header, script path, and a relative link to `references/api.md`.
- Instruct the agent to read `references/api.md` before constructing requests or interpreting fields.

### Workflow

Write an imperative, endpoint-specific sequence that covers:

1. Extracting and validating user inputs.
2. Preserving user-specified marketplace and scope.
3. Constructing the exact documented payload shape.
4. Running the fixed script and retaining the raw JSON response.
5. Checking gateway status, identifiers, completeness fields, and warnings.
6. Producing a traceable summary without inference or fabrication.

Do not copy generic references to keywords, niche IDs, pagination, filters, or sorting unless this endpoint actually supports them.

### How To Run

- Direct users to https://skill.wenmai-ai.com/wenmaiskills/use_guide.html for the `secret-key` and recharge instructions.
- Export the credential as `WENMAI_API_KEY`; mention `WENMAI_SECRET_KEY` only as the supported compatibility variable.
- Run the exact script documented in `references/api.md` with a valid JSON example matching the API payload.
- Use placeholders such as `sk-...`; never commit or echo a real credential.
- State that the script prints the raw Wenmai API response as formatted JSON.

Example pattern:

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/<script>.py '<documented-json-payload>'
```

### Request Rules

- Preserve required wrapper objects such as `request`; never flatten nested fields.
- State required and optional fields using their exact documented names.
- Enforce array sizes, formats, supported values, and other documented limits.
- If a request exceeds an API limit, split it explicitly when appropriate; never silently truncate it.
- Preserve user-specified optional values. If the API defines a server default, omit the field when unspecified instead of inventing a client-side default.
- Do not add parameters that are absent from `references/api.md`.

### Response Rules

- Present comparisons or multi-item responses as compact tables when useful.
- Keep every summarized value traceable to its original response field.
- Preserve time windows, units, currencies, marketplaces, and metric basis fields; do not mix incompatible measurement periods.
- Report normalized or resolved identifiers returned by the API.
- Always surface warnings, unresolved inputs, partial failures, and data-completeness fields.
- Mark absent values as missing; never estimate or fabricate them.

### Error Handling

- For missing credentials, instruct the user to configure the environment variable without pasting the key into chat.
- For parameter errors, identify the relevant wrapper, required field, format, or documented limit.
- For HTTP, gateway, `error`, or non-`OK` responses, report only sanitized status, message, and `requestId` when present.
- For insufficient balance or quota, direct the user to the Wenmai Skills usage guide.
- Never expose API keys, authorization headers, or sensitive response values in logs or documentation.

## Progressive Disclosure

- Keep `SKILL.md` focused on triggering and execution.
- Keep complete parameter tables, response schemas, curl examples, and detailed field definitions in `references/api.md`.
- Link directly from `SKILL.md` to `references/api.md`; avoid duplicating the full API contract.
- Keep the Skill body under 500 lines unless the operation genuinely requires more detail.

## Consistency Checks

- Ensure `name` exactly matches the Skill directory.
- Ensure the endpoint, operation code, script name, example payload, required fields, and limits match `references/api.md`.
- Check whether `skill-card.md` or `agents/openai.yaml` became stale after a capability or display-name change; update them only when needed for consistency.
- Do not modify scripts or API references for a documentation-only request unless the source contract itself is changing.

## Validation

From the repository root, run:

```bash
uv run --with pyyaml python \
  ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skills/<skill-name>
npm test
git diff --check
```

Before handing off, confirm that only intended files changed and report the validation results. Do not call a live API unless the user explicitly requests a live smoke test and provides the required authorization through environment configuration.
