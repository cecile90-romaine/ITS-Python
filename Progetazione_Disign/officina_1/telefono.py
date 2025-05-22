from typing import Self
import re

class Telefono(str):
	def __new__(cls, t:str|Self)->Self:
		if not re.fullmatch('\+?[0-9]+', t):
			raise ValueError(f"Value t == {t} does not comply to standard")
		return str.__new__(cls, t)