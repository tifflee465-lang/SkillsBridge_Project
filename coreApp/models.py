from django.db import models

# Create your models here.


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} from {self.name}"


class HelpRequest(models.Model):
    ISSUE_CHOICES = [
        ('account', 'Account Issue'),
        ('skills', 'Skills Upload Issue'),
        ('bug', 'Bug Report'),
        ('general', 'General Inquiry'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    issue_type = models.CharField(max_length=20, choices=ISSUE_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.issue_type} - {self.email}"

