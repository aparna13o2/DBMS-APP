from django.db import models

class Employee1(models.Model):
    employee_name = models.CharField(max_length=20)
    e_id = models.IntegerField(primary_key=True)  # Changed from AutoField to IntegerField
    salary = models.IntegerField()
    date_of_joining = models.DateField()

class Employee21(models.Model):
    e_id = models.ForeignKey(Employee1, on_delete=models.CASCADE)
    phone = models.BigIntegerField()

    class Meta:
        unique_together = (('e_id', 'phone'),)

class E221(models.Model):
    e_id = models.OneToOneField(Employee1, on_delete=models.CASCADE, primary_key=True)
    house_name = models.CharField(max_length=20)
    pin_code = models.IntegerField()
    landmark = models.CharField(max_length=20)

class E222(models.Model):
    pin_code = models.IntegerField(primary_key=True)  # Changed from AutoField to IntegerField
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)

class Depot1(models.Model):
    depot_id = models.IntegerField(primary_key=True)  # Changed from AutoField to IntegerField
    capacity = models.IntegerField()

class Depot2(models.Model):
    depot_id = models.OneToOneField(Depot1, on_delete=models.CASCADE, primary_key=True)
    place = models.CharField(max_length=20)
    pincode = models.IntegerField()
    district = models.CharField(max_length=20)

class Route12(models.Model):
    duration = models.IntegerField(primary_key=True)  # Changed from AutoField to IntegerField
    refreshment_time = models.IntegerField()

class Route11(models.Model):
    route_id = models.IntegerField(primary_key=True)  # Changed from AutoField to IntegerField
    destination = models.CharField(max_length=20)
    distance = models.IntegerField()
    type_of_service = models.CharField(max_length=20)
    duration = models.ForeignKey(Route12, on_delete=models.CASCADE)

class Route2(models.Model):
    route_id = models.ForeignKey(Route11, on_delete=models.CASCADE)
    main_stops = models.CharField(max_length=20)

    class Meta:
        unique_together = (('route_id', 'main_stops'),)

class Bus(models.Model):
    bonnet_no = models.CharField(max_length=20, primary_key=True)
    registration_no = models.CharField(max_length=20)
    capacity = models.IntegerField()
    status = models.CharField(max_length=20)
    bus_type = models.CharField(max_length=20)

class Passenger(models.Model):
    passenger_id = models.IntegerField(primary_key=True)  # Changed from AutoField to IntegerField
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    concession_eligibility = models.BooleanField()

class Ticket1(models.Model):
    date = models.DateField()
    time = models.TimeField()
    bonnet_no = models.ForeignKey(Bus, on_delete=models.CASCADE)
    start = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)

    class Meta:
        unique_together = (('date', 'time', 'bonnet_no'),)

class Ticket2(models.Model):
    start = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    fare = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = (('start', 'destination'),)

class WorksFor(models.Model):
    employee = models.ForeignKey(Employee1, on_delete=models.CASCADE)
    depot = models.ForeignKey(Depot1, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('employee', 'depot'),)

class WorksIn(models.Model):
    employee = models.ForeignKey(Employee1, on_delete=models.CASCADE)
    bonnet_no = models.ForeignKey(Bus, on_delete=models.CASCADE)
    shift_type = models.CharField(max_length=20)
    date = models.DateField()

    class Meta:
        unique_together = (('employee', 'bonnet_no', 'date'),)

class TravelsIn(models.Model):
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
    bonnet_no = models.ForeignKey(Bus, on_delete=models.CASCADE)

class GoesThrough(models.Model):
    bonnet_no = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route_id = models.ForeignKey(Route11, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('bonnet_no', 'route_id'),)

class StartsFrom1(models.Model):
    route_id = models.OneToOneField(Route11, on_delete=models.CASCADE, primary_key=True)
    depot_id = models.ForeignKey(Depot1, on_delete=models.CASCADE)

class StartsFrom2(models.Model):
    route_id = models.ForeignKey(Route11, on_delete=models.CASCADE)
    portion_no = models.IntegerField()

    class Meta:
        unique_together = (('route_id', 'portion_no'),)