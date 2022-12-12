from django.db import models


class User(models.Model):  # model name
    """
    A model for Users table
    """
    username = models.CharField(max_length=24,  # field max length
                                blank=False,  # required
                                primary_key=True,  # is a primary key
                                help_text="This represents the username.",  # field guide
                                verbose_name="Username",  # human-readable field definition
                                )  # field definition
    birth_date = models.DateField(blank=False,
                                  primary_key=False,
                                  help_text="This represents the user birth date.",
                                  verbose_name="Birth date",
                                  )
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    # Nested

    # episode_owner_season = models.ForeignKey(Season,
    #                                          on_delete=models.CASCADE,
    #                                          related_name="episodes",
    #                                          help_text="This represents the episode owner season.",
    #                                          verbose_name="Episode owner season",
    #                                          )

    def __str__(self):
        return self.username
