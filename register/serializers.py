from rest_framework import serializers
import ipdb
from .models import Register

class RegisterResumeSerializer(serializers.Serializer):
    debits = serializers.SerializerMethodField(method_name="sum_debits")
    rewards = serializers.SerializerMethodField(method_name="sum_rewards")
    balance = serializers.SerializerMethodField(method_name="get_current_value")
    years = serializers.SerializerMethodField(method_name="details_years")

    def details_years(self, validated_data):
        years = {}
        for number in validated_data:
            number.year = number.date.year
            number.month = number.date.month
            if (not number.year in years.keys()):
                years[number.year] = {'months': {}}
                years[number.year]["reward_year"] = 0
                years[number.year]["debit_year"] = 0
                years[number.year]["balance_year"] = 0
            if (not number.month in years[number.year]['months']):
                years[number.year]['months'][number.month] = {"debit": 0, "reward": 0}
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
        if (validated_data['type'] == "reward"):
            if (validated_data['category'] != "salary"):
                raise serializers.ValidationError(f"Category {validated_data['category']} is invalid for type reward")
        
        if (validated_data['type'] == "debit"):
            if (validated_data['category'] == "salary"):
                raise serializers.ValidationError(f"Category {validated_data['category']} is invalid for type debit")

        return super().update(instance, validated_data)
    