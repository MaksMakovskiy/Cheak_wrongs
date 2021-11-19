import json
from typing import Any
from flask import jsonify

class CrudUser:
	def __init__(self, filename: str) -> None:
		self.filename = filename
		self.read_from_file()

	def read_from_file(self) -> None:
		with open(self.filename, "r") as file:
			self.data = json.load(file)

	def get_all_user(self) -> list[str, str]:
		return list(self.data)

	def write_to_file(self) -> None:
		with open(self.filename, "w") as file:
			json.dump(self.data, file)

	def add_new_user(self, login: str, data: dict[str, Any]) -> None:
		if login not in self.data:
			raise ValueError(f"User with login {login} alredy exists")

		self.set_items(login, data)

	def set_items(self, login: str, password: dict[str, Any]) -> None:
		self.data[login] = password

	def get_item(self, login: str) -> dict[str, Any]:
		return self.data[login]

	def delete_item(self, login: str) -> dict[str, Any]:
		del self.data[login]