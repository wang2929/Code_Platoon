class ContactList:
    all_contacts = {}
    def __init__(self, contact_list_name, contact_list):
        self.title = contact_list_name
        self.contacts = contact_list.sort()
        ContactList.all_contacts[contact_list_name] = contact_list
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if type(value) == str and len(value) > 3:
            self._title
        else:
            print("Invalid contact list name. Unable to make the contact list.")
    @property
    def contacts(self):
        return self._contacts
    @contacts.setter
    def contacts(self, value):
        if type(value) == list:
            self._contacts = value
        else:
            print("Invalid list of contacts. Unable to make the contact list.")
    
    def add_contact(self, person_name, person_number):
        new_contact = {person_name: person_number}
        self.contacts.append(new_contact)
        ContactList.all_contacts.append(new_contact)
    
    