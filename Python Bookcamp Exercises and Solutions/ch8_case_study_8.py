class ComputerScienceCourse:
    def __init__(self, institution_name='st. stephen', third_subject='compiler design'):
        self.institution_name = institution_name.title()
        self.first_subject = 'Mathematics'
        self.second_subject = 'Soft Skills'
        self.third_subject = third_subject

    def show_details(self):
        print(f'''
    Institution name: {self.institution_name} college.
    Computer science course includes:
    1. {self.first_subject}.
    2. {self.second_subject}.
    3. {self.third_subject.title()}.
    {'-' * 10}
    ''')


details1 = ComputerScienceCourse('presidency', 'python programming')
details1.show_details()
details2 = ComputerScienceCourse()
details2.show_details()

    # Institution name: Presidency college.
    # Computer science course includes:
    # 1. Mathematics.
    # 2. Soft Skills.
    # 3. Python Programming.
    # ----------

    # Institution name: St. Stephen college.
    # Computer science course includes:
    # 1. Mathematics.
    # 2. Soft Skills.
    # 3. Compiler Design.
    # ----------