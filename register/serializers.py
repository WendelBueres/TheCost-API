from rest_framework import serializers
from .models import Register
from drf_spectacular.utils import *

@extend_schema_serializer(examples=[OpenApiExample(
name="example",value={
	"rewards": 26600.0,
    "debits": 4610.0,
	"balance": 21990.0,
    "2021": {
        "months": {
            "8": {
                "reward": 200.0,
                "debit": 50.0,
            },
            "9": {
                "reward": 200.0,
                "debit": 100.0,
            },
            "10": {
                "reward": 2000.0,
                "debit": 1000.0,
            },
            "11": {
                "reward": 50.0,
                "debit": 0.0,
            },
            "12": {
                "reward": 100.0,
                "debit": 0.0,
            }
        },
        "reward_year": 2550.0,
        "debit_year": 1150.0,
        "balance_year": 1400.0
    },
    "2022": {
        "months": {
            "1": {
                "reward": 100.0,
                "debit": 10.0,
            },
            "2": {
                "reward": 9000.0,
                "debit": 10000.0,
            },
            "3": {
                "reward": 6000.0,
                "debit": 5000.0,
            },
            "4": {
                "reward": 350.0,
                "debit": 700.0,
            },
            "5": {
                "reward": 8000.0,
                "debit": 5000.0,
            },
            "6": {
                "reward": 100.0,
                "debit": 40.0,
            },
            "7": {
                "reward": 700.0,
                "debit": 90.0,
            },
        "reward_year": 24250.0,
        "debit_year": 20840.0,
        "balance_year": 3410.0
            }},
})])

class RegisterResumeSerializer(serializers.Serializer):
    years = serializers.SerializerMethodField(method_name="details_years")
    rewards = serializers.SerializerMethodField(method_name="sum_rewards")
    debits = serializers.SerializerMethodField(method_name="sum_debits")
    balance = serializers.SerializerMethodField(method_name="get_current_value")

    @extend_schema_field(serializers.DictField)
    def details_years(self, validated_data):
        years = {}
        for number in validated_data:
            number.year = number.date.year
            number.month = number.date.month
            if (not number.year in years.keys()):
                years[number.year] = {'months': {}, "reward_year": 0, "debit_year": 0, "balance_year": 0}
            if (not number.month in years[number.year]['months']):
                years[number.year]['months'][number.month] = {"reward": 0, "debit": 0}
            if (number.type == "debit"):
                years[number.year]['debit_year'] += number.value
                years[number.year]['balance_year'] -= number.value
                years[number.year]['months'][number.month]['debit'] += number.value
            if (number.type == "reward"):
                years[number.year]['reward_year'] += number.value
                years[number.year]['balance_year'] += number.value
                years[number.year]['months'][number.month]['reward'] += number.value
        years = dict(sorted(zip(years.keys(), years.values()))) 

        for year in years:
            years[year]['months'] = dict(sorted(zip(years[year]['months'].keys(), years[year]['months'].values()))) 

        if len(years) == 1:
            for number in years:
                del years[number]['reward_year']
                del years[number]['debit_year']
                del years[number]['balance_year']
        return years
    
    @extend_schema_field(serializers.FloatField)
    def sum_debits(self, validated_data):
        def append_registers(number):
            if (number.type == "debit"):
                return number.value
            else: 
                return 0 

        return sum(map(append_registers, validated_data))
    
    @extend_schema_field(serializers.FloatField)
    def sum_rewards(self, validated_data):
        def append_registers(number):
            if (number.type == "reward"):
                return number.value
            else: 
                return 0 

        return sum(map(append_registers, validated_data))
    
    @extend_schema_field(serializers.FloatField)
    def get_current_value(self, validated_data):
        def sum_debits(self, validated_data):
            def append_registers(number):
                if (number.type == "debit"):
                    return number.value
                else: 
                    return 0 

            return sum(map(append_registers, validated_data))
        
        def sum_rewards(self, validated_data):
            def append_registers(number):
                if (number.type == "reward"):
                    return number.value
                else: 
                    return 0 

            return sum(map(append_registers, validated_data))
                
        debits = sum_debits(self, validated_data)
        rewards = sum_rewards(self, validated_data)
        total = rewards-debits

        return total

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register

        fields = [
            "id",
            "description",
            "value",
            "date",
            "type",
            "category",
        ]

    def create(self, validated_data):
        if (validated_data['value'] < 0):
            raise serializers.ValidationError(f"Value {validated_data['value']} is invalid, value must be greater than 0")
       
        if (validated_data['type'] == "reward"):
            if (validated_data['category'] != "salary"):
                raise serializers.ValidationError(f"Category {validated_data['category']} is invalid for type reward")
        
        if (validated_data['type'] == "debit"):
            if (validated_data['category'] == "salary"):
                raise serializers.ValidationError(f"Category {validated_data['category']} is invalid for type debit")

        return super().create(validated_data)

class RegisterSerializerDetails(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = [
            "id",
            "description",
            "value",
            "date",
            "type",
            "category",
            "user_id"
        ]

    def update(self, instance, validated_data):
        if (validated_data['value'] < 0):
            raise serializers.ValidationError(f"Value {validated_data['value']} is invalid, value must be greater than 0")
        
        if (validated_data['type'] == "reward"):
            if (validated_data['category'] != "salary"):
                raise serializers.ValidationError(f"Category {validated_data['category']} is invalid for type reward")
        
        if (validated_data['type'] == "debit"):
            if (validated_data['category'] == "salary"):
                raise serializers.ValidationError(f"Category {validated_data['category']} is invalid for type debit")

        return super().update(instance, validated_data)
    