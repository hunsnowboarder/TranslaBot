"""Module that stores the metrics used for monitoring."""

from prometheus_client import Summary
from streamlit_extras.prometheus import streamlit_registry

registry = streamlit_registry()
EXEC_TIME = Summary(
    "response_latency_seconds",
    "Response latency (seconds)",
    labelnames=("app_main_page",),
    registry=registry,
)
