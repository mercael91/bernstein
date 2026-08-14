#!/usr/bin/env python3
import os
import json
import sys
from pathlib import Path

def load_contract_spec(spec_path):
    """Load contract specification from JSON file."""
    with open(spec_path, 'r') as f:
        return json.load(f)

def load_implementation(impl_path):
    """Load current implementation state."""
    with open(impl_path, 'r') as f:
        return json.load(f)

def generate_drift_patch(spec, impl):
    """Generate patch for contract drift between spec and implementation."""
    drift = []
    
    # Check for missing endpoints
    spec_endpoints = set(spec.get('endpoints', {}).keys())
    impl_endpoints = set(impl.get('endpoints', {}).keys())
    
    for endpoint in spec_endpoints - impl_endpoints:
        drift.append({
            'type': 'missing_endpoint',
            'endpoint': endpoint,
            'expected': spec['endpoints'][endpoint]
        })
    
    # Check for schema mismatches
    for endpoint in spec_endpoints & impl_endpoints:
        spec_schema = spec['endpoints'][endpoint].get('schema', {})
        impl_schema = impl['endpoints'][endpoint].get('schema', {})
        
        if spec_schema != impl_schema:
            drift.append({
                'type': 'schema_mismatch',
                'endpoint': endpoint,
                'expected': spec_schema,
                'actual': impl_schema
            })
    
    return drift

def write_drift_report(drift, output_path):
    """Write drift report to file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(drift, f, indent=2)

def main():
    repo_root = Path(__file__).parent.parent
    spec_path = repo_root / 'contracts' / 'api_spec.json'
    impl_path = repo_root / 'contracts' / 'api_impl.json'
    output_path = repo_root / 'contracts' / 'drift_report.json'
    
    if not spec_path.exists():
        print(f"Error: Contract spec not found at {spec_path}", file=sys.stderr)
        sys.exit(1)
    
    if not impl_path.exists():
        print(f"Error: Implementation spec not found at {impl_path}", file=sys.stderr)
        sys.exit(1)
    
    spec = load_contract_spec(spec_path)
    impl = load_implementation(impl_path)
    drift = generate_drift_patch(spec, impl)
    
    write_drift_report(drift, output_path)
    
    if drift:
        print(f"Found {len(drift)} contract drift issues")
        print(f"Drift report written to {output_path}")
        return 1
    else:
        print("No contract drift detected")
        return 0

if __name__ == '__main__':
    sys.exit(main())
