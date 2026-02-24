"""announcement-templates: Template engine and announcement library for distribution.

Part of ORGAN VII (Kerygma) — the marketing and distribution layer
of the eight-organ creative-institutional system.
"""

__version__ = "0.2.0"

from kerygma_templates.engine import TemplateEngine
from kerygma_templates.quality_checker import QualityChecker, QualityReport
from kerygma_templates.registry_loader import RegistryLoader, EventContext

__all__ = [
    "TemplateEngine",
    "QualityChecker",
    "QualityReport",
    "RegistryLoader",
    "EventContext",
]
