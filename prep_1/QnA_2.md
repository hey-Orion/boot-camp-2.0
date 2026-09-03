Track 2 — Discussion: GitHub Actions, Logging/Sentry, Git/GitHub

Answer out loud first, then write short versions, no notes:

What is a GitHub Actions workflow, and what triggers it?
What's the difference between a GitHub Actions "job" and a "step"?
In your CI/CD setup, what does your pipeline actually check before code gets merged/deployed?
Why use a dedicated tool like Sentry instead of just writing errors to a log file?
What's the difference between logging levels like INFO, WARNING, and ERROR — and how did you decide what to log at each level in your project?
What's the difference between git merge and git rebase?
What's the difference between main and a feature branch in your normal workflow — and why do teams avoid committing directly to main?
Track 3 — Project Walkthrough

Write and rehearse a 2-3 minute narrated tour of Dataflow-Sentinel, out loud. Structure:

What the pipeline does, in one clear sentence (this is the piece to fix from yesterday)
Why Medallion Architecture (Bronze/Silver/Gold) — what problem does that layering solve
Why Airflow (tie back to your migration story)
One technical challenge you hit and solved (Docker/WSL2, or another)
What you'd add next if you had more time (shows forward thinking)