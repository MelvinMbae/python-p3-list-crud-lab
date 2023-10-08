def create_an_empty_list():
    return list()

print(create_an_empty_list())

def create_a_list():
    my_list = ["a","b","c","d"]
    return my_list

print(create_a_list())

def add_element_to_end_of_list(l, element):
    
    l.append(element)
    
    return l

l = create_a_list()
element = 5
    
print(add_element_to_end_of_list(l, element))

def add_element_to_start_of_list(l, element):
    
    l.insert(0, element)
    return l

l = create_a_list()
element = 0

print(add_element_to_start_of_list(l, element))

def remove_element_from_end_of_list(l):
    l.pop()
    return l

l= create_a_list()
print(remove_element_from_end_of_list(l))


def remove_element_from_start_of_list(l):
    
    l.pop(0)
    return l
l= create_a_list()

print(remove_element_from_start_of_list(l))


def retrieve_first_element_from_list(l):
    return l[0]

l= create_a_list()

print(retrieve_first_element_from_list(l))


def retrieve_element_from_index(l, index):
    return l[index]

l= create_a_list()
index = 2

print(retrieve_element_from_index(l, index))


def retrieve_last_element_from_list(l):
    return l[-1]

l = create_a_list()
print(retrieve_last_element_from_list(l))