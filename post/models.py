from django.db import models

from users.models import User


# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_posts")
    text_content = models.TextField()
    created_at = models.DateTimeField(auto_created=True)
    users_that_likes = models.ManyToManyField(User, related_name="liked_posts")
    image = models.ImageField()

    @property
    async def like_count(self):
        return await self.users_that_likes.acount()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_created=True)
