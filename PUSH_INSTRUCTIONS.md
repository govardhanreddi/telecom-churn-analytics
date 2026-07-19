# Safe push instructions

## Important first step

Change the MySQL password that was previously committed in the public repository. The old value remains visible in Git history even after replacing the file.

## Recommended method: update the existing repository

This method preserves the existing `powerBI/telecom_churn.pbix` file.

```bash
git clone https://github.com/govardhanreddi/telecom-churn-analytics.git
cd telecom-churn-analytics
```

Copy all files from this polished package into the cloned folder **without deleting** `powerBI/telecom_churn.pbix`, then run:

```bash
git add .
git commit -m "Polish telecom churn analytics project"
git push origin main
```

Do not use a force-push for this repository unless you have first copied the PBIX file into this package.
