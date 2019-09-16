from src.job import JobRunner

""" A small example, shows how to run the job to save the events from the ticket master in the database """
if __name__ == "__main__":
    job = JobRunner('US')
    job.runner