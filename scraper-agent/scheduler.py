import logging
from typing import Callable

from apscheduler.schedulers.blocking import BlockingScheduler


def run_with_optional_schedule(
    run_once: Callable[[], None],
    schedule_enabled: bool,
    schedule_hours: int,
) -> None:
    if not schedule_enabled:
        run_once()
        return

    logging.info("Schedule enabled. Running now, then every %s hour(s).", schedule_hours)
    run_once()

    scheduler = BlockingScheduler(timezone="UTC")
    scheduler.add_job(run_once, "interval", hours=schedule_hours, id="scraper_agent_run")

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logging.info("Scheduler stopped.")
