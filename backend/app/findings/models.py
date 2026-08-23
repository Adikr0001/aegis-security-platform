from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class FindingStage(BaseModel):
    """
    Represents one stage of an attack chain.
    """

    stage: str
    evidence_id: str
    raw_event_id: str
    timestamp: str

    entity: Dict[str, Any] = Field(
        default_factory=dict
    )


class FindingAttackPathRelationship(BaseModel):
    """
    Represents one relationship in the selected
    attack path.
    """

    source_entity_id: str
    relationship_type: str
    target_entity_id: str

    evidence_ids: List[str] = Field(
        default_factory=list
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
    )


class FindingAttackPath(BaseModel):
    """
    Security-relevant graph path explaining the finding.
    """

    score: float = Field(
        ge=0.0,
        le=100.0,
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
    )

    entity_ids: List[str] = Field(
        default_factory=list
    )

    relationships: List[
        FindingAttackPathRelationship
    ] = Field(
        default_factory=list
    )

    evidence_ids: List[str] = Field(
        default_factory=list
    )

    reasons: List[str] = Field(
        default_factory=list
    )

    length: int = Field(
        ge=0,
    )


class SecurityFinding(BaseModel):
    """
    Canonical Aegis security finding.

    A finding represents an analyst-facing security
    observation derived from correlated evidence.
    """

    finding_id: str
    incident_id: str
    finding_type: str
    title: str
    severity: str

    risk_score: float = Field(
        ge=0.0,
        le=100.0,
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
    )

    first_seen: str
    last_seen: str

    duration_seconds: float = Field(
        ge=0.0,
    )

    stages: List[FindingStage] = Field(
        default_factory=list
    )

    evidence_ids: List[str] = Field(
        default_factory=list
    )

    entities: List[Dict[str, Any]] = Field(
        default_factory=list
    )

    reasons: List[str] = Field(
        default_factory=list
    )

    attack_path: Optional[
        FindingAttackPath
    ] = None

    metadata: Dict[str, Any] = Field(
        default_factory=dict
    )