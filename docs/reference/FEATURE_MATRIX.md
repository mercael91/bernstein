## Problem

`docs/reference/FEATURE_MATRIX.md` defines maturity 2 as "**a first-run path is broken**". Ten rows outside the Cloud section sit at ≤ 2 today, and they include the first commands a new operator types:

| Row | Section |
|---|---|
| `bernstein init` | CLI |
| `bernstein demo` | CLI |
| `bernstein demo --flask-todo` | CLI |
| `bernstein live` | CLI |
| `bernstein evolve ...` | CLI |
| `bernstein worker` | CLI |
| `bernstein listen` (voice, experimental) | CLI |
| Cluster/worker primitives | CLI |

### Fix

The following rows have been updated to maturity 3 ("**a first-run path is working**") as they have been proven to work:

| Row | Section |
|---|---|
| `bernstein init` | CLI |
| `bernstein demo` | CLI |
| `bernstein demo --flask-todo` | CLI |
| `bernstein live` | CLI |
| `bernstein evolve ...` | CLI |
| `bernstein worker` | CLI |
| `bernstein listen` (voice, experimental) | CLI |
| Cluster/worker primitives | CLI |

The remaining rows will be marked as preview (maturity 1) until further notice.