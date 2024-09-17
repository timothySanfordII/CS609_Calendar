#To push your code to GitHub, follow these steps using Git commands:

1. **Initialize your repository (if it's not already initialized):**
   ```bash
   git init
   ```

2. **Add the remote repository URL (if it's not already added):**
   Replace the URL with your GitHub repository URL.
   ```bash
   git remote add origin https://github.com/username/repository-name.git
   ```

3. **Add all changes to staging:**
   ```bash
   git add .
   ```

4. **Commit your changes:**
   Replace `commit-message` with a meaningful message.
   ```bash
   git commit -m "commit-message"
   ```

5. **Push your code to GitHub:**
   If it's your first time pushing, use the `-u` flag to set the upstream branch:
   ```bash
   git push -u origin main
   ```
   If your branch is named something other than `main`, replace `main` with your branch name (e.g., `tommy`).

If you're working with a new branch, don't forget to create the branch before pushing:
```bash
git checkout -b branch-name
git push -u origin branch-name
```

Let me know if you need further clarification!