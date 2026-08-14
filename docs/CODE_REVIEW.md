## Deterministic Review Policy

To ensure a consistent and predictable review process, we will apply the following conventions:

* For security-sensitive paths (`SECURITY.md`, `src/bernstein/core/security/**`, and others), two approving reviews are required.

## Architecture Import Rules

The `.importlinter` and `src/bernstein/core/quality/arch_conformance.py` (`check_arch_conformance()`) will enforce architecture import rules mechanically, ensuring that rules are resolved and checked against a change, not just documented.

## Review Process

To ensure a deterministic review process, we will:

* Review all changes against the defined conventions.
* Ensure that all security-sensitive paths require two approving reviews.
* Enforce architecture import rules mechanically using `.importlinter` and `src/bernstein/core/quality/arch_conformance.py`.

## Commit Message

When committing changes, please include a clear and concise commit message that follows the project's coding style.

## PR Title and Body

When opening a pull request, please include a clear and concise title and body that follows the project's coding style.

Closes #3752