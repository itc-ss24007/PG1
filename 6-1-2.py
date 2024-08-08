class Person:
    def __init__(self,
                 name = '',
                 nationality = '',
                 birth = '',
                 address = ''):
        self.name = name
        self.nationality = nationality
        self.birth = birth
        self.address = address

    def show_attributes(self):
        print("名前:",self.name)
        print("国籍:",self.nationality)
        print("生年月日:",self.birth)
        print("住んでいる場所:",self.address)

heroine = Person(name='かぐや姫',nationality='日本',birth='685',address='沖縄県那覇市')
heroine.show_attributes()

hero = Person(name='wang',nationality='china',birth='705',address='沖縄県那覇市')
hero.show_attributes()

