"""Every Celery task name used by beat, routing or send_task must be a registered task."""

from unittest.mock import patch

from celery import Celery

from app.config import settings
from app.constants.celery_tasks import CeleryTask
from app.integrations.celery.core import create_celery


def _celery_app() -> Celery:
    flags = dict.fromkeys(("data_lifecycle_enabled", "ow_scores_enabled", "telemetry_enabled"), True)
    with patch.multiple(settings, **flags):
        celery_app = create_celery()
    celery_app.loader.import_default_modules()
    return celery_app


def test_core_tasks_and_constants_match() -> None:
    registered = {name for name in _celery_app().tasks if name.startswith("app.")}

    assert registered == set(CeleryTask)


def test_beat_schedule_and_routes_use_constants() -> None:
    celery_app = _celery_app()
    beat_tasks = {entry["task"] for entry in celery_app.conf.beat_schedule.values()}

    assert beat_tasks <= set(CeleryTask)
    assert set(celery_app.conf.task_routes) <= set(CeleryTask)
