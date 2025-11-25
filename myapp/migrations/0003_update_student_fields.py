# Generated migration for updating Student model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_student_issuedbook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_class',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='roll',
            new_name='id_number',
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['id_number']},
        ),
    ]
