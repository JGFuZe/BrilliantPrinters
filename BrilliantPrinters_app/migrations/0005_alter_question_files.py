# Generated by Django 4.2.6 on 2023-11-21 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "BrilliantPrinters_app",
            "0004_questionfile_remove_question_file_question_files",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="files",
            field=models.ForeignKey(
                default=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="BrilliantPrinters_app.questionfile",
            ),
        ),
    ]
