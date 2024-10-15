import openpyxl

from htmlexcel.utils.interactionfile import InteractionFile


class ExcelWriter:
    def __init__(self, filename):
        self.filename = filename
        self.workbook = openpyxl.Workbook()
        self.current_sheet = self.workbook.active

    def switch_sheet(self, sheetname: str):
        self.current_sheet = self.workbook[sheetname]

    def create_table(self, data: InteractionFile):
        headings = data.get_headings()

        self.current_sheet.append(headings)

        for interaction in data.interactions:
            row = interaction.format()
            self.current_sheet.append(row)

    def save(self, directory):
        if ".xlsx" not in self.filename:
            self.filename += ".xlsx"

        self.workbook.save(f"{directory}/{self.filename}")

    def close(self):
        self.workbook.close()
