# Day 1 — Git and data concepts

28 September 2026

[← Week 2](../README.md)

We started the week with Git and the command line, then covered basic statistics, data types, file formats and data cleaning. These are the foundations for the Excel dashboard work coming next.

## Version control

A version control system records changes to files over time. It lets us compare versions, understand what changed and recover earlier work when needed.

This is useful for code, notes and other project files. It avoids relying on lots of manually saved copies with names such as `final`, `final-2` and `final-latest`.

**Git** is the version control software. **GitHub** is a service that hosts Git repositories and provides tools for sharing and collaboration. Git can be used locally without putting anything on GitHub.

The main benefits discussed were:

- Comparing changes between versions.
- Returning to a known working version.
- Seeing when changes were recorded and who made them.
- Trying a different approach on a branch before bringing it into the main work.

Branching was introduced as a concept, but the demonstration focused on the basic local workflow.

### Commits and snapshots

A **commit** records a snapshot of the tracked project content prepared for it. Each commit has an identifier and a message explaining the change.

Git avoids storing another identical copy of every unchanged file for each snapshot. It can refer to content it already has, while recording new content where files have changed.

The photo analogy was useful: a commit captures a particular version of the project, while staging lets us choose which changes will appear in that picture.

### Working directory, staging area and repository

| Area | Purpose |
| --- | --- |
| Working directory | The files being edited on the computer. |
| Staging area, also called the index | The content prepared for the next commit. |
| Git repository | The recorded history and supporting information, normally stored in the hidden `.git` directory. |

Saving a file, staging it and committing it are separate actions.

For example, suppose `notes.md` and `analysis.sql` were both committed yesterday. Today both files have changed, but only `notes.md` is ready:

1. Stage the updated `notes.md`.
2. Create a commit.
3. The commit contains the new notes and the previously committed version of `analysis.sql`.
4. The unfinished SQL changes remain in the working directory.

Leaving a change unstaged does not delete it. Also, editing a file after staging it does not automatically update the staged copy: run `git add` again to include the newer edits. The [Git book](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository) explains this distinction.

### The core Git commands

| Command | What it does |
| --- | --- |
| `git init` | Creates a repository in the current folder. Do this when setting up a new local repository. |
| `git status` | Shows the current branch and any untracked, modified or staged files. |
| `git add notes.md` | Stages the current saved content of `notes.md`. |
| `git commit -m "Add Git notes"` | Records the staged changes with a message. |

After creating and saving `notes.md` in a new practice folder, the basic sequence is:

```bash
git init
git status
git add notes.md
git status
git commit -m "Add Git notes"
git status
```

For later changes, repeat **edit, save, stage, commit**. There is no need to initialise the same repository again each time.

`git add .` stages changes within the current directory and its subdirectories. Adding named files makes it easier to control what is included. Check `git status` before committing.

A new file is **untracked** until it is added. A tracked file can be unchanged, modified or staged. Tracked does not mean it is always ready for the next commit.

Commit early and often, keeping each change understandable. A message such as `Add data cleaning notes` is more useful than `Changes`, especially when looking back through the history.

### Repository scope and ignored files

The folder where `git init` runs determines the repository's scope. Initialising a course folder covers the files and subfolders within it; initialising a separate weekly folder creates a smaller repository for that week.

This repository keeps all eight weeks together so the course notes are in one place.

The two similarly named Git items have different purposes:

- **`.git`** is the directory containing Git's history and repository information.
- **`.gitignore`** is a text file containing patterns for files Git should leave untracked, such as temporary files.

Adding a file to `.gitignore` does not remove it from earlier commits or automatically stop tracking it if it is already tracked. This matters for passwords and other information that should never enter the repository.

### Git and Excel

I asked how Git works with something like Excel. A saved `.xlsx` file can be tracked using the same add-and-commit process, while the actual editing happens in Excel.

Git can retain workbook versions, but an Excel workbook does not give the same readable line-by-line comparison as a plain text file. Version history and a useful view of individual cell changes are different things.

## The command line

A **terminal** provides the window for entering commands and reading output. A **shell**, such as Bash or Zsh, interprets those commands. A graphical user interface uses windows, menus and buttons instead.

The session used Git Bash on Windows. On my Mac, I can use Terminal or the terminal inside VS Code. The basic navigation and Git commands covered work in Bash and Zsh.

### Moving around folders

The shell has a current working directory. Check this before running commands that affect files.

| Command | Meaning |
| --- | --- |
| `pwd` | Print the path of the current working directory. |
| `ls` | List its visible files and folders. |
| `ls -a` | Include hidden entries, such as `.git`. |
| `cd week-02` | Move into the `week-02` folder. |
| `cd ..` | Move up to the parent folder. |
| `cd ~` | Return to the home directory. |

The dot in a path means the current directory; two dots mean the parent. The tilde, `~`, represents the home directory in these shells.

Spaces separate parts of a command. If a filename or path contains spaces, quote it, for example `cd "Training Notes"`. Consistent names with hyphens can make navigation simpler.

### Why learn commands?

Commands help make actions precise and repeatable. They can also be combined into scripts for automation. Many server environments are managed through a command line, so it is useful to work comfortably without relying on a desktop interface.

The aim is to understand what a tool is doing. A graphical Git tool can be convenient, but the underlying difference between staging and committing still matters.

There is no need to memorise every command. Look up unfamiliar commands and understand their effect before running them.

## Basic statistics

### Mean, median and mode

Choose an average that fits the question and the data.

| Measure | How it works | What to consider |
| --- | --- | --- |
| Mean | Add the values and divide by their count. | Uses every value, so extreme values can pull it up or down. |
| Median | Sort the values and find the middle; with an even count, average the two middle values. | Less affected by extreme values. |
| Mode | Find the most frequently occurring value. | Useful for common values or categories; there may be more than one mode. |

For a simple example, take `4, 5, 5, 6, 30`:

- Mean: `50 ÷ 5 = 10`.
- Median: `5`.
- Mode: `5`.

The value `30` pulls up the mean. That does not make the mean incorrect; it means we need to decide which measure best describes the question being asked.

Weighted, geometric and harmonic averages were also mentioned, but the main focus was understanding when to use mean, median and mode.

### Standard deviation and distributions

**Standard deviation** measures how spread out numerical values are around the mean. A smaller value means the observations are more tightly grouped; a larger value means greater spread. It uses the same units as the original data.

A **histogram** groups numerical observations into intervals called bins. Too many bins can make the pattern look noisy; too few can hide useful detail.

A **normal distribution** has a symmetrical bell shape. About 68% of its values lie within one standard deviation of the mean. That rule depends on the distribution being normal; it does not apply to every dataset. See the [NIST normal distribution explanation](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3661.htm).

**Skew** describes an uneven distribution:

- **Positive or right skew:** the longer tail extends towards larger values.
- **Negative or left skew:** the longer tail extends towards smaller values.

The direction refers to the tail. It does not mean all the values are positive or negative. Income and exam-score examples were used to discuss how the context and possible limits on values affect a distribution.

### Outliers

An outlier is unusually far from the other observations. It could be a valid unusual value, a data-entry error or a problem introduced during processing.

The height example made the distinction clear: an exceptionally tall person may be real, while a recorded human height of 60 feet points to a problem with the data.

Investigate the source, units and context before changing or removing an outlier. Removing genuine extremes can change the meaning of the analysis.

### Correlation and causation

Correlation describes an association between variables:

- **Positive:** higher values of one tend to occur with higher values of the other.
- **Negative:** higher values of one tend to occur with lower values of the other.
- **Little or no linear correlation:** there is no clear straight-line pattern.

For Pearson's correlation coefficient, `r` ranges from `-1` to `1`. Values near either end indicate a strong linear relationship; a value near zero does not rule out a curved relationship.

**Correlation does not prove causation.** Two measures may move together because of another factor, a shared trend over time or coincidence.

The divorce-rate and margarine-consumption example showed how unrelated-looking measures can still produce a strong statistical relationship. A convincing-looking chart does not establish that one causes the other.

When presenting analysis, explain what the data shows, then separate possible explanations from conclusions supported by evidence.

## Data types

The type of a value affects how a system stores, compares and calculates with it.

| Type | Example | Use |
| --- | --- | --- |
| Integer | `12` | Whole-number counts. |
| Float | `20.5` | Numbers represented using floating-point arithmetic, including fractional measurements. |
| String | `"London"` | Text, labels and identifiers. |
| Boolean | `True` or `False` | Yes/no conditions. |
| Date | `2026-09-28` | A calendar date. |
| Time | `14:30:00` | A time of day. |
| Date and time | `2026-09-28 14:30:00` | Both parts together, with time-zone information where needed. |

**Continuous data** represents measurements on a scale, such as height. **Discrete numerical data** represents separate counts, such as the number of orders. **Categorical data** groups observations, such as product type or customer sector.

These describe meaning as well as storage. A category can be represented by a number, and a phone number or customer ID may need to be stored as text. Digits alone do not make something a quantity we should average.

Boolean operations include **AND**, **OR** and **NOT**. Their symbols vary between languages. The pipe symbol, `|`, and tilde, `~`, were also discussed; their meaning depends on where they are used.

### Dates and times

Date formats can be ambiguous. `03/04/2026` could mean 3 April or 4 March, depending on the convention. Check the source format before converting it.

The year-first form `YYYY-MM-DD` makes the intended ordering clearer. Time zones also matter: UTC, GMT and British Summer Time should not be treated as interchangeable labels.

Use appropriate date/time types so values can be sorted, compared and grouped correctly.

### Key-value pairs

A key identifies a value. The value can be a simple item or a more complex structure, such as a list.

```json
{
  "first_name": "Bugs",
  "last_name": "Bunny",
  "location": "Earth"
}
```

Key-value structures are common in JSON, APIs and configuration files.

## File formats

| Format | Main purpose |
| --- | --- |
| `.txt` | Plain text. |
| `.md` | Markdown text with formatting syntax. |
| `.csv` | Tabular text data, usually with commas separating fields. |
| `.xlsx` | Excel workbooks, including worksheets, formulas, charts and formatting. |
| `.json` | Structured data using objects, arrays and values; common in APIs. |
| `.yaml` / `.yml` | Structured data often used for configuration; indentation matters. |
| `.xml` | Structured information using tags. |
| `.py` | Python source code. |
| `.ipynb` | Notebook documents used by tools such as Jupyter and Google Colab. |
| `.sql` | SQL statements saved as a script. |
| `.zip` | An archive that bundles files and can compress their contents. |
| `.dat` | A generic extension whose contents depend on the application that created it. |
| `.exe` | A Windows executable, which may be an application or installer. |

I mentioned Google Colab when notebook formats came up. The notebook extension is `.ipynb`.

### CSV and Excel workbooks

A **delimiter** separates fields in a text file. CSV commonly uses commas, while other delimited files may use tabs or semicolons. Check the delimiter when importing data.

```csv
product,quantity,price
Notebook,3,2.50
Pen,5,1.20
```

Opening a CSV in Excel does not turn the original file into an Excel workbook. A CSV holds text data; it does not preserve workbook features such as multiple worksheets, charts and formatting.

**Save the dashboard as `.xlsx`.** Saving the finished work only as a CSV would lose those workbook features.

Changing a filename's extension is not the same as converting its contents to another format.

## Data quality

Good-quality data is suitable for the purpose it will be used for. We examined a table with missing values, duplicate records, inconsistent units, incomplete details and implausible dates.

I pointed out the missing values. These were highlighted as an important early check when exploring a dataset.

| Quality issue | What to check |
| --- | --- |
| Validity | Does the value satisfy the expected type, format, range and other rules? |
| Accuracy | Does it reflect the real value in context? |
| Completeness | Are required values present and complete, rather than missing or cut short? |
| Consistency | Do related records agree, or do they contradict each other? |
| Uniformity | Are units, formats and conventions used consistently? |
| Redundancy | Is the same observation stored more than once unnecessarily? |

A date can be valid in format but inaccurate for the person it describes. A date of birth in 1699 is a possible historical date, but would be implausible in a dataset of living customers.

Uniformity issues included heights stored in feet, inches, metres and centimetres. Duplicate customer rows also contained conflicting details, so simply deleting one row without checking could lose useful information.

## Cleaning data

Keep the original data available and record the changes made. Cleaning decisions should follow the purpose of the analysis.

### Common cleaning steps

- **Remove irrelevant data:** exclude fields or records that are not needed, while retaining the original source.
- **Investigate duplicates:** remove genuine repeated observations, but reconcile conflicting records carefully.
- **Standardise units and formats:** make measurements, dates and labels comparable.
- **Convert types:** store quantities as numbers and dates as dates where appropriate.
- **Check typos:** review suspicious labels and use matching methods carefully.
- **Investigate missing and invalid values:** choose a suitable treatment instead of applying one rule to everything.

For heights, convert the measurements to one unit and make the unit clear in the column name, such as `height_cm`. Removing the text `cm` without first converting other units would give misleading numbers.

Also, **5 feet 4 inches is not 5.4 feet**. It is 64 inches, or 162.56 cm. The conversion needs to reflect the units, rather than just rearranging the characters.

Be careful when standardising labels. Similar names may refer to different things, and historical names may matter to the question being analysed. Fuzzy matching can suggest possible matches, but does not prove they are the same record.

### Scaling

Scaling changes the numerical range used to represent values. Converting exam marks into percentages is one example that can make results easier to compare.

Min-max normalisation can rescale values to a range such as zero to one. This is a different meaning of normalisation from database normalisation, which concerns table structure.

### Missing values

There is no single correct treatment for every missing value. Consider how much is missing, why it might be missing and how important the information is.

| Approach | When it may help | Main consideration |
| --- | --- | --- |
| Drop rows or columns | Too little useful information remains, or the data is unnecessary for the question. | Removing data can lose information or introduce bias. |
| Impute a value | A justified estimate allows useful records to be retained. | The replacement is estimated, not observed. |
| Hot-deck imputation | Use a suitable donor record from the same dataset. | The donor must be meaningfully comparable. |
| Cold-deck imputation | Use suitable information from another dataset or earlier source. | Check that the source is relevant and still applicable. |
| Flag missingness | Keep the observation and make the absence visible. | Keep the missing-data meaning distinct from a real value. |

Mean or median replacement and model-based estimates were mentioned as imputation options. Carrying forward an earlier observation was also discussed, but it only makes sense when the ordering and context support it.

In the class example, one row contained only a name and almost no other information. I suggested removing it. That was a decision about that particular example, rather than a rule to delete every incomplete row.

A blank is not automatically zero. Zero may be a genuine measurement and would change totals and averages if used to represent unknown values. A separate missing-value flag can preserve the distinction.

The customer-sector example showed when an **Unknown** category can be useful. If a customer has not provided their sector, their sales can still be included under Unknown rather than disappearing from a sector breakdown.

## Preparation for the Excel dashboard

The next practical task was introduced as exploring, cleaning and analysing a dataset, then presenting a dashboard with useful insights.

The guidance for choosing data was:

- Pick a subject that is interesting enough to explore and explain.
- Choose enough data to support meaningful analysis without making it unmanageable.
- Prefer a CSV or another format that can be imported easily.
- Look for several questions the data could help answer.
- Keep the subject suitable for a professional presentation.
- Some cleaning work is useful, but avoid spending the whole task rescuing unusable data.

Kaggle was suggested as somewhere to look, but it was not the only permitted source.

The dashboard needs a clear audience and business purpose. Explain what is happening, what the findings could mean and what action they might support. Charts alone are not the whole analysis.

For independent work, the options were to consolidate Git, revise the data concepts, look for a dashboard dataset or work on the separate AI task.
