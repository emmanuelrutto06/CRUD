from rest_framework import serializers
from . models import students

class studentsSerializer(serializers.ModelSerializer):
    firstname=serializers.CharField(required=False)
    lastname=serializers.CharField(required=False)
    # student_id=serializers.IntegerField(required=False)
    stream=serializers.CharField(required=False)
    Date_of_suspension=serializers.DateField(required=False)
    return_date=serializers.DateField(required=False)
    # timestamp = serializers.DateField(required=False)
    Reason_of_suspension=serializers.CharField(required=False)
    Teachers_sign=serializers.CharField(required=False)
    # Adm_No = serializers.CharField(required=False)


    class Meta:
        model=students
        fields='__all__'