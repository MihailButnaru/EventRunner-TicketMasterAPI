<div align="center">
<h1> Job TicketMaster Events into Postgres </h1>
<p1>Job runner that allows you to store the events from ticketmaster in your database</p1>
</div>
<hr/>

## The Problem

If you want to store data from an API into your database for different analysis, modeling, etc. As part of this
goal, I created a small [Job Runner] as I call it to get the data from the API and store it in postgres database.

## This Solution
This solution is very simple, and the job runner is ready for production.

## Instalation
To run the runner:

1. Install the dependencies of project
```
$ pip install - requirements.txt
```

## Samples
A short example how to use the runner
```
from src.job import JobRunner

if __name__ == "__main__":
    job = JobRunner('US')
    job.runner
```

## License & Author
License © MIHAIL BUTNARU

Made with 💖 Mihail Butnaru