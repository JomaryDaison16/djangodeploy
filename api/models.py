from django.db import models

# Create your models here.

# class Token(models.Model):
#     token = models.CharField(max_length=2000)
#     ttl = models.IntegerField()
#     date_added = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return "{0} - {1}".format(self.token, self.ttl)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    date_added = models.DateField(auto_now_add=True)
    # token_id = models.ForeignKey(Token, null=True, on_delete=models.CASCADE)
    usertype = models.IntegerField(null=False, default=2)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name, self.email, self.usertype)
=======
class Token(models.Model):
    # id = models.Autofield(primary_key=True)
    token = models.CharField(max_length=100)
    ttl = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.token, self.ttl)

class Superadmin(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    date_added = models.DateField(auto_now_add=True)
    # token_id = models.ForeignKey(Token, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name, self.email, self.token_id)
    token_id = models.ForeignKey(Token, null=True, on_delete=models.CASCADE)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

class Subadmin(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    date_added = models.DateField(auto_now_add=True)
    # token_id = models.ForeignKey(Token, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name, self.email, self.token_id)
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

class Borrower(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    date_added = models.DateField(auto_now_add=True)
    # token_id = models.ForeignKey(Token, null=True, on_delete=models.CASCADE)
    token_id = models.ForeignKey(Token, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name, self.email, self.token_id)

class Facility(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(default='None')
    image = models.TextField(default='https://images.unsplash.com/photo-1522165078649-823cf4dbaf46?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=756f069c98c96a701453b1e27630e961&auto=format&fit=crop&w=750&q=80')
    date_added = models.DateField(auto_now_add=True)
    status = models.IntegerField()
    borrower_id = models.IntegerField(default=0)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name, self.status, self.borrower_id)

class Equipment(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(default='None')
    image = models.TextField(default='https://images.unsplash.com/photo-1531988042231-d39a9cc12a9a?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=a562d48d64fd49e7cd0419f70806d696&auto=format&fit=crop&w=750&q=80')
    date_added = models.DateField(auto_now_add=True)
    status = models.IntegerField()
    quantity = models.IntegerField(default=1)
    borrower_id = models.IntegerField(default=0)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name, self.status, self.quantity, self.borrower_id)

class Reservation(models.Model):
    borrower_id = models.IntegerField(default=0)
    item_id = models.IntegerField(default=0)
    reserve_type = models.CharField(max_length=20, default='none')
    eventname = models.TextField(default=' ')
    quantity = models.IntegerField(default=0)
    date_application = models.DateField(auto_now_add=True)
    year = models.IntegerField(default=2018)
    month = models.IntegerField(default=0)
    start_day = models.IntegerField(default=0)
    end_day = models.IntegerField(default=0)
    start_time = models.IntegerField(default=0)
    end_time = models.IntegerField(default=0)
    remarks = models.TextField(default='none')
    status = models.IntegerField(default=0)

    def __str__(self):
        return "{0} - {1} - {2} - {3}".format(self.borrower_id, self.item_id, self.date_application, self.status)


class Schedule(models.Model):
    info = models.CharField(max_length=200)
    day = models.IntegerField(default=1)
    month = models.IntegerField(default=1)
    year = models.IntegerField(default=2018)
    time_start = models.IntegerField(default=6)
    time_end = models.IntegerField(default=21)
    item_type = models.IntegerField(default=0)
    item_id = models.IntegerField(default=0)

    def __str__(self):
        return "{0} - {1} - {2} - {3}".format(self.info, self.day, self.month, self.year)

class Logs(models.Model):
    date = models.DateField(auto_now_add=True)
    borrower = models.IntegerField(null=True)
    admin = models.IntegerField(null=True)
    message = models.TextField(default='None')

    def __str__(self):
        return "{0} - {1} - {2} - {3}".format(self.date, self.borrower, self.admin, self.message)
    date_added = models.DateField(auto_now_add=True)
    status = models.IntegerField()
    quantity = models.IntegerField()
    borrower_id = models.ForeignKey(Borrower, null=True, on_delete=models.CASCADE)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

class Equipment(models.Model):
    name = models.CharField(max_length=70)
    date_added = models.DateField(auto_now_add=True)
    status = models.IntegerField()
    quantity = models.IntegerField()
    borrower_id = models.ForeignKey(Borrower, null=True, on_delete=models.CASCADE)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)
        # return "{0} - {1} - {2}".format(self.name, self.status, self.borrower_id)

class Reservation(models.Model):
    Reserver_ID = models.IntegerField()
    Status = models.IntegerField()
    Cancelled = models.IntegerField()
    Type = models.IntegerField()
    Name_reserved = models.CharField(max_length=50)
    Date_Resereved = models.DateField(auto_now_add=True)
    Date_Return = models.DateField()
    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)
    #     return "{0} - {1} - {2}".format(self.Reserver_ID, self., self.,self.,self.,self.,self.)

class BorrowerLogs(models.Model):
    Borrower_ID = models.IntegerField()
    Approver_ID = models.IntegerField()
    Type = models.IntegerField()
    Name_Borrowed = models.CharField(max_length=50)
    Date_Borrowed = models.DateField()
    Date_Return = models.DateField()
    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)
    #     return "{0} - {1} - {2}x".format(self.Borrower_ID, self.Approver_ID, self.Type,self.Name_Borrowed,self.Date_Borrowed,self.Date_Return)

class Logs(models.Model):
    User_ID = models.IntegerField()
    action = models.CharField(max_length=50)
    Date = models.DateField(auto_now_add=True)
    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)
    #     return "{0} - {1} - {2}".format(self.User_ID, self.action, self.Date)
