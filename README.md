# htmlxlsx

A simple CLI application to retrieve interaction information between aminoacid residues given in an HTML file by [PDBSum](https://www.ebi.ac.uk/thornton-srv/databases/pdbsum/).

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have Python 3.6+ installed on your machine.
- You have `git` installed to clone your repository.
- You have `pip` installed.

## Installation

1. **Clone the Repository**

   Open your terminal or command prompt and clone the repository using `git`:

   ```sh
   git clone https://github.com/Caeneus60/htmlxlsx.git
   ```

2. **Navigate to the Project Directory**
   Change into the project directory:

   ```sh
   cd htmlxlsx
   ```

3. **Install the package**
   Use `pip` to install the package along with its dependencies specified in the `pyproject.toml` file:

   ```sh
   pip install .
   ```

## Usage

Once installed, you can use the CLI app to retrieve interaction information from either a file or a directory. Here's an example of how to use the app.

```sh
htmlxlsx -f interaction.html outputdir/
```

Replace `interaction.html` with the path to your HTML file and `outputdir` with the path to the output directory for the Interactions.xlsx file.
