from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from TraineerbookApp.models import BlobImage, ClassRoom, Teacher, Activity, Product, Reservation, Comment, Incident, PAY_METHOD, Billing
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        # Create ClassRooms
        class_room_1 = ClassRoom.objects.create(name='Class Room 1')
        class_room_2 = ClassRoom.objects.create(name='Class Room 2')
        class_room_3 = ClassRoom.objects.create(name='Class Room 3')
        class_room_4 = ClassRoom.objects.create(name='Class Room 4')
        class_room_5 = ClassRoom.objects.create(name='Class Room 5')
        class_room_6 = ClassRoom.objects.create(name='Class Room 6')
        # Create Teachers
        teacher_1 = Teacher.objects.create(name='Coach David')
        teacher_2 = Teacher.objects.create(name='Coach Carlos')
        teacher_3 = Teacher.objects.create(name='Coach Fernando')
        teacher_4 = Teacher.objects.create(name='Coach Juan Carlos')
        teacher_5 = Teacher.objects.create(name='Coach Raul')

        image_activity_1 = BlobImage.objects.create()
        image_activity_1.save_image('../assets/sample_data/images/kettlebell-2052775_1280.jpg')
        image_activity_2 = BlobImage.objects.create()
        image_activity_2.save_image('../assets/sample_data/images/weightlifting-5730110_1280.jpg')
        image_activity_3 = BlobImage.objects.create()
        image_activity_3.save_image('../assets/sample_data/images/Bodypump.jpg')
        image_activity_4 = BlobImage.objects.create()
        image_activity_4.save_image('../assets/sample_data/images/entrenamiento-funcional.jpeg')
        image_activity_5 = BlobImage.objects.create()
        image_activity_5.save_image('../assets/sample_data/images/Bnatacion.jpg')
        image_activity_6 = BlobImage.objects.create()
        image_activity_6.save_image('../assets/sample_data/images/pilates.jpeg')
        image_activity_7 = BlobImage.objects.create()
        image_activity_7.save_image('../assets/sample_data/images/street-workout-2628919_1280.jpg')

        # Create Activities
        activity_1 = Activity.objects.create(
            image=image_activity_1,
            name='Crossfit',
            description='Técnica de entrenamiento que conecta movimientos de diferentes disciplinas, tales como la halterofilia, el entrenamiento metabólico o el gimnástico',
            teacher=teacher_1,
            class_space=class_room_1
        )
        activity_2 = Activity.objects.create(
            image=image_activity_2,
            name='Halterofilia',
            description='La halterofilia es un deporte olímpico, también conocido como levantamiento de pesas, esta disciplina requiere de un gran entrenamiento de los músculos del cuerpo para adquirir la fuerza necesaria para los levantamientos, además de desarrollar destreza y actitud mental.',
            teacher=teacher_2,
            class_space=class_room_2
        )
        activity_3 = Activity.objects.create(
            image=image_activity_3,
            name='Bodypump',
            description='El Body Pump es un programa de entrenamiento físico intenso que combina actividad aeróbica y trabajo muscular mediante el levantamiento de pesas al ritmo de la música',
            teacher=teacher_3,
            class_space=class_room_3
        )
        activity_4 = Activity.objects.create(
            image=image_activity_4,
            name='Entrenamiento funcional',
            description='El entrenamiento funcional es un medio de entrenamiento basado en la realización de movimientos libres o con resistencias, en muchos casos en superficies inestables, que guardan relación con gestos comunes a la actividad deportiva que realicemos.',
            teacher=teacher_4,
            class_space=class_room_4
        )
        activity_5 = Activity.objects.create(
            image=image_activity_5,
            name='Natacion',
            description='La natación es el arte de sostenerse y avanzar, usando los brazos y las piernas, sobre o bajo el agua. Puede realizarse como actividad lúdica o como deporte de competición. Debido a que los seres humanos no nadan instintivamente, la natación es una habilidad que debe ser aprendida.',
            teacher=teacher_5,
            class_space=class_room_5
        )
        activity_6 = Activity.objects.create(
            image=image_activity_6,
            name='Pilates',
            description='Es un deporte en el que se trabajan el cuerpo y la mente, y cuyos objetivos principales son reforzar la musculatura (desde la más profunda a la más superficial), aumentar la fuerza y la flexibilidad del cuerpo y mejorar la capacidad de concentración.',
            teacher=teacher_1,
            class_space=class_room_6
        )
        activity_7 = Activity.objects.create(
            image=image_activity_7,
            name='Calistenia',
            description='La calistenia es un sistema de entrenamiento con ejercicios físicos que se realizan con el propio peso corporal',
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

        product_3 = Product.objects.create(
            product_hour_init=timezone.now(),
            product_hour_fin=timezone.now() + timedelta(hours=1),
            quantity=5,
            price=30,
            activity=activity_3
        )
        product_4 = Product.objects.create(
            product_hour_init=timezone.now(),
            product_hour_fin=timezone.now() + timedelta(hours=1),
            quantity=5,
            price=30,
            activity=activity_4
        )
        product_5 = Product.objects.create(
            product_hour_init=timezone.now(),
            product_hour_fin=timezone.now() + timedelta(hours=1),
            quantity=5,
            price=30,
            activity=activity_5
        )
        product_6 = Product.objects.create(
            product_hour_init=timezone.now()+ timedelta(hours=1),
            product_hour_fin=timezone.now() + timedelta(hours=2),
            quantity=5,
            price=30,
            activity=activity_6
        )
        product_7 = Product.objects.create(
            product_hour_init=timezone.now()+ timedelta(hours=1),
            product_hour_fin=timezone.now() + timedelta(hours=2),
            quantity=5,
            price=30,
            activity=activity_7
        )
        product_8 = Product.objects.create(
            product_hour_init=timezone.now()+ timedelta(hours=1),
            product_hour_fin=timezone.now() + timedelta(hours=2),
            quantity=5,
            price=30,
            activity=activity_1
        )

        # Create Users (if not already created)
        user_model = get_user_model()
        user_1, created = user_model.objects.get_or_create(username='user1', defaults={'password': 'password'})
        user_2, created = user_model.objects.get_or_create(username='user2', defaults={'password': 'password'})
        user_3, created = user_model.objects.get_or_create(username='user3', defaults={'password': 'password'})
        user_4, created = user_model.objects.get_or_create(username='user4', defaults={'password': 'password'})
        user_5, created = user_model.objects.get_or_create(username='user5', defaults={'password': 'password'})

        # Create Reservations
        reservation_1 = Reservation.objects.create(
            user=user_1,
            product=product_1,
            buy_date=timezone.now().date(),
            buy_method=PAY_METHOD[0][0]  
        )
        reservation_2 = Reservation.objects.create(
            user=user_2,
            product=product_2,
            buy_date=timezone.now().date(),
            buy_method=PAY_METHOD[1][0]  
        )
        reservation_3 = Reservation.objects.create(
            user=user_3,
            product=product_3,
            buy_date=timezone.now().date(),
            buy_method=PAY_METHOD[0][0]  
        )
        reservation_4 = Reservation.objects.create(
            user=user_4,
            product=product_4,
            buy_date=timezone.now().date(),
            buy_method=PAY_METHOD[0][0]  
        )
        reservation_5 = Reservation.objects.create(
            user=user_5,
            product=product_5,
            buy_date=timezone.now().date(),
            buy_method=PAY_METHOD[0][0]  
        )
        reservation_6 = Reservation.objects.create(
            user=user_1,
            product=product_6,
            buy_date=timezone.now().date(),
            buy_method=PAY_METHOD[0][0]  
        )
        reservation_7 = Reservation.objects.create(
            user=user_2,
            product=product_7,
            buy_date=timezone.now().date(),
            buy_method=PAY_METHOD[0][0]  
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
        comment_3 = Comment.objects.create(
            user=user_3,
            activity=activity_3,
            content='This is a comment about Activity 3.'
        )
        comment_4 = Comment.objects.create(
            user=user_4,
            activity=activity_4,
            content='This is a comment about Activity 4.'
        )
        comment_5 = Comment.objects.create(
            user=user_5,
            activity=activity_5,
            content='This is a comment about Activity 5.'
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
        billing_3 = Billing.objects.create(
            user=user_3,
            billing_address='Billing Address 3'
        )
        billing_4 = Billing.objects.create(
            user=user_4,
            billing_address='Billing Address 4'
        )
        billing_5 = Billing.objects.create(
            user=user_5,
            billing_address='Billing Address 5'
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data.'))
