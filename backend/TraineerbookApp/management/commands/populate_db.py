from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.utils import timezone
from datetime import timedelta
from TraineerbookApp.models import ClassRoom, Teacher, Activity, Product, Reservation, Comment, Incident, PAY_METHOD, Billing
from django.contrib.auth import get_user_model
from django.core.files import File

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        # Create ClassRooms
        class_room_1 = ClassRoom.objects.create(name='Class Room 1')
        class_room_2 = ClassRoom.objects.create(name='Class Room 2')

        # Create Teachers
        teacher_1 = Teacher.objects.create(name='Coach David')
        teacher_2 = Teacher.objects.create(name='Coach Carlos')

        # Create Activities
        activity_1 = Activity.objects.create(
            image='assets\kettlebell-2052775_1280.jpg',
            name='Crossfit',
            teacher=teacher_1,
            class_space=class_room_1
        )
        activity_2 = Activity.objects.create(
            image='assets\weightlifting-5730110_1280.jpg',
            name='Halterofilia',
            teacher=teacher_2,
            class_space=class_room_2
        )

        # Create Products
        product_1 = Product.objects.create(
            product_hour_init=timezone.now(),
            product_hour_fin=timezone.now() + timedelta(hours=2),
            quantity=10,
            price=50,
            activity=activity_1
        )
        product_2 = Product.objects.create(
            product_hour_init=timezone.now(),
            product_hour_fin=timezone.now() + timedelta(hours=1),
            quantity=5,
            price=30,
            activity=activity_2
        )

        # Create Users (if not already created)
        user_model = get_user_model()
        user_1, created = user_model.objects.get_or_create(username='user1', defaults={'password': 'password'})
        user_2, created = user_model.objects.get_or_create(username='user2', defaults={'password': 'password'})

        # Create Reservations
        reservation_1 = Reservation.objects.create(
            user=user_1,
            product=product_1,
            buy_date=timezone.now().date(),
            buy_method=PAY_METHOD[0][0]  # Assuming the first payment method is 'online'
        )
        reservation_2 = Reservation.objects.create(
            user=user_2,
            product=product_2,
            buy_date=timezone.now().date(),
            buy_method=PAY_METHOD[1][0]  # Assuming the second payment method is 'payback'
        )

        # Create Comments
        comment_1 = Comment.objects.create(
            user=user_1,
            activity=activity_1,
            content='This is a comment about Activity 1.'
        )
        comment_2 = Comment.objects.create(
            user=user_2,
            activity=activity_2,
            content='This is a comment about Activity 2.'
        )

        # Create Incidents
        incident_1 = Incident.objects.create(
            user=user_1,
            reservation=reservation_1,
            content='Incident content related to Reservation 1.'
        )
        incident_2 = Incident.objects.create(
            user=user_2,
            reservation=reservation_2,
            content='Incident content related to Reservation 2.'
        )

        # Create Billings
        billing_1 = Billing.objects.create(
            user=user_1,
            billing_address='Billing Address 1'
        )
        billing_2 = Billing.objects.create(
            user=user_2,
            billing_address='Billing Address 2'
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data.'))
