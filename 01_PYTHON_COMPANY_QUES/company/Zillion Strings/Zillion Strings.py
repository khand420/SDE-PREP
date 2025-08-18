# Write a Django model for a blog application with ‘Post’ and ‘Comment’ models.


# from django.models import models

# class Post(models.Model):
#     user = models.Foriegnkey(User)  
#     title = models.Charfield()
#     desc = models.Charfield()
#     comment = models.Foriegnkey(Comment, onDelte_cascade = True)
#     # comments = models.Charfield()


# class Comment(models.Model):
#     # comment = models.Foriegnkey(Post, onDelte_cascade = True)
#     comments = models.Charfield()


# data = Post.select_related(‘Comment’)    


from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)  # Specify max_length
    desc = models.TextField()  # Use TextField for longer descriptions

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # Link to Post
    comment_text = models.TextField()  # Use TextField for comments

    def __str__(self):
        return self.comment_text[:20]  # Return first 20 characters of the comment


# data = Post.objects.prefetch_related('comments').all()


