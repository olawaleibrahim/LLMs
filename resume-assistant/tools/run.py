from datetime import datetime as dt
from pathlib import Path

import click
from loguru import logger

from pipelines import scrape_webpage_pipeline


@click.command(
    help="""
Digital Research Assistant project CLI v0.0.1. 

Main entry point for the pipeline execution. 
This entrypoint is where everything comes together.


Run a pipeline with the required parameters. This executes
all steps in the pipeline in the correct order using the orchestrator
stack component that is configured in your active ZenML stack.

Examples:

  \b
  # Run the pipeline with default options
  python run.py
               
  \b
  # Run the pipeline without cache
  python run.py --no-cache
  
  \b
  # Run only the ETL pipeline
  python run.py --only-etl

"""
)
@click.option(
    "--no-cache",
    is_flag=True,
    default=False,
    help="Disable caching for the pipeline run.",
)
@click.option(
    "--run-scrape-job-description",
    is_flag=True,
    default=False,
    help="Whether to run the scrape job description pipeline.",
)
@click.option(
    "--url",
    default="https://job-boards.greenhouse.io/scaleai/jobs/4413274005",
    help="Filename of the ETL config file.",
)
def main(
    no_cache: bool = False,
    run_scrape_job_description: bool = False,
    run_etl: bool = False,
    url: str = "https://job-boards.greenhouse.io/scaleai/jobs/4413274005",
) -> None:
    assert (
        run_scrape_job_description
    ), "Please specify an action to run."


    root_dir = Path(__file__).resolve().parent.parent

    if run_scrape_job_description:
        job_description = scrape_webpage_pipeline(url)
        print(job_description)


if __name__ == "__main__":
    main()