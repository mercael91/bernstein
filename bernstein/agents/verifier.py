import logging
from typing import Dict, List, Optional
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)


@dataclass
class VerificationResult:
    """Result of a verification operation with evidence."""
    found: bool
    searched_locations: List[str] = field(default_factory=list)
    searched_count: int = 0
    matched_count: int = 0
    metadata: Dict[str, any] = field(default_factory=dict)

    def to_dict(self) -> Dict:
        return {
            "found": self.found,
            "searched_locations": self.searched_locations,
            "searched_count": self.searched_count,
            "matched_count": self.matched_count,
            "metadata": self.metadata
        }


class AgentVerifier:
    def __init__(self, strict: bool = True):
        self.strict = strict
        self._search_evidence = []

    def verify(self, target: str, corpus: List[str]) -> VerificationResult:
        """Verify target with evidence collection."""
        result = VerificationResult()
        
        logger.info(f"Starting verification for: {target}")
        logger.info(f"Strict mode: {self.strict}")
        
        for location in corpus:
            result.searched_locations.append(location)
            result.searched_count += 1
            
            try:
                if self._check_location(location, target):
                    result.matched_count += 1
                    result.found = True
            except Exception as e:
                if self.strict:
                    raise
                logger.warning(f"Error checking {location}: {e}")
        
        logger.info(
            f"Verification complete: searched={result.searched_count}, "
            f"matched={result.matched_count}, found={result.found}"
        )
        
        return result

    def _check_location(self, location: str, target: str) -> bool:
        """Override in subclasses."""
        raise NotImplementedError
