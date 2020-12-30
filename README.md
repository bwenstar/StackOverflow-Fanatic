# StackOverflow-Fanatic
StackOverflow crowns users with a 'Fanatic Badge' if you log into your account for 100 consecutive days. I don't check StackOverflow daily, but I want the badge, so I thought I'd write a script and have GitHub Actions take care of the rest.

## How can I get my Fanatic Badge using GitHub Actions?
**This script only works if you use an email to login** (no GitHub/Google/Facebook logins)
1. Fork this repo
2. In your forked repo, go to the `Settings` tab
3. Select `Secrets` from the sidebar
4. Add two secrets:
    * `SO_USERNAME` - the email you use for StackOverflow
    * `SO_PASSWORD` - your StackOverflow password

Once these steps are complete, GitHub Actions will take care of the rest. Currently, the script is configured to run daily @ 13:07 UTC. If you'd like, you can change what time it will run by modifying the `.github/workflows/fanatic.yml` file. Don't forget to disable the Action once you've received your Fanatic Badge.
