class Resume:
    def __init__(self,name,age,gender,address,email,skills = ['Softawwre']):
        self.name = name
        self.age = self.validate_age(age)
        self.gender = gender
        self.address = address
        self.email = self.validate_email(email)
        self.skills = skills or []

    # UPDATEING VALUES
    def update_contacting(self,phonenumber= None,email=None):
        if phonenumber:
            self.phonenumber = phonenumber
        if email:
            self.email = email
        
    # Data Validation
    def validate_age(self, age):
        if age < 18:
            raise ValueError('Age must be 18 and over')
        else:
            return age
    def validate_email(self ,email):
        if '@' not in email or '.' not in email:
            raise ValueError('Invalid email address')
        else:
            return 

    def display_resume(self):
        print(f'name:{self.name},age:{self.age},gender:{self.gender},addres:{self.address},email:{self.email},skills:{self.skills}')
        
resume1 = Resume('Jeff',23,'M','Nairobi,Kenya','jess@gamil.com',['javascript'])

resume1.update_contacting('0111','me@gmail.com')
resume1.display_resume()