from contact_list import ContactList


alice = {
    'name': 'alice',
    'number' : '867-5309'
}
bob = {
    'name': 'bob',
    'number' : '555-5555'
}
carol = {
    'name': 'carol',
    'number' : '123-4567'
}
dan = {
    'name': 'dan',
    'number' : '987-6543'
}
eve = {
    'name': 'eve',
    'number' : '711-2022'
}
friends =[bob, carol, dan]
neighbors = [dan, carol, bob, alice]
work =[dan, bob, eve]
def test_contact_list():
    my_list = ContactList('My Friends', friends)
    assert my_list.name == 'My Friends'
    assert my_list.contacts == friends

def test_contact_list_sort():
    my_list = ContactList('My Friends', neighbors)
    person1 = my_list.contacts[0]
    assert person1['name'] == 'alice'

def test_add_contact():
    empty_contact_book = ContactList('My friends :(', [])
    francisco = {'name': 'francisco', 'number': '65323548291'}
    empty_contact_book.add_contact(francisco)
    assert len(empty_contact_book.contacts) == 1
    assert isinstance(empty_contact_book.contacts, list)

def test_remove_contact():
    newList = ContactList('my list', [bob, carol])
    newList.remove_contact('bob')
    assert len(newList.contacts) == 1
    assert newList.contacts[0] == carol

def test_shared_contacts():
    """Within the two contact lists friends and work, there should only be bob and dan that are shared"""
    friend_contacts = ContactList('friends', friends)
    work_contacts = ContactList('work', work)
    mutuals = friend_contacts.find_shared_contacts(work_contacts)
    assert isinstance(mutuals, ContactList)
    assert len(mutuals.contacts) == 2
    assert mutuals.contacts[0] == bob
    assert mutuals.contacts[1] == dan




