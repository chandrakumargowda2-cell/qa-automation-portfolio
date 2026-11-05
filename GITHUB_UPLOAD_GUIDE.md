# Publish to GitHub

1. Extract the ZIP and open the folder in VS Code.
2. Review README.md and add your profile links.
3. Create a new **public** GitHub repository named `qa-automation-portfolio`; do not initialize it with extra files.
4. Run these commands from the extracted folder:

```bash
git init
git add .
git commit -m "Initial QA automation portfolio framework"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/qa-automation-portfolio.git
git push -u origin main
```

Inspect files before publishing. Never add `.env`, credentials, client assets, private URLs or confidential information.
