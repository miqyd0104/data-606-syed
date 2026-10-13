# Day 3 — Git and GitHub

30 September 2026

[← Week 2](../README.md) · [Day 2](day-02-critical-thinking-and-visualisation.md)

The morning started with the Week 1 assessment, followed by a recap of Git and an introduction to GitHub. In the afternoon, we saw how to connect a local repository to GitHub, push commits, use a `.gitignore` file and add a README.

## Explaining a technology: what, how and why

A useful way to learn a tool and prepare for technical interview questions is to answer three questions:

- **What is it?** Give a clear definition before adding detail.
- **How does it work?** Explain the main process or concepts at an appropriate level.
- **Why use it?** Connect its features to a practical benefit.

The “how” can become very detailed, so start with the basics. There is no need to explain every internal mechanism to show a sound understanding.

For interview answers, answer the question directly, then add enough explanation to show what it means in practice.

## Git recap

**Git is a version control system.** It records project history so changes can be compared and earlier work can be recovered. It also supports branches for trying changes separately from the main line of work.

Git can do this locally on a computer. A GitHub account or internet connection is not required for the local add-and-commit workflow.

### The basic workflow

| Step | Purpose |
| --- | --- |
| Navigate to the project folder | Make sure commands run in the intended location. |
| `git init` | Set up a new local repository. This is a setup step, not something to repeat before every commit. |
| Edit and save files | Make the changes in the working directory. |
| `git add filename` | Stage the saved content that should go into the next commit. |
| `git commit -m "Explain the change"` | Record the staged changes as a new commit. |

Use `git status` to check the current situation as work progresses. The fuller command examples are in [Day 1's Git notes](day-01-git-and-data-concepts.md).

`cd` changes directories and `pwd` shows the current location. These are shell commands rather than Git commands, but they are important when working with a repository from the terminal.

### Staging and committing

The **staging area** holds the content prepared for the next commit. It lets us choose which changes belong together instead of automatically recording everything being worked on.

A **commit** records a snapshot of the project. Unchanged tracked content remains part of that snapshot, while staged changes provide the new versions. Git can reuse content it already stores rather than make another identical copy of every unchanged file.

The repository's history is normally stored in its `.git` directory. Commit messages help explain the history when looking back through it.

Messages should be short and specific, such as `Add data cleaning notes` or `Fix date conversion`. A history full of messages like `Update` is harder to understand.

The distinction reinforced in the discussion was:

- **Commit:** record changes in the local repository.
- **Push:** send committed work to a remote repository.

Making a commit does not automatically upload anything to GitHub.

## Branching and safe experimentation

I explained that Git keeps snapshots which can be revisited after a mistake, and that branching lets us try another direction alongside the main project.

The trainer described the benefit as **safe experimentation**. A branch gives a separate line of development where an idea can be tried and tested before deciding whether to merge it into the main branch.

For example, a project might already have a working analysis. A new approach can be developed on a branch, then reviewed before being brought into the main version. If the experiment is not useful, there is no need to merge it.

Branching is useful even when working alone. The concept was discussed here; detailed branch and merge commands were outside this recap.

## What GitHub adds

**GitHub is a platform for hosting Git repositories and working with them online.** Git is the underlying version control system; GitHub adds remote hosting and features around that system.

GitLab and Bitbucket were also mentioned as other repository-hosting platforms.

| Git | GitHub |
| --- | --- |
| Records versions and changes. | Hosts repositories remotely. |
| Can be used locally without an internet connection. | Provides an online interface for accessing and sharing repositories. |
| Supports commits, branches and merges. | Adds collaboration, issue tracking and automation features. |

They are often used together, which can make them sound like the same thing. Understanding them separately makes the combined workflow easier to follow.

### Cloud and remote repositories

The introduction to cloud computing described resources provided remotely over the internet, available when needed. The servers still exist physically; they are managed elsewhere rather than being the computer in front of us.

With GitHub, a local repository can be connected to a remote repository. We can continue working locally, record commits and then send that committed work to the remote.

The online copy does not automatically include every file saved on the laptop. It only contains the work that has actually been shared with it.

## Why use a hosted repository?

### Collaboration

A shared remote gives a team a common place to exchange work. People can be given access to the repository and work on changes that can later be reviewed and combined.

Git provides the version-control capabilities, while a hosting platform makes coordinating that work easier.

### Visibility

GitHub's interface makes it easier to inspect files, read commit messages and compare changes. This is another reason to make commit messages meaningful.

Issues can record bugs, questions or work to do. Referring to an issue can help connect a change with the problem it addresses.

### Automation

Hosted platforms can provide additional tools around the repository. **GitHub Actions** was mentioned as an example of automation that can run workflows in response to repository activity.

The main point was that hosting can offer more than somewhere to store files. It can also support the wider development process.

### Recovery and access

Local version history alone does not protect against losing the device that holds it. If committed work has been pushed to a remote repository, it can be recovered on another machine by cloning the repository, provided access is available.

Uncommitted or unpushed work would still be missing from that remote copy.

Repository permissions also help organisations manage who can access shared work. Removing someone's remote access prevents further access through that account; it does not erase copies they already downloaded.

### Community and sharing

Public repositories make it possible to discover projects, learn from how other people approach problems and share work with others.

For this training repository, keeping the notes organised and readable helps someone else understand the topics covered and the practical work added over time.

## Connecting a local repository to GitHub

The demo started with an existing local repository that already contained commits. A new, empty repository was then created on GitHub.

### Creating the remote repository

Choose a clear repository name and description, then decide who should be able to see the content:

- **Public:** anyone can view the repository. This does not give everyone permission to push changes to it.
- **Private:** access is restricted to authorised users.

The advice was to choose private when unsure what could safely be shared. Public repositories can be useful for showcasing appropriate work. Passwords, tokens and private keys should be kept out of both public and private repositories.

For the demo, the options to create a README and `.gitignore` on GitHub were left off. Those files were added locally later, so the remote began empty.

### Add the remote

First, navigate into the local repository and check the current state. For a repository being connected for the first time, the command sequence looks like this, using this training repository's URL as an example:

```bash
git status
git remote add origin https://github.com/miqyd0104/data-606-syed.git
git remote -v
```

`origin` is a short name for the remote, not a branch name. Adding it records the address locally; it does not upload files or authenticate with GitHub. Only add it once. `git remote -v` shows the configured addresses. See [GitHub's remote repository guide](https://docs.github.com/en/get-started/git-basics/managing-remote-repositories).

### Branch name and first push

The demo's local branch was named `master` and was renamed to `main` before the first push:

```bash
git branch -M main
git push -u origin main
```

`main` is a branch name, not a requirement for GitHub to work. The rename made the example use the intended branch name consistently.

In the push command, `origin` identifies the remote and `main` identifies the local branch to send. The `-u` option sets its upstream tracking relationship, which later commands can use. It is not necessary to set that relationship again with every push. See the [Git push documentation](https://git-scm.com/docs/git-push).

After the push, refreshing GitHub showed the files and the earlier commit history. The normal workflow then becomes **edit, save, stage, commit, push**.

### What actually gets pushed?

A push sends the commits needed to update the selected remote branch, including any required earlier history the remote does not already have.

It does not send unstaged edits, staged-but-uncommitted changes or every other local branch automatically. This is why saving a file or adding it to staging is not enough to make it appear on GitHub.

### HTTPS and SSH

The first push in the demo failed because the remote used an SSH address and the authentication setup was not ready for that connection. The remote was changed to HTTPS and the push succeeded.

These address styles use different authentication methods:

```text
HTTPS: https://github.com/USERNAME/REPOSITORY.git
SSH:   git@github.com:USERNAME/REPOSITORY.git
```

Replace `USERNAME` and `REPOSITORY` with the relevant account and repository names.

For HTTPS, GitHub supports a credential helper or a personal access token; the normal account password is not used for Git authentication. SSH uses a configured key pair. See [GitHub's authentication guidance](https://docs.github.com/en/get-started/git-basics/about-remote-repositories).

The demo removed and re-added `origin`. An existing address can also be changed directly:

```bash
git remote set-url origin https://github.com/miqyd0104/data-606-syed.git
git remote -v
```

Changing the remote address changes where Git connects. It does not create a new commit or upload the project.

### Cloning a repository

Cloning creates a local copy of an existing remote repository. Run it from the folder where the new project directory should be created:

```bash
git clone https://github.com/miqyd0104/data-606-syed.git
```

This brings down the repository and its history, ready to work with locally. There is no need to run `git init` inside a repository that has just been cloned.

## Using `.gitignore`

A `.gitignore` file contains patterns for files and folders that should remain untracked. Its exact name is `.gitignore`, with no extra `.txt` extension.

The demo used a sample file called `passwords.txt` to show how ignoring works. An example of ignore patterns is:

```gitignore
passwords.txt
temporary-files/
*.tmp
```

A filename targets that file, a folder pattern can exclude a directory, and `*` acts as a wildcard. The demo also showed `*.txt`, which matches text files generally, so the scope of a pattern matters.

Set up ignore rules before adding unwanted files. They do not erase earlier commits or automatically stop tracking a file that is already tracked. Sensitive content can remain visible in the history even after it is removed from the latest version.

For shared project rules, normally commit the `.gitignore` file itself so other people receive those rules when they clone the repository.

## README files

A `README.md` gives the repository a clear introduction. GitHub displays it on the repository page, so a reader does not need to open individual files to understand the project.

Useful content includes the project's purpose, how the folders are organised and links to the main files. For these notes, the README helps readers find the right week and day.

The demo added a README using the same workflow as any other file:

```bash
git add README.md
git commit -m "Add repository introduction"
git push origin main
```

After refreshing GitHub, the README appeared beneath the file listing.

## Learning tools before combining them

The session returned to the idea of learning each tool's purpose before connecting several together. Combining tools can add useful capabilities, but also makes the overall system more complex.

The progression here was to understand Git locally first, then understand what GitHub adds. The same approach can apply later when combining tools for a data pipeline: know what each part does, how it works and why it is needed.

The recommendation was to practise the commands before relying on graphical buttons or automation. Those tools can save time, but understanding the steps makes it easier to explain the workflow and diagnose a problem.

Two terminal habits from the demo were to check the current directory before acting and use Tab to complete a filename once enough of it has been typed to identify it.

## Other work for the day

The Week 1 assessment was closed book, with one hour available.

The priorities for the rest of the day were:

1. Complete the separate AI task for Helen.
2. Apply feedback to the second version of the professional profile.
3. Continue the Excel dashboard.
4. Start the optional SQL learning resources if the earlier work was finished.

The dashboard target was extended to Thursday afternoon, with reviews intended for Friday. Presentations were still a possibility rather than a confirmed requirement.

The trainer also asked for a brief end-of-day update on progress. The professional habit was to communicate what had been completed and what still needed attention, especially when several tasks were competing for time.
