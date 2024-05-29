class House:
    """A class to store details of a house"""
    def __init__(self, link: str, name: str, address: str, num_bed: float, num_bath: float, sq_feet: int,
                 max_occupant: int, price: int, distant_from_campus: float, phone_number = None):
        self.link = link
        self.name = name
        self.address = address
        self.num_bed = num_bed
        self.num_bath = num_bath
        self.sq_feet = sq_feet
        self.max_occupant = max_occupant
        self.price = price
        self.distant_from_campus = distant_from_campus
        self.phone_number = phone_number

    def __repr__(self) -> str:
        return f'Link: {self.link}\nHouse name: {self.name}\nAdress: {self.address}\nNumber Of Bed: {self.num_bed}\nPrice: {self.price}\nDistant From Campus: {self.distant_from_campus}\nPhone of the renter: {self.phone_number}\n'

