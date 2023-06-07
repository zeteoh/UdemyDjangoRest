from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review

def name_length(value):
    """Validation 

    Args:
        value (_type_): type charfield that takes in name of the field

    Raises:
        serializers.ValidationError: check if the field is valid 
    """
    if len(value) < 2:
        raise serializers.ValidationError('Name must be at least 2 characters long')
    
class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ['watchlist']
        
class WatchListSerializer(serializers.ModelSerializer):
    # shows list of reviews when querying for watchlist in the postman
    # reviews = ReviewSerializer(many=True, read_only=True)
    # shows platform name such as NETFLIX instead of ID such as 10
    platform = serializers.CharField(source='platform.name')
    """
        Dont have to initialise create and update methods, model serializers will handle it themselves.
        But validators will need to be implemented for all models
    """
    # adding a custom field that is not initially initialized in our model
    # len_name = serializers.SerializerMethodField()
    class Meta:
        model = WatchList
        fields = '__all__'
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         """Updates an existing Movie object based on the provided validated data

#         Args:
#             instance (_type_): _description_
#             validated_data (_type_): _description_

#         Returns:
#             _type_: _description_
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         """Object level validation that checks for the object instead of a specific field

#         Args:
#             data (_type_): takes in data of the object

#         Raises:
#             serializers.ValidationError: raises an error if the name is the same as the description string

#         Returns:
#             _type_: returns the data if validation is successful
#         """
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Title and description cannot be the same')
#         return data
        
    # def validate_name(self, value):
    #     """Field level validation for name field

    #     Args:
    #         value (_type_): type charfield that takes in name of the field

    #     Raises:
    #         serializers.ValidationError: check if the field is valid 

    #     Returns:
    #         _type_: a valid value type since the field is over the length of 2
    #     """
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name must be at least 2 characters long')
    #     else:
    #         return value