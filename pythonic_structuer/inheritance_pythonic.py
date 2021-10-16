class Person():
    """
        first_name: str, optional
    """

    def __init__(self, *args, **kwargs):
        first_name = kwargs.get('first_name', None)
        last_name = kwargs.get('last_name', None)
        self.first_name = first_name if first_name else args[0]
        self.last_name = last_name if last_name else args[1]

    def __str__(self):
        # return ' '.join([self.first_name, self.last_name])
        return 'its breaking'

    def get_person_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name
        }


class Teenager(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        phone_number = kwargs.get('phone_number', None)
        website = kwargs.get('website', None)
        self.phone_number = phone_number if phone_number else args[2]
        self.website = website if website else args[3]

    # def __str__(self):
    #     return ' '.join([self.first_name, self.last_name, self.phone_number, self.website])

    def get_person_dict(self):
        return_dict = super().get_person_dict()
        return_dict['phone_number'] = self.phone_number
        return_dict['website'] = self.website
        return return_dict

a = Person('John', 'Doe')
b = Person(last_name='Bobby', first_name='Ricky')
c = Teenager('Boy', 'George', 2543667707, 'joehoward.com')
d = Teenager(first_name='Jack', phone_number='1231231111', last_name='Black', website='google.com')

print('\t'.join([str(a), str(b), str(c), str(d)]))
# print('\t'.join([dict(a), dict(b), dict(c), d.__dict__]))
