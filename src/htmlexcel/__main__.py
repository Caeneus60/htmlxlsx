#!/bin/python3

import glob

import click

from htmlexcel.utils.htmlreader import HTMLReader
from htmlexcel.utils.excelwriter import ExcelWriter
from htmlexcel.utils.interactionfile import InteractionFile


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option("-f", "--file", help="Single html file to parse", type=click.Path())
@click.option(
    "-d",
    "--directory",
    help="Directory to search for html files to parse",
    type=click.Path(
        exists=True,
        readable=True,
    ),
)
@click.argument(
    "out",
    type=click.Path(exists=True, readable=True),
)
def cli(file, directory, out):
    """This script gets interaction info from html to OUT directory as an xlsx file"""
    if file:
        files = [file]
    if directory:
        files = glob.glob(f"{directory}/*.htm*")

    if not files:
        click.echo("Make sure you're giving a file or directory.")
        return

    interaction_files = []

    for file in files:
        html_content = HTMLReader(file)
        data_file = InteractionFile(html_content)
        interaction_files.append(data_file)

    writer = ExcelWriter("Interactions")

    for i, interaction_file in enumerate(interaction_files):
        index = str(i + 1)
        if i == 0:
            writer.current_sheet.title = index
        else:
            writer.workbook.create_sheet(index)
            writer.switch_sheet(index)
        writer.create_table(interaction_file)
        writer.save(out)
        writer.close()


if __name__ == "__main__":
    cli()
