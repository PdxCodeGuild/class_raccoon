from django.db import models

class TodoItem(models.Model):
    text = models.TextField()
    due_date = models.DateField(
        null = True,
        blank = True
    )
    creation_date = models.DateField(auto_now=True)
    priority = models.CharField(
        max_length = 8,
        choices=(
            ('0', "Low"),
            ('1', "Medium"),
            ('2', "High")
        )
    )
    completed = models.BooleanField()

    def __str__(self):
        text_caps = self.text_caps()
        prior = self.prior()
        return text_caps + ' | Due date: ' + str(self.due_date) + ' | Created: ' + str(self.creation_date) + ' | Priority: ' + prior + ' | Completed: ' + str(self.completed)

    def text_caps(self):
        text_caps = self.text.capitalize()
        return text_caps

    def prior(self):
        if self.priority == '2':
            prior = "High"
        elif self.priority == '1':
            prior = "Medium"
        else:
            prior = "Low"
        return prior
