from dataclasses import dataclass


@dataclass
class Atom:
    """
    Receives a list to construct attributes, must be 5 in length.
    Formats and represents atom information.
    """

    number: str
    name: str
    res_name: str
    res_num: str
    chain: str

    def __str__(self):
        return (
            f"Atom Number: {self.number}\nAtom Name: {self.name}\nRes Name: {self.res_name}\n"
            f"Res Number: {self.res_num}\nChain: {self.chain}\n"
        )

    def __repr__(self):
        return f"<Atom ({self.name}, {self.number}) >"
