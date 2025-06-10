# esrcizio_1:


class ContactManager:

    def __init__(self):
        
        self.contacts: dict[str, list[str]] = { }
    

    def create_contact(self, name: str, phone_numbers: list[str]) -> dict[str, list[str]]:
        """
        Qualcosa.....

        """

        if type(phone_numbers) != list:

            raise ValueError("!!!")

        if name not in self.contacts:
            self.contacts[name] = phone_numbers
        
        else:
            raise ValueError("Errore, il contatto esiste già!")
        
        return {name:phone_numbers}
    
    def add_phone_number(self, contact_name: str, phone_number: str)  -> dict[str, list[str]]:

        if contact_name in self.contacts[contact_name]:

            if phone_number not in self.contacts[contact_name]:

                self.contacts[contact_name].append(phone_number)
            else:
                raise ValueError("Errore: il contacto già esiste!")
            
        else:

            raise ValueError("")


        '''
        if contact_name not in self.contacts:

            raise ValueError("Errore, il contactto non è all' interno del dizionario")
        
        if phone_number in self.contacts[contact_name]:

            raise ValueError("Errore, il contatto esiste gia!")

        self.contacts[contact_name].append(phone_number)'''

        return{contact_name:self.contacts[contact_name]} 
    

    def remove_phone_number(self, contact_name:str, phone_number: str) -> dict[str,list[str]]:


        if contact_name not in self.contacts:

            raise ValueError("Errore: il contatto no è presente nel dizionario!")

        if phone_number not in self.contacts[contact_name]:

            return ValueError("Errore: il numero di telefono non è presente!")

        self.contacts[contact_name].remove(phone_number)

        return {contact_name: self.contacts[contact_name]}


    def update_phone_number(self, contact_name:str, old_phone_number:str, new_phone_number:str) -> dict[str,list[str]]:


        if contact_name not in self.contacts:
             raise ValueError("Errore: .......!")

        if old_phone_number not in self.contacts[contact_name]:

            raise ValueError("Errore:........!")


        index: int = self.contacts[contact_name].index(old_phone_number)

        self.contacts[contact_name][index] = new_phone_number

        return {contact_name: self.cont[contact_name]}


    def list_contact(self) -> list[str]:

        return list(self.contacts.keys())


    def search_contact_by_phone_number(self, phone_number:str) -> list[str]:

        contacts_found:list = []

        for contact, phone_numbers in self.contacts.items():
            
            if phone_number in phone_numbers:

                contacts_found.append(contact)

        if not contacts_found:

            raise ValueError("Errore:....!")

        return contacts_found

l: list = [i if i%2 == 0 else 0 for i in range(10)]

d_1 = {1: 2, 2: 3}

d_2:dict = {v: k for k,v in d_1.items()}





if __name__ == "__main__":

  rubrica:ContactManager = ContactManager()

  rubrica.create_contact(name="Flavio", phone_numbers=["123345678890"])

  rubrica.create_contact(name="Marco", phone_numbers=["1233875634987"])

  rubrica.create_contact(name="Cecile", phone_numbers=["123390383278"])

print(rubrica.list_contact())

print(rubrica.search_contact_by_phone_number("123390383278"))